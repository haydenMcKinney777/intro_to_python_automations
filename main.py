from selenium import webdriver
import time
from selenium.webdriver.common.by import By

"""
below we are setting options to make browsing easier. 
disable infobars means ignoring things such as nav bars on an html file
start maximized means that the page we are scraping gets maximized, since sometimes web content gets hidden when browser is resized
disable dev shm is related to linux
no sandbox gives our script greater privileges on pages
the experimental options we added is to help our scripts not be detected by web pages

analogy: think of the driver as a remote control for a web page, and the python script is the one pushing the controller buttons
"""
def get_driver():
  options = webdriver.EdgeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
 
  driver = webdriver.Edge(options=options)              #the driver is responsible for launching the browser and controlling it, and allows us to use methods like find_elements() etc.
  driver.get("http://automated.pythonanywhere.com")     #loads the web page to prepare it for scraping
  return driver
 
def main():
  driver = get_driver()
  time.sleep(3)        #the dynamic value takes about 2-3 seconds to load onto the html page, so we do not want to scrape the page until after that value has loaded in.
  element = driver.find_element(By.XPATH, value="/html/body/div[1]/div/h1[2]")      #driver.find_element() returns a WebElement object, which we are then assigning to our variable called 'element' (that's where the .text field comes from)
  return element.text
 
print(main())