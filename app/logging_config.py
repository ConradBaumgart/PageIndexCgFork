import logging
import sys
from pathlib import Path

LOG_PATH = Path("logs/app.log")

# 1) Make sure the directory exists
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

# Configure root logger
logging.basicConfig(
    level=logging.INFO,  # INFO or DEBUG for more details
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),  # logs to console
        logging.FileHandler(LOG_PATH, encoding="utf-8"),  # logs to file
    ],
)


# Optional: create a function to get a logger for each module
def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
