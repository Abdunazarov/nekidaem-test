# stdlib
import os

# thirdparty
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]
BROKER_URI = os.environ["BROKER_URI"]
