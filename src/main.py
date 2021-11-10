from fastapi.security.api_key import APIKey
from fastapi import Depends, FastAPI

from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Stats
from src.schemas import CreateStats

from src.helpers import validate_api_key
from datetime import datetime

from dateutil.parser import parse


app = FastAPI()

@app.get("/")
async def root(api_key: APIKey = Depends(validate_api_key)):
    return {"message": "Hello World"}

@app.post("/stats", status_code=201)
def create(
    details: CreateStats,
    api_key: APIKey = Depends(validate_api_key),
    db: Session = Depends(get_db),
):

    stat = Stats(
        lower=details.lower,
        higher=details.higher,
        open=details.open,
        close=details.close,
        volume=details.volume,
        change=details.change,
        timestamp=details.timestamp
    ) 
    
    db.add(stat)
    db.commit()

    return {
        'success': True,
        "created_id": stat.id
    }
