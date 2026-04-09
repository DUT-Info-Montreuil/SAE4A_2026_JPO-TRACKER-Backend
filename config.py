import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/visiteurs")
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")
    ADMIN_PASSWORD_HASH = os.getenv("ADMIN_PASSWORD_HASH", "")