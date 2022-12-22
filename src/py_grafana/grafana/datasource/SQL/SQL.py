from py_grafana.grafana.datasource.DataSource import DataSource


class MSSQL(DataSource):

    def __init__(self):
        super(MSSQL, self).__init__()
        self.httpMethod = None
        self.type = "mssql"

    def obj_to_dict(self):
        # TODO find a better way to generate dictionaries
        json_data = {
            'httpMethod': self.httpMethod
        }
        sql_dict = self.__dict__.copy()
        sql_dict["jsonData"] = json_data
        del sql_dict["httpMethod"]
        return sql_dict

    def dict_to_obj(self, sql_dict):
        for key in self.__dict__:
            if key in sql_dict:
                self.__dict__[key] = sql_dict[key]
        return self
