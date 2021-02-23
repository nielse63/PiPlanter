import sys

from loguru import logger

config = {
    "handlers": [
        dict(
            sink=sys.stdout,
            format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        ),
        dict(
            sink="logs/pyplanter.log",
            serialize=True,
            format="{message}",
            rotation="100 MB",
        ),
    ]
}
logger.configure(handlers=config["handlers"])
