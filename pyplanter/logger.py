import sys

from loguru import logger

logger.configure(
    handlers=[
        dict(
            sink=sys.stdout,
            format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <4}</level> | <level>{message}</level>",
        ),
        dict(
            sink="logs/pyplanter.log",
            serialize=True,
            format="{message}",
            rotation="100 MB",
        ),
    ]
)
