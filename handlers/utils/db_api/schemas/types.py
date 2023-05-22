from sqlalchemy import Column, BigInteger, String, sql

from handlers.utils.db_api.db_TelegramBot import TimedBaseModel



class Types(TimedBaseModel):
    __tablename__ = 'types'
    id = Column(BigInteger, primary_key=True)
    type = Column(String(50))

    query: sql.select