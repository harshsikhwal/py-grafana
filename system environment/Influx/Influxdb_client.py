import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDB:

    def __init__(self, url, org, token):
        """
        Initializes InfluxDB obj, stays global and is shared by multiple buckets
        :param url: The URL of the Influx server
        :param org: The organization
        :param token: The API Token
        """
        self.Url = url
        self.Org = org
        self.Token = token

        try:
            self.Client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

        except:
            print("Unable to connect")
            return

        print("Connection successful")

    def create_bucket(self, bucket_name):

        bucket = self.Client.buckets_api().find_bucket_by_name(bucket_name)
        if bucket is not None:
            self.Client.buckets_api().delete_bucket(bucket)

        self.Client.buckets_api().create_bucket(bucket_name=bucket_name, org=self.Org)
        return Bucket(bucket_name, self.Org, self.Client)


class Bucket:
    """Stores the bucket(database) data"""

    def __init__(self, bucket_name, org, client):
        """
        Initiializes the bucket and creates a new bucket
        :param bucket_name: The name of the bucket
        :param org: The associated organization
        :param client: The client from Influx
        """
        self.BucketName = bucket_name
        self.Org = org
        self.Client = client
        self.WriteAPI = client.write_api(write_options=SYNCHRONOUS)

    def set_measurement(self, measurement):
        """
        Sets the measurement (table name)
        :param measurement: The name of the measurement
        :return: None
        """
        self.measurement = measurement

    def add_and_commit_field_set(self, time=None, fields=None, tags=None):
        """
        Adds a time, tag and field set and returns 1 on successful write
        :param time: The time parameter associated
        :param fields: The field dict. should contain column as key and value as value
        :param tags: The associated tags. Input is a dict
        :return: 1 on success, -1 on fail
        """
        influx_metric = {}
        # if time is not None:
        #     influx_metric["time"] = time

        if fields is not None:
            influx_metric["fields"] = fields

        if tags is not None:
            influx_metric["tags"] = tags

        influx_metric["measurement"] = self.measurement
        data = []
        data.append(influx_metric)
        try:
            print(data)
            self.WriteAPI.write(self.BucketName, self.Org, data)
        except:
            print("Unable to write data")
            return -1
        print("Writing data to influx successful")
        return 1
