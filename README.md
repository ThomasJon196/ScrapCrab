# ScrapCrab

Automated webscraping, timeseries database & dashboard.

Deployed in a docker-compose environment.

1 Credit Master project.

# Goal

- ~~Build service Retrieve data from web (Scrapping, API, downloads) [Python, BeautifulSoup, Requests, Selenium]~~
- ~~Store data in database ([InfluxDB] for time series~~, [Prometheus] for Monitoring)
- ~~Create Dashboard to display data [Grafana]~~
- ~~Deploy application via docker-compose.~~ (Optionaly on continously running machine Chromebox)

# Deadline: 10.01.2023

# Data sources


Download files: https://www.pegelonline.wsv.de/webservices/files (Temp & waterlevel)

Page content: https://pegel.bonn.de/php/rheinpegel.php (waterlevel)


# CHANGELOG

    xx.11.22    - Started project
                - Researched websites for Rhein waterlevel data
                - Included Selenium & BeatuifulSoup Webscraping
                - 4 hours
    
    01.12.22    - Added jupyternotebook 
                - Finished scrapper
                - Researched influxDB Timeseries Database 
                - 4 hours

    02.12.22    - Added influxDB write from pandas Dataframe
                - Refactored jupyternotebook
                - Investigated scheduled python task: Advanced Python Scheduler
                    Source: https://apscheduler.readthedocs.io/en/3.x/userguide.html
                - Added logging. INFO/WARNING, FORMATER
                    Source: https://stackoverflow.com/questions/16757578/what-is-pythons-default-logging-formatter
                - Added headless Chromedriver to python. Required for running Selenium inside docker-container. 
                    Window settings window size was important somehow. 
                    Source: https://www.geeksforgeeks.org/driving-headless-chrome-with-python/
                - Added Chromedriver-version handling in Dockerfile.
                - Added .dockerignore for smaller Build Context
                - docker-compose added and scraper + influxdb works.
                - 7 hours

    05.12.22    - Tried monitoring/ docker-compose file. Grafana/Prometheus/node-exporter.
                    Prometheus Error: ts=2022-12-05T17:23:46.631Z caller=dedupe.go:112 component=remote level=warn remote_name=37e61e
                     url=grafana msg="Failed to send batch, retrying" err="Post \"grafana\": unsupported protocol scheme \"\""


    22.12.22    - Error: raise NewConnectionError(
      | urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x7f7f1ef17ac0>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution

                Write api cannot find influxdb...somehow. Localhost was accessible.
                Library functinon changed. So i had to add type cast to int.

                - Made grafana work for exported prometheus metrics. But grafana actually imports metrics from prometheus. Prometheus push still fails.

    28.12.2022  - Prometheus vs influxDB : Pull-Based / Push-Based System.
                - Combined monitoring with scraping docker-compose.
                - Integrated influxDB Dashboard into Grafana
                - Solved grafana file permission problems.

# IDEAS

- Grafana credentials are in plaintext inside prometheus.yaml. How to import these env files into yaml file?
- Deploy on Chromebox and Monitor Chromebox Resources
- Alternatively use selenium standalone images https://github.com/SeleniumHQ/docker-selenium
- Add env-variables & conditionals for logging levels
- Check chromedriver compatibility
- Best practise to load .env variables into Docker Image
- ngrok-reverseproxy mit cloudflare-api. (Schwierigkeiten mit der Implementierung in .js)