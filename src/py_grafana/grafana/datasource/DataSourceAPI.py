from py_grafana.base import Base
import py_grafana.grafana.datasource as DataSource


def classify_json_as_datasource(datasource_dict):
    datasource_obj = None
    if datasource_dict["type"] == "influxdb":
        datasource_obj = DataSource.TimeSeries.Influx()
        datasource_obj.dict_to_obj(datasource_dict)
        return datasource_obj

    if datasource_dict["type"] == "mssql":
        datasource_obj = DataSource.SQL.MSSQL()
        datasource_obj.dict_to_obj(datasource_dict)
        return datasource_obj

    if datasource_dict["type"] == "prometheus":
        datasource_obj = DataSource.TimeSeries.Prometheus()
        datasource_obj.dict_to_obj(datasource_dict)
        return datasource_obj

    if datasource_dict["type"] == "elasticsearch":
        datasource_obj = DataSource.DocumentAndLogging.ElasticSearch()
        datasource_obj.dict_to_obj(datasource_dict)
        return datasource_obj

    else:
        datasource_obj = DataSource.TimeSeries.DataSource()
        datasource_obj.dict_to_obj(datasource_dict)
        return datasource_obj


class DataSourceAPI(Base):

    def __init__(self, parent):
        super(DataSourceAPI, self).__init__(parent)
        self.basic_token = None

    def set_token(self, basic_token):
        self.basic_token = basic_token

    def fetch_all_datasource(self):
        """
        Returns a list of Datasources
        """
        # GET /api/datasources
        slug = "/api/datasources"
        datasource_dict = self._fetch(slug, token=self.basic_token)
        datasources = []
        if datasource_dict is not None:
            for datasource in datasource_dict:
                datasources.append(classify_json_as_datasource(datasource))
        return datasources

    def create_datasource(self, datasource):
        # POST /api/datasources
        slug = "/api/datasources"
        datasource_json = self._create(slug, payload=datasource.obj_to_dict(), token=self.basic_token)
        if "datasource" in datasource_json:
            datasource.dict_to_obj(datasource_json["datasource"])
        if "message" in datasource_json:
            if datasource_json["message"] == "Datasource added":
                return self
        return None

    def get_datasource_by_id(self, datasource_id):
        # GET /api/datasources/:datasourceId
        slug = "/api/datasources/" + str(datasource_id)
        datasource_json = self._fetch(slug, token=self.basic_token)
        if datasource_json is not None:
            return classify_json_as_datasource(datasource_json)

    def get_datasource_by_uid(self, datasource_uid):
        # GET /api/datasources/uid/:uid
        slug = "/api/datasources/uid/" + datasource_uid
        datasource_json = self._fetch(slug, token=self.basic_token)
        if datasource_json is not None:
            return classify_json_as_datasource(datasource_json)

    def get_datasource_by_name(self, datasource_name):
        # GET /api/datasources/name/:name
        slug = "/api/datasources/name/" + str(datasource_name)
        datasource_json = self._fetch(slug, token=self.basic_token)
        if datasource_json is not None:
            return classify_json_as_datasource(datasource_json)

    def update_datasource(self, datasource):
        # PUT /api/datasources/uid/:uid
        slug = "/api/datasources/uid/" + str(datasource.uid)
        datasource_json = self._put(slug, payload=datasource.obj_to_dict(), token=self.basic_token)
        if "datasource" in datasource_json:
            datasource.dict_to_obj(datasource_json["datasource"])
        if "message" in datasource_json:
            if datasource_json["message"] == "Datasource added":
                return self
        return None

    def delete_datasource(self, datasource):
        # DELETE /api/datasources/:datasourceId
        # DELETE /api/datasources/uid/:uid
        # DELETE /api/datasources/name/:datasourceName
        slug = "/api/datasources/" + str(datasource.id)
        return self._remove(slug, token=self.basic_token)
