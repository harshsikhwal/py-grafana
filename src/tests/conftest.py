import pytest
import os
from py_grafana import Grafana

pytest.CMD_LINE_OPTIONS = {
    "server": {
        "default": "localhost",
        "help": "The location of the grafana API endpoint.",
    },
    "port": {
        "default": "3000",
        "help": "The the port at that the grafana server is running",
    }
}
pytest.BASEDIR = os.path.abspath(os.path.dirname(__file__))
pytest.SERVER = None
pytest.PORT = None


def pytest_addoption(parser):
    """Add command line options to the pytest config object.
    This is a good starting place for parameterizing variables.
    Command line option values can come from the command line and if they do
    not exist a default can be provided.
    Any external configuration files can also be processed here.
    All option values are a string that when eval() MUST return an iterable.
    """
    for name, value in pytest.CMD_LINE_OPTIONS.items():
        parser.addoption(
            f"--{name}",
            action="store",
            type=str,
            default=value["default"],
            help=value["help"],
        )


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "unittest: Run tests to check sanity of the code",
    )
    pytest.generate_code = "unittest" in config.invocation_params.args
    for name, value in pytest.CMD_LINE_OPTIONS.items():
        if f"--{name}" in config.invocation_params.args:
            value = config.getoption(f"--{name}")
        else:
            value = value["default"]
        setattr(pytest, name.upper().replace("-", "_"), value)

    print_cmd_options()


def print_cmd_options():
    print("#" * 80)
    print("Test will run with these options")
    print("\tSERVER: ", pytest.SERVER)
    print("\tPORT: ", pytest.PORT)
    print("#" * 80)


@pytest.fixture()
def grafana():
    return Grafana().connect(pytest.SERVER, int(pytest.PORT))

