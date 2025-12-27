import logging
from fastapi import HTTPException, status
from typing import Optional
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class AppException(HTTPException):
    def __init__(self, status_code: int, detail: str, error_code: Optional[str] = None):
        super().__init__(status_code=status_code, detail=detail)
        self.error_code = error_code
        logger.error(f"AppException: {error_code} - {detail}")

def log_info(message: str):
    logger.info(message)

def log_error(message: str, error: Optional[Exception] = None):
    if error:
        logger.error(f"{message} - Error: {str(error)}")
    else:
        logger.error(message)

def log_debug(message: str):
    logger.debug(message)

def log_warning(message: str):
    logger.warning(message)