import pytest
from py_grafana import User, Token


@pytest.mark.unittest
def test_fetch_users(grafana):
    """
    This tests the fetch_users api from user_api of py_grafana package
    """
    bt = Token.BasicToken("admin", "admin")
    grafana.user_api.set_token(bt)

    users = grafana.user_api.fetch_users()

    assert len(users) > 0


@pytest.mark.unittest
def test_get_user_by_email(grafana):
    """
    This tests the get_user_by_email api from user_api of py_grafana package
    """
    bt = Token.BasicToken("admin", "admin")
    grafana.user_api.set_token(bt)

    user = grafana.user_api.get_user_by_email("admin@localhost")
    assert user is not None


@pytest.mark.unittest
def test_get_user_by_id(grafana):
    """
    This tests the get_user_by_id api from user_api of py_grafana package
    """
    bt = Token.BasicToken("admin", "admin")
    grafana.user_api.set_token(bt)

    user = grafana.user_api.get_user_by_id(1)

    assert user is not None


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