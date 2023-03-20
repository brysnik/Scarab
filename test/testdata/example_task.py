
import os
from venv import logger


def main():
    logger.info("Starting example task")
    logger.info("Printing environment variables")
    for k, v in os.environ.items():
        logger.info(f"{k}={v}")
    logger.info("Done")
    logger.info("Closing example task")
    return 0
