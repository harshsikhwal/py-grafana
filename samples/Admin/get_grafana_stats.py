from py_grafana import Grafana, BasicToken

grafana = Grafana().connect("localhost", 3000)

bt = BasicToken("admin", "admin")

grafana.admin_api.set_token(bt)

stats = grafana.admin_api.fetch_grafana_stats()

print(stats)
