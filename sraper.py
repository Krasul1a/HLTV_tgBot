
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def connect():
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    global driver
    driver = webdriver.Chrome('/home/dima/PycharmProjects/selenium/chromedriver', options=chrome_options)
    driver.get("https://www.hltv.org/matches")
    sleep(2)
    return 'Connect'
def reconnect():
    driver.refresh()


def disconnect():
    driver.quit()
def matchLive():
    tScore = driver.find_elements_by_class_name('liveMatch')
    return tScore
