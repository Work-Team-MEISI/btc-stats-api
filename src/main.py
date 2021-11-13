from fastapi.security.api_key import APIKey
from fastapi import Depends, FastAPI
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from src.database import get_db
from src import models
from src import schemas

from src.helpers import validate_api_key
from datetime import datetime

from dateutil.parser import parse


app = FastAPI(debug=True)

@app.get("/")
async def root(api_key: APIKey = Depends(validate_api_key)):
    return {"message": "Hello World"}

@app.post("/stats", status_code=201)
def create(
    stats: List[schemas.Stats],
    api_key: APIKey = Depends(validate_api_key),
    db: Session = Depends(get_db)
):
    stats = [models.Stats(**stat.dict()) for stat in stats]

    db.add_all(stats)
    db.commit()

    return {
        'success': True,
        'stat_ids': [stat.id for stat in stats]
    }
