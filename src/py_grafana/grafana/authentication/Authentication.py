from py_grafana.base import Base
from py_grafana.token import BearerToken


class APIKey:
    def __init__(self):
        self.id = None
        self.name = None
        self.role = "Viewer"
        self.seconds_to_live = None
        self.expiration = None
        self.token = None

    def set_token(self, token: str):
        self.token = token

    def dict_to_obj(self, organization_dict):
        for key in self.__dict__:
            if key in organization_dict:
                self.__dict__[key] = organization_dict[key]
        return self

    def obj_to_dict(self):
        api_dict = self.__dict__.copy()
        del api_dict["token"]
        return api_dict


class AuthenticationAPI(Base):
    def __init__(self, parent):
        super(AuthenticationAPI, self).__init__(parent)
        self.basic_token = None

    def set_token(self, basic_token):
        self.basic_token = basic_token

    def get_api_keys(self):
        # GET /api/auth/keys
        slug = "/api/auth/keys"
        api_key_dict = self._fetch(slug, token=self.basic_token)
        api_keys = []
        if api_key_dict is not None:
            for auth in api_key_dict:
                api_keys.append(APIKey().dict_to_obj(auth))
        return api_keys

    def create_api_key(self, api_key: APIKey):
        # POST /api/auth/keys
        slug = "/api/auth/keys"
        key = self._create(slug, api_key.obj_to_dict(), token=self.basic_token)
        if key is not None:
            api_key.id = key["id"]
            return key["key"]
        return None

    def delete_api_key_by_id(self, api_key_id: int):
        # DELETE /api/auth/keys/:id
        slug = "/api/auth/keys/" + str(api_key_id)
        return self._remove(slug, token=self.basic_token)

    def delete_api_key(self, api_key: APIKey):
        # DELETE /api/auth/keys/:id
        slug = "/api/auth/keys/" + str(api_key.id)
        return self._remove(slug, token=self.basic_token)
