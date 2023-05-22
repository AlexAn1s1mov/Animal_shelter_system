from sklearn.datasets import load_files
import asyncio
from keras.utils import np_utils
import numpy as np
from glob import glob
import cv2
import random
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tqdm import tqdm
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Dropout, Flatten, Dense, Activation
from keras.models import Sequential
from keras.optimizers import Adam, Adamax
from keras.callbacks import ModelCheckpoint
random.seed(8675309)
import matplotlib.pyplot as plt


# define function to load train, test, and validation datasets
def load_dataset(path):
    data = load_files(path)
    dog_files = np.array(data['filenames'])
    dog_targets = np_utils.to_categorical(np.array(data['target']), 133)
    return dog_files, dog_targets



# returns "True" if face is detected in image stored at img_path
def face_detector(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    return len(faces) > 0

def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def paths_to_tensor(img_paths):
    list_of_tensors = [path_to_tensor(img_path) for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)



def ResNet50_predict_labels(img_path):
    # returns prediction vector for image located at img_path
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))

### returns "True" if a dog is detected in the image stored at img_path
def dog_detector(img_path):
    prediction = ResNet50_predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151))

def extract_Resnet50(tensor):
    from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
    return ResNet50(weights='imagenet', include_top=False).predict(preprocess_input(tensor))

def ResNet50_predict_breed(img_path):
    # extract bottleneck features
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
    # obtain predicted vector
    predicted_vector = ResNet_model.predict(bottleneck_feature)
    # return dog breed that is predicted by the model
    breed = dog_names[np.argmax(predicted_vector)]
    #img = cv2.imread(img_path)
    #cv_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #imgplot = plt.imshow(cv_rgb)
    if dog_detector(img_path) == True:
        return f"Порода данной собаки {breed}"
    if face_detector(img_path) == True:
        return f"На изображении человек"
    else:
        return f"На изображении нет собаки или человека"

def train_model():
    # load train, test, and validation datasets
    # train_files, train_targets = load_dataset('dogImages/train')
    # valid_files, valid_targets = load_dataset('dogImages/valid')
    # test_files, test_targets = load_dataset('dogImages/test')
    train_files, train_targets = load_dataset('Classifier/dogImages/train')
    valid_files, valid_targets = load_dataset('Classifier/dogImages/valid')
    test_files, test_targets = load_dataset('Classifier/dogImages/test')

    # load list of dog names
    global dog_names
    dog_names = [item[31:-1] for item in sorted(glob("Classifier/dogImages/train/*/"))]

    # load filenames in shuffled human dataset
    human_files = np.array(glob("Classifier/lfw/*/*"))
    random.shuffle(human_files)

    # extract pre-trained face detector
    global face_cascade
    face_cascade = cv2.CascadeClassifier('Classifier/haarcascades/haarcascade_frontalface_alt.xml')

    # define ResNet50 model
    global ResNet50_model
    ResNet50_model = ResNet50(weights='imagenet')


    bottleneck_features = np.load('Classifier/bottleneck_features/DogResnet50Data.npz')
    train_ResNet50 = bottleneck_features['train']
    valid_ResNet50 = bottleneck_features['valid']
    test_ResNet50 = bottleneck_features['test']

    global ResNet_model
    ResNet_model = Sequential()
    ResNet_model.add(GlobalAveragePooling2D(input_shape=train_ResNet50.shape[1:]))
    ResNet_model.add(Dense(133, activation='softmax'))

    ResNet_model.summary()
    ResNet_model.compile(loss='categorical_crossentropy', optimizer=Adamax(learning_rate=0.002), metrics=['accuracy'])

    checkpointer = ModelCheckpoint(filepath='Classifier/saved_models/weights.best_adamax.ResNet50.hdf5',
                               verbose=0, save_best_only=True)

    epochs = 30
    batch_size = 64

    ResNet_model.fit(train_ResNet50, train_targets,
          validation_data=(valid_ResNet50, valid_targets),
          epochs=epochs, batch_size=batch_size, callbacks=[checkpointer], verbose=0)

    # get index of predicted dog breed for each image in test set
    ResNet50_predictions = [np.argmax(ResNet_model.predict(np.expand_dims(feature, axis=0))) for feature in test_ResNet50]

    # report test accuracy
    test_accuracy = 100*np.sum(np.array(ResNet50_predictions)==np.argmax(test_targets, axis=1))/len(ResNet50_predictions)
    print('Test accuracy: %.4f%%' % test_accuracy)
#     opt = Adamax(lr=0.0002)
#     epochs = 1
#     batch_size = 64

#     ResNet_model.fit(train_ResNet50, train_targets,
#           validation_data=(valid_ResNet50, valid_targets),
#           epochs=epochs, batch_size=batch_size, callbacks=[checkpointer], verbose=1)
    ### Load the model weights with the best validation loss.
    ResNet_model.load_weights('Classifier/saved_models/weights.best_adamax.ResNet50.hdf5')
    #return ResNet_model

#train_model()
#ResNet50_predict_breed('images/w.jpg')

