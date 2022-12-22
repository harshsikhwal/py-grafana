from py_grafana import Grafana

grafana = Grafana().connect("localhost", 3000)


organization = grafana.organization_api.get_current_organization()

print(organization.obj_to_dict())
