from py_grafana.grafana.datasource.DataSource import DataSource


class ElasticSearch(DataSource):

    def __init__(self):
        super(ElasticSearch, self).__init__()
        self.esVersion = None
        self.logLevelField = ""
        self.logMessageField = ""
        self.maxConcurrentShardRequests = 256
        self.timeField = "@timestamp"
        self.type = "elasticsearch"

    def obj_to_dict(self):
        # TODO find a better way to generate dictionaries
        json_data = {
            "esVersion": self.esVersion,
            "logLevelField": self.logLevelField,
            "logMessageField": self.logMessageField,
            "maxConcurrentShardRequests": self.maxConcurrentShardRequests,
            "timeField": self.timeField
        }
        elastic_dict = self.__dict__.copy()
        elastic_dict["jsonData"] = json_data
        del elastic_dict["esVersion"]
        del elastic_dict["logLevelField"]
        del elastic_dict["logMessageField"]
        del elastic_dict["maxConcurrentShardRequests"]
        del elastic_dict["timeField"]

    def dict_to_obj(self, elastic_dict):
        for key in self.__dict__:
            if key in elastic_dict:
                self.__dict__[key] = elastic_dict[key]
        return self
