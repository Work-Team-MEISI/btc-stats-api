from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

from dateutil.parser import parse

class Stats(BaseModel):
    id: int
    lower: float
    higher: float
    open: float
    close: float
    volume: float
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

