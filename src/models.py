from sqlalchemy import Integer, String, Float, DateTime
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import Column
from src.database import Base


class Stats(Base):
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True)
    lower = Column(Float, nullable=False)
    higher = Column(Float, nullable=False)
    open = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)
    change = Column(Float, nullable=True)
    timestamp = Column(DateTime, nullable=False)

class WeeklyStats(Base):
    __tablename__ = 'weekly_stats'

    id = Column(Integer, primary_key=True)
    lower = Column(Float, nullable=False)
    higher = Column(Float, nullable=False)
    open = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    avg_volume = Column(Float, nullable=False)
    change = Column(Float, nullable=True)
    timestamp = Column(DateTime, nullable=False)

class MonthlyStats(Base):
    __tablename__ = 'monthly_stats'

    id = Column(Integer, primary_key=True)
    lower = Column(Float, nullable=False)
    higher = Column(Float, nullable=False)
    open = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    avg_volume = Column(Float, nullable=False)
    change = Column(Float, nullable=True)
    timestamp = Column(DateTime, nullable=False)

class AnualStats(Base):
    __tablename__ = 'anual_stats'

    id = Column(Integer, primary_key=True)
    lower = Column(Float, nullable=False)
    higher = Column(Float, nullable=False)
    open = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    avg_volume = Column(Float, nullable=False)
    change = Column(Float, nullable=True)
    timestamp = Column(DateTime, nullable=False)

class SVMRStats(Base):
    __tablename__ = 'svmr_stats'

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    accuracy = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)


