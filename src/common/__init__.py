import logging
from .config import Settings


settings = Settings()
logger = logging.getLogger()

fmt = logging.Formatter("[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(fmt)

logger.addHandler(console_handler)
