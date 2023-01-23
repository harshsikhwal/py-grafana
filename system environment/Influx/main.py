import time
import random
from Influxdb_client import InfluxDB, Bucket

influx_db = None
car_speed_influx_bucket = None
traffic_metric_influx_bucket = None

car_list = ["Honda", "Chevrolet", "Mercedes-Benz", "Ford", "Toyota"]
traffic_stat_list = ["Tx Frames", "Rx Frames", "Tx Bytes", "Rx Bytes"]



def generate_data():
    global car_speed_influx_bucket
    global traffic_metric_influx_bucket
    while True:
        car_stats = {}
        traffic_stats = {}

        # generate car speed
        for i in range(len(car_list)):
            # generate speed
            car_stats[car_list[i]] = random.randint(0, 200)

        car_speed_influx_bucket.add_and_commit_field_set(fields=car_stats)

        # generate traffic stats
        for i in range(len(traffic_stat_list)):
            # generate data
            traffic_stats[traffic_stat_list[i]] = random.randint(0, 1000000)

        traffic_metric_influx_bucket.add_and_commit_field_set(fields=traffic_stats)
        # add to influx db

        time.sleep(5)


def create_connection():
    global influx_db
    global car_speed_influx_bucket
    global traffic_metric_influx_bucket
    influx_db = InfluxDB(url="http://localhost:8086/",
                         token="Ohilgzn22aQFwscO-af5RqwfqAkPcAu0KLxMDWSCbM6a0ybZPekt_7v6VZsxeTlmxv6KOf7vlldL2MS9uQ8CLA==",
                         org="testorg")
    car_speed_influx_bucket = influx_db.create_bucket("car speed")
    car_speed_influx_bucket.set_measurement("car")
    traffic_metric_influx_bucket = influx_db.create_bucket("traffic metric")
    traffic_metric_influx_bucket.set_measurement("traffic")


def main():
    create_connection()
    generate_data()


if __name__ == "__main__":
    main()
