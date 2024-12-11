from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys             #used in this scenario to automatically press the enter key after typing the password
from selenium.webdriver.support.ui import WebDriverWait     #this replaces time.sleep. using webdriverwait is more time efficient
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
  options = webdriver.EdgeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
 
  driver = webdriver.Edge(options=options)                      #the driver is responsible for launching the browser and controlling it, and allows us to use methods like find_elements() etc.
  driver.get("http://automated.pythonanywhere.com")             #loads the web page to prepare it for scraping
  return driver
 
def main():
  driver = get_driver()
  try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/div/div/a")))
    driver.find_element(By.XPATH, "/html/body/nav/div/div/div/a").click()                                         #click the login button
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "id_username"))).send_keys("automated") #fill out user and password, then click enter
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-success")))
    avg_temp = driver.find_element(By.CLASS_NAME, "text-success").text
    return avg_temp
  except Exception as e:
    print(f"Exception occured: {e}")
    return None
  finally:
    driver.quit()



print(main())