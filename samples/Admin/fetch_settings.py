import json
from py_grafana import Grafana, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.admin_api.set_token(bt)

settings = grafana.admin_api.fetch_settings()

print(json.dumps(settings, indent=4))
