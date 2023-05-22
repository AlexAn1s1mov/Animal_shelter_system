from sqlalchemy import Column, BigInteger, String, DateTime, sql

from handlers.utils.db_api.db_TelegramBot import TimedBaseModel



class Animals(TimedBaseModel):
    __tablename__ = 'animals'
    id = Column(BigInteger, primary_key=True)
    kind = Column(String(50))
    name = Column(String(50))
    age = Column(BigInteger)
    date_of_enter = Column(DateTime)
    date_of_exit = Column(DateTime)
    status = Column(String(50))
    Enclosure_id = Column(BigInteger)
    query: sql.select