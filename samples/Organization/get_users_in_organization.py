from py_grafana import Grafana, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.organization_api.set_token(bt)

organization = grafana.organization_api.get_current_organization()

grafana.organization_api.admin_api_pool.set_token(bt)
users = grafana.organization_api.admin_api_pool.get_users_in_organization(organization)

for user in users:
    print(user.obj_to_dict())
