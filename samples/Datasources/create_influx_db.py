from py_grafana import Grafana, DataSource

grafana = Grafana().connect("localhost", 3000)

inf = DataSource.TimeSeries.Influx()

inf.name = "mndb3"
inf.url = "http://localhost:8086"
inf.defaultBucket = "live data"
inf.httpMethod = "POST"
inf.httpMode = "POST"
inf.organization = "key"
inf.version = "Flux"
inf.access = "proxy"

grafana.datasource_api.create_datasource(inf)

print(inf.obj_to_dict())