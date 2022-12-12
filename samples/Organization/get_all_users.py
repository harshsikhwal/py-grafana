from py_grafana import Grafana, BasicToken

grafana = Grafana().connect("localhost", 3000)

users = grafana.organization_api.get_all_users()

for user in users:
    print(user.obj_to_dict())
