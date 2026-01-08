from loguru import logger

logger.add(
    "./log/app_{time:YYYY-MM-DD}.log",
    rotation="00:00",
    retention="100 days",
    # compression="gz",
    level="INFO"
)