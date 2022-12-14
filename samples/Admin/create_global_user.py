from py_grafana import Grafana, BasicToken, User

grafana = Grafana().connect("localhost", 3000)

bt = BasicToken("admin", "admin")

grafana.admin_api.set_token(bt)

user = User()
user.name = "yash sikhwal"
user.email = "yashsikhwal2000@graf.com"
user.password = "Baloney1"

user = grafana.admin_api.create_global_user(user)

print(user.obj_to_dict())
