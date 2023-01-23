from py_grafana import Grafana, Folder, Token

# connect to grafana server
grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.folder_api.set_token(bt)

# create a folder f1
folder = Folder(title="f1", uid="uzumaki")
grafana.folder_api.create_folder(folder)
print(folder)

grafana.dashboard_api.set_token(bt)

# create a new dashboard under folder f1
grafana.dashboard_api.create_dashboard(folder, "new db")
db = grafana.folders["f1"].dashboards["new db"]
print(db)
