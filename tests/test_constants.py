import os
import pathlib

from pyplanter.constants import ENV_FILE_PATH, IFTTT_KEY
from pyplanter.helpers import ifttt_endpoint


def test_ifttt_endpoint():
    assert pathlib.Path(ENV_FILE_PATH).exists()
    output = ifttt_endpoint("some_action")
    assert "some_action" in output
    assert output.endswith(os.getenv(IFTTT_KEY))
