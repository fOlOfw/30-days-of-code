"""
Goals: 
- Scrape game news data from two main websites
- Keywords: Unity, Unreal
- Create a Twitter bot where every 3 hours news will be listed
Libraries:
Pandas is a library used for data manipulation and analysis. It is used to extract the data and store it in the desired format
Selenium is a web testing library. It is used to automate browser activities
Beautiful Soup is a Python package for parsing HTML and XML documents. It creates parse trees that is helpful to extract the data easily
"""
import requests
import sys
import pandas as pd
from selenium import webdriver
from BeautifulSoup import BeautifulSoup


print(sys.path)

msg = "Hello World"
print(msg)
