import logging
import os
from datetime import datetime

LOG_DIRS = "logs"
os.makedirs(LOG_DIRS,exist_ok=True)

FILE_PATH = os.path.join(LOG_DIRS+f"/log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=FILE_PATH,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def get_log(name):
    log = logging.getLogger(name=name)
    log.setLevel(logging.INFO)
    return log