from fastapi.exceptions import HTTPException
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

import datetime

from src.helpers import (
    validate_api_key,
    get_stats_by_date_interval,
    get_date_intervals,
    buckets,
    get_date_intervals_list
)
    


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
    date_order: Optional[str] = None,
    bucket: Optional[str] = None
):
    if date_order not in ['desc', 'asc']:
        raise HTTPException(
            status_code=400,
            detail="Make sure 'date_order' query param is 'desc' or 'asc'."
        )
    
    if bucket not in buckets:
        raise HTTPException(
            status_code=400,
            detail="Make sure 'bucket' query param is 'day', 'week', 'month', or 'year'."
        )
        
    stats = db.query(models.Stats)

    if date_order:
        stats = stats.order_by(eval(date_order + "(models.Stats.timestamp)"))
    
    if bucket and bucket != 'day':
        first_read = (stats.all())[0].timestamp

        date_intervals = get_date_intervals(bucket, first_read)
        date_intervals_list = get_date_intervals_list(date_intervals)

        date_intervals_list.append([date_intervals_list[-1][-1], datetime.datetime.now()])

        if limit:
            date_intervals_list = date_intervals_list[-limit:]

        avg_stats = []

        for i, date_list in enumerate(date_intervals_list): 
            stats_by_date_iterval = stats.filter(
                    models.Stats.timestamp >= date_list[0]
                ).filter(
                    models.Stats.timestamp <= date_list[1]
                ).all()

            avg_close = sum([stat_by_date.close for stat_by_date in stats_by_date_iterval])/len(stats_by_date_iterval)
            min_lower = min([stat_by_date.lower for stat_by_date in stats_by_date_iterval])
            max_higher = max([stat_by_date.higher for stat_by_date in stats_by_date_iterval])

            avg_stat = {}

            avg_stat['id'] = i + 1

            avg_stat['avg_close'] = avg_close
            avg_stat['lower'] = min_lower
            avg_stat['higher'] = max_higher
            avg_stat['timestamp'] = date_list[0]

            avg_stats.append(schemas.retrieve_stats(**avg_stat))

        return paginate(avg_stats)

    return paginate(stats.all())


add_pagination(app)