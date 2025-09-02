import logging
import os
import time
from config.settings import settings

if settings.enable_logging:
    LOG_FILE = os.path.join(os.path.dirname(__file__), "../datafiles/output/app.log")
    ERROR_LOG_FILE = os.path.join(os.path.dirname(__file__), "../datafiles/output/error.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.FileHandler(ERROR_LOG_FILE),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger("logger")

    def remove_old_logs(log_directory):
        current_time = time.time()
        for filename in os.listdir(log_directory):
            file_path = os.path.join(log_directory, filename)
            if os.path.isfile(file_path):
                file_creation_time = os.path.getctime(file_path)
                if (current_time - file_creation_time) // (24 * 3600) >= 7:
                    os.remove(file_path)

    remove_old_logs(os.path.join(os.path.dirname(__file__), "../datafiles/output"))
else:
    logger = logging.getLogger("null")
    logger.addHandler(logging.NullHandler())