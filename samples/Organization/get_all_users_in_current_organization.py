from py_grafana import Grafana

grafana = Grafana().connect("localhost", 3000)

users = grafana.organization_api.get_all_users_in_current_organization()

for user in users:
    print(user.obj_to_dict())
