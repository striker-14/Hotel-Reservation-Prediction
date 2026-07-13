# Used to permanently record events, errors, data changes, and operational status during a program's execution instead of losing that data when the console closes
import logging
import os # used for creating directories
from datetime import datetime # we need date and time of each log

LOGS_DIR = "logs" # creating logs directory
os.makedirs(LOGS_DIR,exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger