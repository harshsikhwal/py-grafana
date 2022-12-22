from py_grafana import Grafana, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.organization_api.set_token(bt)

organization = grafana.organization_api.admin_api_pool.get_organization_by_id(1)

print(organization.obj_to_dict())
