from py_grafana import Grafana

grafana = Grafana().connect("localhost", 3000)

datasource = grafana.datasource_api().get_datasource_by_id(5)

print(datasource.obj_to_dict())