import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

if not SECRET_KEY:
    raise ValueError("Missing SECRET_KEY in .env file!")

ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
