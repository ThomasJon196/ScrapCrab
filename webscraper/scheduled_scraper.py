
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from scraper import *
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
# Init influxDB credentials
from dotenv import load_dotenv
import os
import sys
load_dotenv()
influx_token = os.environ.get('influx_token')
influx_org   = os.environ.get('influx_org')
influx_bucket = os.environ.get('influx_bucket')
influxdb_url = os.environ.get('influxdb_url')
REFRESH_INTERVAL_MINUTES = os.environ.get('REFRESH_INTERVAL_MINUTES')

# Define Logger
logging.basicConfig(
    level=logging.WARNING,
    format="[%(asctime)s]" + logging.BASIC_FORMAT,
    datefmt="%d/%b/%Y %H:%M:%S",
    stream=sys.stdout)
logger = logging.getLogger(__name__)


def write_to_influxdb(dataframe):
    client = InfluxDBClient(url=f"http://{influxdb_url}:8086",
                            token=influx_token, org=influx_org)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(influx_bucket, influx_org, record=dataframe,
                    data_frame_measurement_name='waterlevel',
                    data_frame_tag_columns=['waterlevel'])
    write_api.close()
    client.close()

def update_waterlevel_database():
    df = scrap_data_into_dataframe()
    write_to_influxdb(df)
    logger.info("Executed databased update.")
    logger.warning("Warning it works.")

# Start Scheduler which runs infinitely
scheduler = BlockingScheduler()
scheduler.add_job(update_waterlevel_database, 'interval', seconds=REFRESH_INTERVAL_MINUTES)
scheduler.start()