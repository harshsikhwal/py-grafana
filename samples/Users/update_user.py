from py_grafana import Grafana, Token, User

grafana = Grafana().connect("localhost", 3000)

# set token
bt = Token.BasicToken("admin", "admin")
grafana.user_api.set_token(bt)
grafana.admin_api.set_token(bt)

# create a new user
user = User()
user.name = "test user"
user.email = "test_user@user.com"
user.password = "Baloney1"

user = grafana.admin_api.create_global_user(user)

# print the new user
print(user.obj_to_dict())

# update a user setting

user.name = "new user"

# call the update api
grafana.user_api.update_user(user)

# print the updated user

user = grafana.user_api.get_user_by_email("test_user@user.com")
print(user.obj_to_dict())

# clean the grafana system
grafana.admin_api.delete_user(user)