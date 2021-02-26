import sys

from loguru import logger
from appdirs import user_log_dir
from piplanter.constants import APP_NAME, APP_AUTHOR

logger.configure(
    handlers=[
        dict(
            sink=sys.stdout,
            format="<level>{level.icon} {level: <8}</level> <light-white>[{file.name}:{line}]</light-white> {message}",
        ),
        dict(
            sink=user_log_dir(APP_NAME, APP_AUTHOR),  # ~/Library/Logs/piplanter
            serialize=True,
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
