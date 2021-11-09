from fastapi.security.api_key import APIKey
from fastapi import Depends, FastAPI

from src.helpers import validate_api_key

app = FastAPI()

@app.get("/")
async def root(api_key: APIKey = Depends(validate_api_key)):
    return {"message": "Hello World"}