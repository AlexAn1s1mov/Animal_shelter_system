from sqlalchemy import Column, BigInteger, String, sql

from handlers.utils.db_api.db_TelegramBot import TimedBaseModel


class Status(TimedBaseModel):
    __tablename__ = 'status'
    id = Column(BigInteger, primary_key=True)
    status = Column(String(50))

    query: sql.select

