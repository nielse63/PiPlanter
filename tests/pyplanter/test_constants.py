import pathlib
import os
from pyplanter.constants import IFTTT_KEY, ENV_FILE_PATH
from pyplanter.helpers import ifttt_endpoint


def test_ifttt_endpoint():
    assert pathlib.Path(ENV_FILE_PATH).exists()
    output = ifttt_endpoint("some_action")
    assert "some_action" in output
    assert output.endswith(os.getenv(IFTTT_KEY))
