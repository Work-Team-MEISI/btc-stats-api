from datetime import datetime
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException
from dateutil import parser, rrule
from datetime import timedelta, datetime

from starlette.status import HTTP_403_FORBIDDEN

from src.config import API_KEY, API_KEY_NAME

buckets = ['day', 'week', 'month', 'year']

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def validate_api_key(
    api_key_header: str = Security(api_key_header)
):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Access Token is invalid"
        )

def get_time_category(category):
    return {
        'week': rrule.WEEKLY,
        'month': rrule.MONTHLY,
        'year': rrule.YEARLY
    }[category]

def get_date_intervals(bucket, date_from):
    rule = get_time_category(bucket)

    date_interval = [
        date for date in rrule.rrule(rule, dtstart=date_from, until=datetime.now())
    ]

    return date_interval

def get_date_intervals_list(dates):
    dates_intervals = []

    
    
    for index, date in enumerate(dates):
        intervals = []

        if (index + 1 < len(dates) and index >= 0):
            next_date = dates[index + 1]

            intervals.append(date)

            if index + 2 != len(dates):
                intervals.append(next_date)
            else:
                intervals.append(next_date)

            if intervals:
                dates_intervals.append(intervals)

    return dates_intervals

def get_stats_by_date_interval(stats, bucket):
    return