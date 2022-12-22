from py_grafana import Grafana

# connect to grafana server
grafana = Grafana().connect("localhost", 3000)

# create a new dashboard under folder f1
db = grafana.dashboard_api.fetch_dashboard_by_uid("TAzwbbc4z")
print(db)

