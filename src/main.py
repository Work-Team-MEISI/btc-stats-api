from fastapi.security.api_key import APIKey
from fastapi import Depends, FastAPI
from typing import List, Optional

from sqlalchemy import desc, asc
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode

from src.database import get_db
from src import models, schemas
from src.schemas.retrive import Stats as get_stats_schema
from fastapi_pagination import Page, add_pagination, paginate

from src.helpers import validate_api_key

app = FastAPI(debug=True)

@app.get("/")
async def root(api_key: APIKey = Depends(validate_api_key)):
    return {"message": "Hello World"}

@app.post("/stats", status_code=201)
def create_stats(
    stats: List[schemas.create_stats],
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

@app.get("/stats", response_model=Page[schemas.retrieve_stats])
def get_stats(
    db: Session = Depends(get_db),
    limit: Optional[int] = None,
    date_order: Optional[str] = None
):
    stats = None

    if limit and date_order:
        stats = db.query(models.Stats).order_by(eval(date_order+"(models.Stats.timestamp)")).limit(limit).all()
    else:
        stats = db.query(models.Stats).all()

    return paginate(stats)

@app.post("/week-stats", status_code=201)
def create_weekly_stats(
    stats: List[schemas.create_avg_stats],
    api_key: APIKey = Depends(validate_api_key),
    db: Session = Depends(get_db)
):
    stats = [models.WeeklyStats(**stat.dict()) for stat in stats]

    db.add_all(stats)
    db.commit()

    return {
        'success': True,
        'stat_ids': [stat.id for stat in stats]
    }

@app.get("/week-stats", response_model=Page[schemas.retrieve_avg_stats])
def get_stats(
    db: Session = Depends(get_db),
    limit: Optional[int] = None,
    date_order: Optional[str] = None
):
    stats = None

    if limit and date_order:
        stats = db.query(models.WeeklyStats).order_by(eval(date_order+"(models.WeeklyStats.timestamp)")).limit(limit).all()
    else:
        stats = db.query(models.WeeklyStats).all()

    return paginate(stats)

@app.post("/month-stats", status_code=201)
def create_weekly_stats(
    stats: List[schemas.create_avg_stats],
    api_key: APIKey = Depends(validate_api_key),
    db: Session = Depends(get_db)
):
    stats = [models.MonthlyStats(**stat.dict()) for stat in stats]

    db.add_all(stats)
    db.commit()

    return {
        'success': True,
        'stat_ids': [stat.id for stat in stats]
    }

@app.get("/month-stats", response_model=Page[schemas.retrieve_avg_stats])
def get_stats(
    db: Session = Depends(get_db),
    limit: Optional[int] = None,
    date_order: Optional[str] = None
):
    stats = None

    if limit and date_order:
        stats = db.query(models.MonthlyStats).order_by(eval(date_order+"(models.MonthlyStats.timestamp)")).limit(limit).all()
    else:
        stats = db.query(models.MonthlyStats).all()

    return paginate(stats)

@app.post("/anual-stats", status_code=201)
def create_weekly_stats(
    stats: List[schemas.create_avg_stats],
    api_key: APIKey = Depends(validate_api_key),
    db: Session = Depends(get_db)
):
    stats = [models.AnualStats(**stat.dict()) for stat in stats]

    db.add_all(stats)
    db.commit()

    return {
        'success': True,
        'stat_ids': [stat.id for stat in stats]
    }

@app.get("/anual-stats", response_model=Page[schemas.retrieve_avg_stats])
def get_stats(
    db: Session = Depends(get_db),
    limit: Optional[int] = None,
    date_order: Optional[str] = None
):
    stats = None

    if limit and date_order:
        stats = db.query(models.AnualStats).order_by(eval(date_order+"(models.AnualStats.timestamp)")).limit(limit).all()
    else:
        stats = db.query(models.AnualStats).all()

    return paginate(stats)

add_pagination(app)