# SETUP InfluxDB


## Generate `config.yaml` for custom configuration

```bash
$ docker run --rm influxdb:2.5.1 influxd print-config > config.yml
```

## Run influx container withall necessary env-variables



```bash
docker run --rm -d -p 8086:8086 \
      -v $PWD/influx/database:/var/lib/influxdb2 \
      -v $PWD/influx/config.yml:/etc/influxdb2/config.yml \
      -e DOCKER_INFLUXDB_INIT_MODE=setup \
      -e DOCKER_INFLUXDB_INIT_USERNAME=admin \
      -e DOCKER_INFLUXDB_INIT_PASSWORD=admin123 \
      -e DOCKER_INFLUXDB_INIT_ORG=ScrapCrab-Org \
      -e DOCKER_INFLUXDB_INIT_BUCKET=Scrap-bucket \
      influxdb:2.5.1
```