from py_grafana import Grafana

grafana = Grafana().connect("localhost", 3000)

datasources = grafana.datasource_api().fetch_all_datasource()

for datasource in datasources:

    print(datasource.obj_to_dict())