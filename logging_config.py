from loguru import logger

logger.add("logs/api.log", rotation="1 day", level="INFO")