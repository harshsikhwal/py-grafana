from py_grafana import Grafana, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")

grafana.set_token_to_apis(bt)

folder = grafana.folder_api.get_folder_by_id(26)

print(folder.obj_to_dict())
