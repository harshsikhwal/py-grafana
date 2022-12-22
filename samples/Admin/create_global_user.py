from py_grafana import Grafana, Token, User

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.admin_api.set_token(bt)

user = User()
user.name = "new user"
user.email = "new_user@user.com"
user.password = "Baloney1"

user = grafana.admin_api.create_global_user(user)

print(user.obj_to_dict())
