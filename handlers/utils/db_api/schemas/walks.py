from sqlalchemy import Column, BigInteger, String, DateTime, Time, sql

from handlers.utils.db_api.db_TelegramBot import TimedBaseModel


class Walks(TimedBaseModel):
    __tablename__ = 'walks'
    id = Column(BigInteger, primary_key=True)
    Date_of_walk = Column(DateTime)
    Time_start = Column(Time)
    Time_end = Column(Time)
    animal_id = Column(BigInteger)

    query: sql.select