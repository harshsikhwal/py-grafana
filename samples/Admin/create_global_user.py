from py_grafana import Grafana, BasicToken, User

grafana = Grafana().connect("localhost", 3000)

bt = BasicToken("admin", "admin")

grafana.admin_api.set_token(bt)

user = User()
user.name = "new user"
user.email = "user.e@graf.com"
user.password = "password"

user = grafana.admin_api.create_global_user(user)

print(user.obj_to_dict())
