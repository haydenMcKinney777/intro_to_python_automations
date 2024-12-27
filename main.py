from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait     #this replaces time.sleep. using webdriverwait is more time efficient
from selenium.webdriver.support import expected_conditions as EC
import yagmail
import os
import re      #for cleaning up text

def get_driver():
  options = webdriver.EdgeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
 
  driver = webdriver.Edge(options=options)              #the driver is responsible for launching the browser and controlling it, and allows us to use methods like find_elements() etc.
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")     #loads the web page to prepare it for scraping
  return driver


def send_email(percent):
    sender = os.getenv('gmail_email')
    password = os.getenv('app_password_gmail')
    receiver = os.getenv('email')
    yag = yagmail.SMTP(sender, password)

    subject = "Stock Percentage Dropped Below -0.10%!"
    contents = f"This email is to inform you that the stock price is now {percent}%!\n"

    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email has been successfully sent.\n")


def main():
    driver = get_driver()
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".stock-trend.trend-drop")))

        stock_percentage = driver.find_element(By.CSS_SELECTOR, ".stock-trend.trend-drop").text

        cleaned_stock_percentage = float(re.sub(r"[^\d.-]", "", stock_percentage))     #\d = any decimal, . = literal dot, - = literal minus, ^ in square brackets is boolean NOT, so we're saying anything that is not a digit, dot, or minus sign, take it out

        if cleaned_stock_percentage < -0.10:
            send_email(cleaned_stock_percentage)
    finally:
        driver.quit()

main()