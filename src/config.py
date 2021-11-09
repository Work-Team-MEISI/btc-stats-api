import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", default="dev")

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = os.getenv("API_KEY_NAME")
