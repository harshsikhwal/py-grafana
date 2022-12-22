from py_grafana import Grafana, Token, APIKey

token = Token.BearerToken("eyJrIjoienZHR3pwclgyOXRmSWU3R2owa1VRUzVJY0Q1MXlIalUiLCJuIjoiYXNkIiwiaWQiOjF9")

grafana = Grafana().connect("localhost", 3000, token)

api_key = APIKey()
api_key.name = "test key"
api_key.role = "admin"

# create key
key = grafana.authentication_api.create_api_key(api_key)

# delete the same
grafana.authentication_api.delete_api_key_by_id(api_key.id)
