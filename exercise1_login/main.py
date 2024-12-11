"""
EXERCISE 1: Click login button, login, scrape the dynamic data and output it. 
            Also, write a new .txt file for each time the dynamic data updates, naming each text file with the current date and time.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys                                                                                                                   
from selenium.webdriver.support.ui import WebDriverWait                                                                                                           
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

def get_driver():
  options = webdriver.EdgeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
 
  driver = webdriver.Edge(options=options)                                                                                                                        #the driver is responsible for launching the browser and controlling it, and allows us to use methods like find_elements() etc.
  driver.get("http://automated.pythonanywhere.com")                                                                                                               #loads the web page to prepare it for scraping
  return driver
 
def write_file(text):
  current_datetime = datetime.datetime.now().strftime("%m-%d-%Y.%H-%M-%S")                                                                                        #stores the current date and time in month-day-year.hour-minute-second
  filename = f"{current_datetime}.txt"
  with open(filename, 'w') as file:
    file.write(text)

def main():
  driver = get_driver()
  try:
      WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/div/div/a"))).click()                                         #click the login button after finding it
      
      WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "id_username"))).send_keys("automated")                                              #fill out user and password, then click enter
      driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)
      
      for _ in range(10):
        avg_temp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-success"))).text.split(": ")[1]                          #wait for and grab the dynamic data, grabbing only the text after the ':' (which is the average temp number we want)
        float(avg_temp)
        write_file(avg_temp)
        time.sleep(2)                                                                                                                                            #im sure there is a way to check if the dynamic data has been updated instead of just waiting 2 seconds, but this achieves the same result for now, and is fine to use since we know for sure the data updates every 2 seconds.
  except Exception as e:
    print(f"Exception occured: {e}")
    return None
  finally:
    driver.quit()

main()