from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys             #used in this scenario to automatically press the enter key after typing the password
from selenium.webdriver.support.ui import WebDriverWait     #this replaces time.sleep. using webdriverwait is more time efficient
from selenium.webdriver.support import expected_conditions as EC

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
 
  driver = webdriver.Edge(options=options)                      #the driver is responsible for launching the browser and controlling it, and allows us to use methods like find_elements() etc.
  driver.get("http://automated.pythonanywhere.com/login/")      #loads the web page to prepare it for scraping
  return driver
 
def main():
  driver = get_driver()

  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "id_username")))                #tells the driver to wait a maximum of 5 seconds, or until the username field has been located. 
  driver.find_element(By.ID, value="id_username").send_keys("automated")                                #find the 'username' field on the login page by its ID, and send the keyboard keys "automated" which will be used to fill the text box (the username is automated and pw is automatedautomated)
  driver.find_element(By.ID, value="id_password").send_keys("automatedautomated" + Keys.RETURN)         #enter the password and press enter
  
  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/div/a")))
  driver.find_element(By.XPATH, value="/html/body/nav/div/a").click()   #click the home link
  print(driver.current_url)

print(main())