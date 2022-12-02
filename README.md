# ScrapCrab

Automated webscraping combined with a dashboard.
Master project.

# Goal

- ~~Build service Retrieve data from web (Scrapping, API, downloads) [Python, BeautifulSoup, Requests, Selenium]~~
- ~~Store data in database ([InfluxDB] for time series~~, [Prometheus] for Monitoring)
- Create Dashboard to display data [Grafana]
- Deploy application via docker-compose. (Optionaly on continously running machine Chromebox)

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
                - Added headless Chromedriver to python. Required for running inside a docker-container. 
                    Window settings window size was important somehow. 
                    Source: https://www.geeksforgeeks.org/driving-headless-chrome-with-python/
                - Added Chromedriver-version handling in Dockerfile.
                - Added .dockerignore for smaller Build Context
                - docker-compose added and scraper + influxdb works.
                - 7 hours

    
# IDEAS

- Alternatively use selenium standalone images https://github.com/SeleniumHQ/docker-selenium
- Add env-variables & conditionals for logging levels
- Check chromedriver compatibility
- Best practise to load .env variables into Docker Image