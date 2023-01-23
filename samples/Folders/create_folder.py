from py_grafana import Grafana, Folder, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")

grafana.set_token_to_apis(bt)

folder = Folder()
folder.title = "testfolder"
folder.uid = "testfolder"

folder = grafana.folder_api.create_folder(folder)

print(folder.obj_to_dict())
