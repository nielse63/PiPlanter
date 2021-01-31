from pytemplate.howdy import Howdy

TEST_MESSAGE = "howdy"
TEST_NAME = "Erik"


def test_attributes():
    instance = Howdy(TEST_MESSAGE)
    assert instance.message == TEST_MESSAGE


def test_hello():
    instance = Howdy(TEST_MESSAGE)
    message = instance.hello(TEST_NAME)
    assert TEST_MESSAGE in message
    assert TEST_NAME in message
