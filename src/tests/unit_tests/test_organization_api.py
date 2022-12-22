import pytest
from py_grafana import User, Token, Organization
import time


@pytest.mark.unittest
def test_get_current_organization(grafana):
    """
    This tests the get_current_organization api from organization_api of py_grafana package
    """
    bt = Token.BasicToken("admin", "admin")
    grafana.organization_api.set_token(bt)
    organization = grafana.organization_api.get_current_organization()
    assert organization is not None


@pytest.mark.unittest
def test_get_all_users_in_current_organization(grafana):
    """
    This tests the get_all_users_in_current_organization api from organization_api of py_grafana package
    """
    bt = Token.BasicToken("admin", "admin")
    grafana.organization_api.set_token(bt)
    users = grafana.organization_api.get_all_users_in_current_organization()
    assert len(users) > 0


@pytest.mark.unittest
def test_create_organization(grafana):
    """
    This tests the create_organization api from organization_api of py_grafana package
    """
    organization = Organization()
    organization.name = "test corporate"

    bt = Token.BasicToken("admin", "admin")
    grafana.organization_api.admin_api_pool.set_token(bt)

    org = grafana.organization_api.admin_api_pool.create_organization(organization)

    assert org is not None

    # general cleanup
    grafana.organization_api.admin_api_pool.delete_organization(organization)


@pytest.mark.unittest
def test_delete_organization_by_id(grafana):
    """
    This tests the delete_organization_by_id api from organization_api of py_grafana package
    """
    organization = Organization()
    organization.name = "test corporate"

    bt = Token.BasicToken("admin", "admin")
    grafana.organization_api.admin_api_pool.set_token(bt)

    # create organization
    org = grafana.organization_api.admin_api_pool.create_organization(organization)
    # delete organization
    grafana.organization_api.admin_api_pool.delete_organization(organization)

    organizations = grafana.organization_api.admin_api_pool.fetch_all_organizations()

    for organization in organizations:
        assert organization.name != "test corporate"


@pytest.mark.unittest
def test_fetch_all_organizations(grafana):
    bt = Token.BasicToken("admin", "admin")
    grafana.organization_api.set_token(bt)

    organizations = grafana.organization_api.admin_api_pool.fetch_all_organizations()

    assert len(organizations) > 0



@pytest.mark.unittest
def test_get_organization_by_id(grafana):
    bt = Token.BasicToken("admin", "admin")
    grafana.organization_api.set_token(bt)

    organization = grafana.organization_api.admin_api_pool.get_organization_by_id(1)

    assert organization is not None


@pytest.mark.unittest
def test_get_users_in_organization(grafana):
    bt = Token.BasicToken("admin", "admin")
    grafana.organization_api.admin_api_pool.set_token(bt)
    grafana.organization_api.set_token(bt)
    # get current organization
    organization = grafana.organization_api.get_current_organization()
    # get users of current organization
    users = grafana.organization_api.admin_api_pool.get_users_in_organization(organization)

    assert len(users) > 0


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
