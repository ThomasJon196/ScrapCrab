# Init influxDB with access token. Required for access to the database.

docker run --rm -d -p 8086:8086 \
      -v $PWD/influx/database:/var/lib/influxdb2 \
      -v $PWD/influx/config.yml:/etc/influxdb2/config.yml \
      -e DOCKER_INFLUXDB_INIT_MODE=setup \
      -e DOCKER_INFLUXDB_INIT_USERNAME=admin \
      -e DOCKER_INFLUXDB_INIT_PASSWORD=admin123 \
      -e DOCKER_INFLUXDB_INIT_ORG=ScrapCrab-Org \
      -e DOCKER_INFLUXDB_INIT_BUCKET=Scrap-bucket \
      -e DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=secret-influx-db-token \
      --name influxdb \
      influxdb:2.0
