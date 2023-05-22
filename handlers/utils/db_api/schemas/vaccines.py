from sqlalchemy import Column, BigInteger, String, sql

from handlers.utils.db_api.db_TelegramBot import TimedBaseModel


class Vaccines(TimedBaseModel):
    __tablename__ = 'vaccines'
    id = Column(BigInteger, primary_key=True)
    name_vaccines = Column(String(50))
    self_period = Column(BigInteger)
    Vaccines_on_period = Column(String(5))

    query: sql.select