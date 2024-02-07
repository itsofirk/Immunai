import logging
from .config import Settings


settings = Settings()
logger = logging.getLogger()

console_handler = logging.StreamHandler()
fmt = logging.Formatter("[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")
console_handler.setFormatter(fmt)

logger.setLevel(settings.logging_level)
logger.addHandler(console_handler)
