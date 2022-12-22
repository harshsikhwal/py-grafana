from py_grafana import Grafana, Organization, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")

organization = grafana.organization_api.get_current_organization()

print(organization.obj_to_dict())

organization.name = "New Org Name"

grafana.organization_api.update_current_organization(organization)

organization = grafana.organization_api.get_current_organization()

print(organization.obj_to_dict())
