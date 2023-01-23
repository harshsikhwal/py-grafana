from py_grafana import Grafana, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.datasource_api().set_token(bt)

datasource = grafana.datasource_api().get_datasource_by_name("testdb")

print(datasource.obj_to_dict())