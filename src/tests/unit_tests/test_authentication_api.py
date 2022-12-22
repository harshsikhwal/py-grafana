import pytest
from py_grafana import Token, APIKey

def delete_test_key(grafana):
    bt = Token.BasicToken("admin", "admin")
    grafana.authentication_api.set_token(bt)
    keys = grafana.authentication_api.get_api_keys()
    for key in keys:
        if key.name == "test key":
            grafana.authentication_api.delete_api_key(key)
            break


@pytest.mark.unittest
def test_get_api_keys(grafana):
    """
    This tests the get_api_keys api from authentication_api of py_grafana package
    """
    bt = Token.BasicToken("admin", "admin")
    grafana.authentication_api.set_token(bt)

    api_keys = grafana.authentication_api.get_api_keys()
    assert len(api_keys) > 0


@pytest.mark.unittest
def test_create_api_key(grafana):
    """
    This tests the create_api_key api from authentication_api of py_grafana package
    """
    delete_test_key(grafana)
    bt = Token.BasicToken("admin", "admin")
    grafana.authentication_api.set_token(bt)

    api_key = APIKey()
    api_key.name = "test key"
    api_key.role = "admin"

    key = grafana.authentication_api.create_api_key(api_key)
    assert key != ""

@pytest.mark.unittest
def test_delete_api_key(grafana):
    """
    This tests the create_api_key api from authentication_api of py_grafana package
    """
    delete_test_key(grafana)
    bt = Token.BasicToken("admin", "admin")
    grafana.authentication_api.set_token(bt)

    api_key = APIKey()
    api_key.name = "test key"
    api_key.role = "admin"

    # create key
    key = grafana.authentication_api.create_api_key(api_key)

    # delete the same
    grafana.authentication_api.delete_api_key(api_key)
    keys = grafana.authentication_api.get_api_keys()
    for key in keys:
        assert key.name != api_key.name


if __name__ == "__main__":
    pytest.main(
        [
            "--server",
            "localhost",
            "--port",
            "3000",
            "-s",
            "-o",
            "log_cli=1",
            "-o",
            "log_cli_level=INFO",

            __file__,
        ]
    )
