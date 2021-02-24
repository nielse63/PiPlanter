import sys

from loguru import logger

logger.configure(
    handlers=[
        dict(
            sink=sys.stdout,
            format="<level>{level.icon} {level: <8}</level> <light-white>[{file.name}:{line}]</light-white> {message}",
        ),
        dict(
            sink="logs/pyplanter.log",
            serialize=True,
            # format="{message}",
            rotation="10 MB",
        ),
    ],
    levels=[
        dict(name="DEBUG", icon="●"),
        dict(name="INFO", icon="ℹ"),
        dict(name="SUCCESS", icon="✔"),
        dict(name="WARNING", icon="‼"),
        dict(name="ERROR", icon="✖"),
        dict(name="CRITICAL", icon="ⓧ"),
    ],
)
