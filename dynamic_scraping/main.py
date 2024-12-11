from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

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
  try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-success")))
    avg_temp = driver.find_element(By.CLASS_NAME, "text-success")
    print(driver.current_url)
    return avg_temp.text
  except Exception as e:
    print(f"An error occurred: {e}")
    return None
  finally:
    driver.quit()
 
print(main())