import logging
import os
import sys
from datetime import datetime
from src.exception import CustomException
# Create a unique log file name using the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the path for the logs folder
logs_path = os.path.join(os.getcwd(), "logs")

# Create the logs folder if it doesn't already exist
os.makedirs(logs_path, exist_ok=True)

# Create the complete path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,   # Log file location
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO         # Log INFO and above
)

# Example log message
logging.info("Logging has started.")

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by 0")
        print(CustomException(e, sys))
