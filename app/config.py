from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    # add more environment variables as needed

settings = Settings()

# coment the line bellow once is clear the database is connected
print("Loaded DATABASE_URL:", settings.DATABASE_URL)