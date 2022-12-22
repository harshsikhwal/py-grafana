from py_grafana import Grafana, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.admin_api.set_token(bt)

settings = {
  "updates":
  {
    "auth.saml":
    {
      "enabled": "true"
    }
  }
}

grafana.admin_api.update_settings(settings)

