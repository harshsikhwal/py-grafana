from py_grafana.grafana.datasource.DataSource import DataSource


class Influx(DataSource):

    def __init__(self):
        super(Influx, self).__init__()
        self.type = "influxdb"
        self.defaultBucket = None
        self.httpMethod = "POST"
        self.httpMode = "POST"
        self.organization = None
        self.version = "Flux"
        self.access = "proxy"

    def obj_to_dict(self):
        # TODO find a better way to generate dictionaries
        json_data = {
            'defaultBucket': self.defaultBucket,
            'httpMethod': self.httpMethod,
            'httpMode': self.httpMode,
            'organization': self.organization,
            'version': self.version
        }
        influx_dict = self.__dict__.copy()
        influx_dict["jsonData"] = json_data
        del influx_dict["defaultBucket"]
        del influx_dict["httpMethod"]
        del influx_dict["httpMode"]
        del influx_dict["organization"]
        del influx_dict["version"]
        return influx_dict

    def dict_to_obj(self, influx_dict):
        for key in self.__dict__:
            if key in influx_dict:
                self.__dict__[key] = influx_dict[key]
        return self


class Prometheus(DataSource):

    def __init__(self):
        super(Prometheus, self).__init__()
        self.type = "prometheus"
        self.httpMethod = "POST"

    def obj_to_dict(self):
        # TODO find a better way to generate dictionaries
        json_data = {
            'httpMethod': self.httpMethod
        }
        prometheus_dict = self.__dict__.copy()
        prometheus_dict["jsonData"] = json_data
        del prometheus_dict["httpMethod"]
        return prometheus_dict

    def dict_to_obj(self, prometheus_dict):
        for key in self.__dict__:
            if key in prometheus_dict:
                self.__dict__[key] = prometheus_dict[key]
        return self
