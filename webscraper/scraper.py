"""
Retrieve of Rhein-waterlevel from "https://pegel.bonn.de/php/rheinpegel.php"

Notes:
- Single page website creates content dynamically via PHP. Try Selenium (BeautifulSoup can only retrieve html-content) 
- Downloaded the apropiate chromeDriver version from: https://pypi.org/project/chromedriver-py/107.0.5304.18/
- Use Selenium to navigate through Webpage and retrieve HTML of element
- Use BeautifulSoup to retrieve specific data from HTML
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

from bs4 import BeautifulSoup

import pandas as pd
import re


def scrap_data():
    """
    Scraps waterlevel data from https://pegel.bonn.de/php/rheinpegel.php 
    via `Selenium` & `BeautifulSoup`.
    """
    # Selenium is used to retrieve raw HTML-data    

    service_object = Service(binary_path)
    # Invoke new browser window & Set enable headless mode
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=service_object, options=chrome_options)

    # Navigate to website
    driver.get("https://pegel.bonn.de/php/rheinpegel.php")
    # Select button element
    show_table_button = driver.find_element(by='id', value='btn_table')
    # Click button
    show_table_button.click()
    # Retrieve generated HTML element by id
    waterlevel_data_element = driver.find_elements(by='id', value='dataTable')
    # Get innerHTML content of table
    waterlevel_data_html = waterlevel_data_element[0].get_attribute(
        name='innerHTML')
    driver.close()

    # BeautifulSoup used to retrieve elements inside specific HTML-tags.
    
    # Create Soup from HTML
    soup = BeautifulSoup(waterlevel_data_html, 'html.parser')
    # Find all table rows
    table_rows = soup.find_all('tr')
    table_header = table_rows[0].text
    table_data = table_rows[1:]
    # Split into single td (tabledata) elements
    html_rows = [BeautifulSoup(str(table_data[i]), 'html.parser').find_all('td')
                 for i in range(len(table_data))]
    rows = [[row[0].text, row[1].text] for row in html_rows]
    date_time_raw = [row[0] for row in rows]
    waterlevel_raw = [row[1] for row in rows]
    return date_time_raw, waterlevel_raw


def create_dataframe(date_time_raw, waterlevel_raw):
    """
    Create pandas DataFrame from date_time, waterlevel data.
    """    
    dt = pd.to_datetime(date_time_raw, format="%m/%d/%Y, %H:%M:%S Uhr")
    waterlevel = [int(re.findall(pattern=r'(\d+)', string=waterlevel_raw[i])[0])
                  for i in range(len(waterlevel_raw))]
    data_dict = {
        'Datetime': dt,
        'Waterlevel': waterlevel
    }
    dataFrame = pd.DataFrame(data_dict)
    return dataFrame


def map_duplicates_to_24_hour_format(dataFrame):
    """
    As the dates are stored in 12 hour format wihtout indication of AM/PM,
    later duplicates have to be mapped to the correct time in 24 hour format manually.
    """
    duplicated_mask = dataFrame['Datetime'].duplicated(keep='last')
    dataFrame.loc[duplicated_mask,
                  'Datetime'] = dataFrame['Datetime'][duplicated_mask] + pd.Timedelta(hours=12)
    return dataFrame


def set_index_column_time(dataframe):
    dataframe = dataframe.rename(columns={'Datetime': '_time'})
    dataframe = dataframe.set_index('_time')
    return dataframe

def scrap_data_into_dataframe():
    dt_data, waterlevel_data = scrap_data()
    dataframe = create_dataframe(dt_data, waterlevel_data)
    dataframe = map_duplicates_to_24_hour_format(dataframe)
    dataframe = set_index_column_time(dataframe)
    return dataframe



