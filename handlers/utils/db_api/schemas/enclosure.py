from sqlalchemy import Column, BigInteger, String, sql

from handlers.utils.db_api.db_TelegramBot import TimedBaseModel


class Enclosure(TimedBaseModel):
    __tablename__ = 'enclosure'
    enclosure_number = Column(BigInteger, primary_key=True)
    size = Column(String(50))
    type_id = Column(BigInteger)

    query: sql.select
