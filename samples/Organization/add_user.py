from py_grafana import Grafana, BasicToken, User

grafana = Grafana().connect("localhost", 3000)

user = User()
user.name = "new user 1"
user.email = "newuser@xyz.com"


status = grafana.organization_api.add_user(user)
print(status)

