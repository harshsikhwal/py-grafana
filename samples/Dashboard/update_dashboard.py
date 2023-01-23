import py_grafana.grafana.dashboard.Dashboard
from py_grafana import Grafana, Folder

# connect to grafana server
grafana = Grafana().connect("localhost", 3000)

# create a folder f1
folder = Folder(title="f1", uid="uzumaki")
grafana.folder_api.create_folder(folder)
print(folder)

# create a new dashboard under folder f1
grafana.dashboard_api.create_dashboard(folder, "new db")
db = grafana.folders["f1"].dashboards["new db"]
print(db)

# changing refresh rate and updating
db.refresh = 10
grafana.dashboard_api.update_dashboard(db)

db = py_grafana.grafana.dashboard.Dashboard.Dashboard()

grafana.dashboard_api.update_dashboard(db)

# fetching to see updated result
db = grafana.dashboard_api.fetch_dashboard_by_uid(db.uid)
print(db)
