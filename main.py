from selenium import webdriver
from selenium.webdriver.common.by import By

"""
below we are setting options to make browsing easier. 
disable infobars means ignoring things such as nav bars on an html file
start maximized means that the page we are scraping gets maximized, since sometimes web content gets hidden when browser is resized
disable dev shm is related to linux
no sandbox gives our script greater privileges on pages
the experimental options we added is to help our scripts not be detected by web pages
"""
def get_driver():
  options = webdriver.EdgeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
 
  driver = webdriver.Edge(options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver
 
def main():
  driver = get_driver()
  element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
  return element.text
 
print(main())