from py_grafana import Grafana, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.user_api.set_token(bt)

user = grafana.user_api.get_user_by_id(1)

print(user.obj_to_dict())