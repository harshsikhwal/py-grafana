import json

class Datasource:
    """A class that stores the DataSource data"""
    def __init__(self):
        """
        {
            "id": 1,
            "orgId": 1,
            "uid": "H8joYFVGz"
            "name": "datasource_elastic",
            "type": "elasticsearch",
            "typeLogoUrl": "public/app/plugins/datasource/elasticsearch/img/elasticsearch.svg",
            "access": "proxy",
            "url": "http://mydatasource.com",
            "password": "",
            "user": "",
            "database": "grafana-dash",
            "basicAuth": false,
            "isDefault": false,
            "jsonData":
            {
                "esVersion": 5,
                "logLevelField": "",
                "logMessageField": "",
                "maxConcurrentShardRequests": 256,
                "timeField": "@timestamp"
            },
            "readOnly": false
        }
        """
        self.id = None
        self.orgId = None
        self.uid = None
        self.name = None
        self.type = None
        self.typeLogoUrl = None
        self.access = None
        self.url = None
        self.password = None
        self.user = None
        self.database = None
        self.basicAuth = None
        self.isDefault = None
        self.jsonData = {}
        self.secureJsonData = {}
        self.readOnly = None

    def to_json(self):
        datasource_json = {}
        if self.id is not None:
            datasource_json["id"] = self.id
        if self.orgId is not None:
            datasource_json["ordId"] = self.orgId
        if self.uid is not None:
            datasource_json["uid"] = self.uid
        if self.name is not None:
            datasource_json["name"] = self.name
        if self.type is not None:
            datasource_json["type"] = self.type
        if self.typeLogoUrl is not None:
            datasource_json["typeLogoUrl"] = self.typeLogoUrl
        if self.access is not None:
            datasource_json["access"] = self.access
        if self.url is not None:
            datasource_json["url"] = self.url
        if self.password is not None:
            datasource_json["password"] = self.password
        if self.database is not None:
            datasource_json["database"] = self.database
        if self.basicAuth is not None:
            datasource_json["basicAuth"] = self.basicAuth
        if self.isDefault is not None:
            datasource_json["isDefault"] = self.isDefault
        if len(self.jsonData) > 0:
            datasource_json["jsonData"] = self.jsonData
        if len(self.secureJsonData) > 0:
            datasource_json["secureJsonData"] = self.secureJsonData
        if self.readOnly is not None:
            datasource_json["readOnly"] = self.readOnly

    def dict_to_obj(self, j):
        # TODO if API returns something extra, how will that be handled?
        self.__dict__ = json.loads(j)
