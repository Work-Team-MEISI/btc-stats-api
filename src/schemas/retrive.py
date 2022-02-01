from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

from dateutil.parser import parse

class Stats(BaseModel):
    id: int
    lower: float
    higher: float
    open: Optional[float] = None
    close: Optional[float] = None
    volume: Optional[float] = None
    avg_close: Optional[float] = None
    change: Optional[float] = None
    timestamp: datetime

    class Config:
        orm_mode = True

class AvgStats(BaseModel):
    id: int
    lower: float
    higher: float
    open: float
    close: float
    avg_volume: float
    change: Optional[float] = None
    timestamp: datetime

    class Config:
        orm_mode = True

class SVMRStats(BaseModel):
    id: int
    value: float
    accuracy: float
    date: datetime

    class Config:
        orm_mode = True
