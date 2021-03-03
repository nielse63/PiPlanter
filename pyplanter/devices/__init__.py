import requests

from pyplanter.helpers import ifttt_endpoint
from pyplanter.logger import logger


def iftt_webhook_action(action: str) -> None:
    url = ifttt_endpoint(action)
    try:
        response = requests.post(url)
        if response.status_code > 399:
            raise RuntimeWarning(
                f"ifttt action {action} failed: {response.json()}"
            )
    except Exception as error:
        logger.error(error)
        raise error
