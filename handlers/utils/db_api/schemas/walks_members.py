from sqlalchemy import Column, BigInteger, String, DateTime, Time, sql

from handlers.utils.db_api.db_TelegramBot import TimedBaseModel


class Walks_members(TimedBaseModel):
    __tablename__ = 'walks_members'
    walk_id = Column(BigInteger, primary_key=True)
    worker_id = Column(BigInteger)
    volonture_id = Column(BigInteger)

    query: sql.select