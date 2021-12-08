from pydantic import BaseModel, validator
from typing import Optional

from dateutil.parser import parse

class Stats(BaseModel):
    lower: float
    higher: float
    open: Optional[float] = None
    close: Optional[float] = None
    avg_close: Optional[float] = None
    volume: float
    change: Optional[float] = None
    timestamp: str

    @validator('timestamp')
    def validate_date(cls, v):
        try:
            parse(v)
        except:
            raise ValueError('Date must be valid')
            
        return v

    class Config:
        orm_mode = True

class AvgStats(BaseModel):
    lower: float
    higher: float
    open: float
    close: float
    avg_volume: float
    change: Optional[float] = None
    timestamp: str

    @validator('timestamp')
    def validate_date(cls, v):
        try:
            parse(v)
        except:
            raise ValueError('Date must be valid')
            
        return v