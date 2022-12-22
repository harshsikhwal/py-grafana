from py_grafana import Grafana, Token, User

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.organization_api.set_token(bt)

organizations = grafana.organization_api.admin_api_pool.fetch_all_organizations()

for organization in organizations:
    print(organization.obj_to_dict())