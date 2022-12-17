from py_grafana import Grafana, Folder

# connect to grafana server
grafana = Grafana().connect("localhost", 3000)

# create a folder f1
folder = Folder(title="f1", uid="uzumaki")
grafana.folders_api.create_folder(folder)
print(folder)

# create a new dashboard under folder f1
grafana.dashboard_api.create_dashboard(folder, "new db")
db = grafana.folders["f1"].dashboards["new db"]
print(db)
