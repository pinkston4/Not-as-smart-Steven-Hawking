import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
import string

class Fetcher:
    """
    The Fetcher class is the web scraper/parser
    Fetcher searches google and looks for the google supplied answer
    methods:
        __init__()
        lookup()
    """
    def __init__(self, url):
        self.driver = webdriver.PhantomJS()
        self.driver.wait =WebDriverWait(self.driver, 5)
        self.url = url

    def lookup(self,):
        """
        lookup is a method that actually makes the call to the internet and parses the results
        """
        self.driver.get(self.url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        if soup.find_all(class_='_sPg') == []:
            return
        else:
            answer = soup.find_all(class_='_sPg')[0]
            result_beta = str(answer.get_text())
            result = result_beta.replace('(', '').replace(')', '')
            self.driver.quit()
            return result
