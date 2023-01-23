from py_grafana import Grafana, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")

grafana.set_token_to_apis(bt)

folders = grafana.folder_api.get_all_folders()

for folder in folders:
    print(folder.obj_to_dict())
