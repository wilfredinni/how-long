from how_long import __version__
from how_long import timer


def test_version():
    assert __version__ == "0.1.0"


def test_wrap():
    @timer
    def wrapped_function():
        return

    assert wrapped_function.__name__ == "wrapped_function"
