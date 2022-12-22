from py_grafana import Grafana, Organization, Token

grafana = Grafana().connect("localhost", 3000)

organization = Organization()
organization.name = "test corporate"

bt = Token.BasicToken("admin", "admin")
grafana.organization_api.admin_api_pool.set_token(bt)

org = grafana.organization_api.admin_api_pool.create_organization(organization)

print(org.obj_to_dict())

# general cleanup
grafana.organization_api.admin_api_pool.delete_organization(organization)



