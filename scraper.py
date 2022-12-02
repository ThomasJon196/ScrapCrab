"""
Retrieve of Rhein-waterlevel from "https://pegel.bonn.de/php/rheinpegel.php"

Notes:
- Single page website creates content dynamically via PHP. Try Selenium (BeautifulSoup can only retrieve html-content) 
- Downloaded the apropiate chromeDriver version from: https://pypi.org/project/chromedriver-py/107.0.5304.18/
- Use Selenium to navigate through Webpage and retrieve HTML of element
- Use BeautifulSoup to retrieve specific data from HTML
"""

def scrap_data_and_write_to_dataframe():
    """
    This functions does currently multiple things and should be refactored in the future
    1.
    2.
    3.

    returns: pd.DataFrame of current waterlevel readings and timestamps
    """

    from selenium import webdriver                                      # Imports for Selenium + Chromebrowser
    from selenium.webdriver.chrome.service import Service   
    from chromedriver_py import binary_path

    service_object = Service(binary_path)
    driver = webdriver.Chrome(service=service_object)                   # Invoke new browser window

    driver.get("https://pegel.bonn.de/php/rheinpegel.php")              # Navigate to website

    show_table_button = driver.find_element(by='id', value='btn_table') # Find button by id

    show_table_button.click()                                           # Click button

    waterlevel_data_element = driver.find_elements(by='id', value='dataTable')   # Retrieve generated HTML element by id

    waterlevel_data_html = waterlevel_data_element[0].get_attribute(name='innerHTML')   # Get innerHTML content of table

    driver.close()

    from bs4 import BeautifulSoup                                       
    soup = BeautifulSoup(waterlevel_data_html, 'html.parser')           # Create Soup from HTML
    print(soup.prettify())                                              # Print formated HTML view
    table_rows = soup.find_all('tr')                                    # Find all table rows
    table_header = table_rows[0].text
    table_data = table_rows[1:]

    # Temporary save tablerows as txt (REMOVE LATER)

    # with open(file='./table_rows.list', mode='w') as file:
    #     file.write(str(list(table_rows)))



    # Extract tabledata from strings via regex
    # Problem: Database uses 12hour format without specifying pm/am. Has to be mapped manually.
    #           Alternativelly: Tappering is 15 min. 96 - 1 entries per day. (since the last one counts for the next day)
    #                           Let the first 48 entries be 00:00-11:45, and transform the following 47 to 12:00-23:45
    # Fill date, time & waterlevel columns

    # Split into single td (tabledata) elements
    html_rows = [BeautifulSoup(str(table_data[i])).find_all('td') for i in range(len(table_data))]
    rows = [[row[0].text, row[1].text] for row in html_rows]
    date_time_raw     = [row[0] for row in rows]
    waterlevel_raw    = [row[1] for row in rows]


    # Create Pandas dataframe
    import pandas as pd
    dt = pd.to_datetime(date_time_raw, format="%m/%d/%Y, %H:%M:%S Uhr")
    import re
    waterlevel = [int(re.findall(pattern=r'(\d+)', string=waterlevel_raw[i])[0]) for i in range(len(waterlevel_raw))]
    data_dict = {
        'Datetime' : dt,
        'Waterlevel' : waterlevel
    }
    dataFrame = pd.DataFrame(data_dict)


    # Map correct PM values to 24 hour format
    duplicated_mask = dataFrame['Datetime'].duplicated(keep='last')
    dataFrame.loc[duplicated_mask, 'Datetime'] = dataFrame['Datetime'][duplicated_mask] + pd.Timedelta(hours=12)

    print(dataFrame.head())
    return dataFrame

####
# Deprecated section
####

"""
Erhebung des Temperaturmesserte von: http://luadb.lds.nrw.de/LUA/hygon/pegel.php?stationsname_t=Bad-Honnef&yAchse=Standard&hoehe=468&breite=724&datum=2022-11-21&meindatum=21.11.2022&tabellet=Tabelle&nachSuche=&meifocus=&neuname=
Die Seite wird 2023 aktualisiert. Macht keinen Sinn
"""
def depr_func():
    # Map time values to current time since data is missing PM/AM annotations
    import pytz                                                         
    from datetime import datetime
    tz = pytz.timezone('Europe/Berlin')
    berlin_current_datetime = datetime.now(tz)
    print(berlin_current_datetime)


    import requests
    page = requests.get("http://luadb.lds.nrw.de/LUA/hygon/pegel.php?stationsname_t=Bad-Honnef&yAchse=Standard&hoehe=468&breite=724&datum=2022-11-21&meindatum=21.11.2022&tabellet=Tabelle&nachSuche=&meifocus=&neuname=")


    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup.prettify())              # Print formated page content


    measurement_time = soup.find_all('td', class_='messwerte')
    measurement_temp = soup.find_all('td', class_='messwerte_r')


#%

