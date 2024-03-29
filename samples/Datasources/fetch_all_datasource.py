from py_grafana import Grafana, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.datasource_api().set_token(bt)


datasources = grafana.datasource_api().fetch_all_datasource()

for datasource in datasources:

    print(datasource.obj_to_dict())