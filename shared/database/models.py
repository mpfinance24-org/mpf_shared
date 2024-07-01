from datetime import datetime
from typing import List

from sqlalchemy import Boolean, ForeignKey, Enum, Text, LargeBinary, \
    BigInteger, Table
from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from shared.database import Base


class SalesReports(Base):
    __tablename__ = 'sales_reports'
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )
    subject_name: Mapped[str] = mapped_column(String, nullable=False)
    date_from: Mapped[datetime]  # Дата начала отчётного периода
    date_to: Mapped[datetime]  # Дата конца отчётного периода
    create_dt: Mapped[datetime]  # Дата формирования отчёта
    currency_name: Mapped[str]  # Валюта отчёта
    rrd_id: Mapped[int]  # номер строки
    subject_name: Mapped[str]  # Предмет
    nm_id: Mapped[int]  # Артикул WB
    ts_name: Mapped[str]  # Размер
    shk_id: Mapped[int]  # Штрихкод
    # Уникальный идентификатор заказа.srid равен rid в ответах методов сборочных заданий.
    srid: Mapped[str] = mapped_column(String, unique=True)

    # created_date: Mapped[datetime.datetime] = mapped_column(
    #     DateTime(timezone=True), server_default=func.now()
    # )

class Clients(Base):
    __tablename__ = 'clients'
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )
    name: Mapped[str]
    surname: Mapped[str]
    wb_apikey: Mapped[str] = mapped_column(String, nullable=False)
