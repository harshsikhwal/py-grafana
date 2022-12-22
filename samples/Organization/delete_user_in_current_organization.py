from py_grafana import Grafana, Token, User

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.admin_api.set_token(bt)

user = User()
user.name = "test user"
user.email = "test_user@user.com"
user.password = "Baloney1"

# create user
grafana.organization_api.add_user_in_current_organization(user)

# delete the user
grafana.organization_api.delete_user_in_current_organization(user)
