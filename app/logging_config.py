import logging
import sys

# Configure root logger
logging.basicConfig(
    level=logging.INFO,  # INFO or DEBUG for more details
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),  # logs to console
        logging.FileHandler("logs/app.log", encoding="utf-8")  # logs to file
    ]
)

# Optional: create a function to get a logger for each module
def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
