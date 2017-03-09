from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup


class Fetcher:
    """
    The Fetcher class is the web scraper/parser
    Fetcher searches google and looks for the google supplied answer
    Fether uses PhantomJS as a headless browser which it then uses to look up
    what the user wants in google and then return the page. Which is then parsed
    with BeautifulSoup.
    methods:
        __init__()
        lookup()
    """
    def __init__(self, url):
        self.driver = webdriver.PhantomJS()
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url

    def lookup(self,):
        """
        lookup is a method that actually makes the call to the internet and parses the results
        """
        self.driver.get(self.url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        if soup.find_all(class_='_sPg') == []:
            if soup.find_all(class_='_m3b') != []:
                answer = soup.find_all(class_='_m3b')[0]
                result_beta = str(answer.get_text())
                result = result_beta.replace('(', '').replace(')', '')
                self.driver.quit()
                return result
            else:
                self.driver.quit()
                return
        else:
            answer = soup.find_all(class_='_sPg')[0]
            result_beta = str(answer.get_text())
            result = result_beta.replace('(', '').replace(')', '')
            self.driver.quit()
            return result
