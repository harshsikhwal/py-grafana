from py_grafana import Grafana, Folder, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")

grafana.set_token_to_apis(bt)

folder = grafana.folder_api.get_folder_by_uid("testfolder")

print(folder.obj_to_dict())

folder.title = "new folder"

folder = grafana.folder_api.update_folder(folder)

print(folder.obj_to_dict())
