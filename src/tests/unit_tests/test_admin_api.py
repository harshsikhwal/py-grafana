import pytest
from py_grafana import User, Token


def delete_test_user(grafana):
    # get all users
    bt = Token.BasicToken("admin", "admin")
    grafana.user_api.set_token(bt)
    grafana.admin_api.set_token(bt)
    users = grafana.user_api.fetch_users()
    for user in users:
        if user.email == "test_user@user.com":
            grafana.admin_api.delete_user(user)


@pytest.mark.unittest
def test_create_global_user(grafana):
    """
    This tests the create_global_user api from admin_api of py_grafana package
    """
    delete_test_user(grafana)
    bt = Token.BasicToken("admin", "admin")
    grafana.admin_api.set_token(bt)
    user = User()
    user.name = "test user"
    user.email = "test_user@user.com"
    user.password = "Baloney1"
    user = grafana.admin_api.create_global_user(user)
    assert user.id is not None


@pytest.mark.unittest
def test_fetch_settings(grafana):
    """
    This tests the fetch_settings api from admin_api of py_grafana package
    """
    delete_test_user(grafana)
    bt = Token.BasicToken("admin", "admin")
    grafana.admin_api.set_token(bt)
    settings = grafana.admin_api.fetch_settings()
    assert settings is not None


@pytest.mark.unittest
def test_update_settings(grafana):
    """
    This tests the update_settings api from admin_api of py_grafana package
    """
    bt = Token.BasicToken("admin", "admin")
    grafana.admin_api.set_token(bt)

    settings = {
        "updates":
            {
                "auth.saml":
                    {
                        "enabled": "true"
                    }
            }
    }

    grafana.admin_api.update_settings(settings)

    settings = grafana.admin_api.fetch_settings()

    assert settings["auth.saml"]["enabled"] == "true"


@pytest.mark.unittest
def test_delete_user(grafana):
    """
    This tests the delete_user api from admin_api of py_grafana package
    """
    delete_test_user(grafana)
    bt = Token.BasicToken("admin", "admin")
    grafana.admin_api.set_token(bt)

    user = User()
    user.name = "test user"
    user.email = "test_user@user.com"
    user.password = "Baloney1"

    # create user
    user = grafana.admin_api.create_global_user(user)

    # delete the user
    grafana.admin_api.delete_user(user)

    # get all users
    grafana.user_api.set_token(bt)
    users = grafana.user_api.fetch_users()

    for u in users:
        assert u.email != user.email


@pytest.mark.unittest
def test_fetch_grafana_usage_report_preview(grafana):
    """
    This tests the fetch_grafana_usage_report_preview api from admin_api of py_grafana package
    """
    bt = Token.BasicToken("admin", "admin")
    grafana.admin_api.set_token(bt)

    stats = grafana.admin_api.fetch_grafana_usage_report_preview()
    assert len(stats) > 0


@pytest.mark.unittest
def test_fetch_grafana_stats(grafana):
    """
    This tests the fetch_grafana_stats api from admin_api of py_grafana package
    """
    bt = Token.BasicToken("admin", "admin")
    grafana.admin_api.set_token(bt)

    stats = grafana.admin_api.fetch_grafana_stats()

    assert len(stats) > 0


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
