from py_grafana import Grafana, Token, User

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")

grafana.admin_api.set_token(bt)

user = User()
user.name = "new user"
user.email = "user.e@graf.com"
user.password = "password"

user = grafana.admin_api.create_global_user(user)

print(user.obj_to_dict())

user.password = "new_password"

grafana.admin_api.change_user_password(user)