import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", default="dev")

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = os.getenv("API_KEY_NAME")

if ENV == 'PROD':
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL").replace('postgres', 'postgresql')
elif ENV == 'DOCKER':
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL").replace('@localhost', '@btc-db')
    print(SQLALCHEMY_DATABASE_URL)
else:
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

