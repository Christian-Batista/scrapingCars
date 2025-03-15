from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "port": os.getenv("DB_PORT"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

IMAGES_PATH = os.getenv("IMAGES_PATH")
