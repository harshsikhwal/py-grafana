from py_grafana import Grafana, Folder, Authentication, Admin, BasicToken

grafana = Grafana().connect("localhost", 3000)


# folder = Folder(title="nf2", uid="nf2")

# folder = grafana.folders_api.create_folder(folder)

# folder = grafana.folders_api().create_folder_by_name("new folder")


# grafana.Folder[folder.title] = folder
#
# # user = grafana.users_api().get_user_by_username("vb")
# auth = Authentication("vb", "Admin")
# grafana.authentication_api.create_api_key(auth)
# print(auth.token.get_token_str())

# bt = BasicToken("admin", "admin")
#
# test = grafana.admin_api.set_token(bt)
#
#
# test.set_s("harsh")
#
# settings = {
#   "updates": {
#     "users": {
#       "default_theme": "light"
#     }
#   }
# }
#
# print(test.s)
#
#
# # grafana.admin_api.update_settings(settings)
# test.update_settings(settings)
