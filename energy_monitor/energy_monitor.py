import os
import sys
import time
import sched
import signal
from datetime import datetime

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv
from p110 import TapoP110


s = sched.scheduler(time.time, time.sleep)


def insert_data(sc, client, p110):
    bucket = os.getenv("INFLUXDB_V2_BUCKET")
    hostname = os.getenv("PLUG_NAME")
    current_power = p110.get_current_power()

    # Create point with the current power consumption
    p = Point("energy_consumption") \
        .tag("host", hostname) \
        .field("current_power", current_power)

    # Write data to influxdb bucket
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket=bucket, record=p)

    # Log data
    print("[" + str(hostname) + "] " +
          datetime.now().isoformat() + ": " +
          str(current_power) + " mW")

    # Re-run this function every 3s without drifting
    s.enter((3 - time.time() % 3), 1, insert_data, (sc, client, p110,))


def signal_handler(sig, frame):
    # Cancel all scheduler events
    list(map(s.cancel, s.queue))

    sys.exit(0)


def main():
    print("P110 Energy Monitor by @mercxry")
    load_dotenv()

    # Initialize clients
    p110 = TapoP110()
    client = InfluxDBClient.from_env_properties()

    # Start scheduler
    s.enter((3 - time.time() % 3), 1, insert_data, (s, client, p110,))
    s.run()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
