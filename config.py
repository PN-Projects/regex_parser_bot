import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
DATABASE_URI = os.getenv('DATABASE_URI')

# Privileged users and god user
GOD_USER_ID = int(os.getenv('GOD_USER_ID'))  # God user ID
PRIVILEGED_USER_IDS = list(map(int, os.getenv('PRIVILEGED_USER_IDS', '').split(',')))  # List of privileged user IDs
