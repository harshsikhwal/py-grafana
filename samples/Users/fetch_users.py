from py_grafana import Grafana, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.user_api.set_token(bt)

users = grafana.user_api.fetch_users()

for user in users:
    print(user.obj_to_dict())
