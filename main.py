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
    options.add_argument("disable-blank-features = AutomationControlled")

    driver = webdriver.Edge(options=options)
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver

def send_email(percent):
    sender = os.getenv('gmail_email')
    password = os.getenv('app_password_gmail')
    receiver = os.getenv('email')
    yag = yagmail.SMTP(sender, password)

    subject = "Stock Percentage Dropped Below -10.0%!"
    contents = f"This email is to inform you that the stock price is now {percent}%!\n"

    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email sent.\n")


def main():
    driver = get_driver()
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".stock-trend.trend-drop")))

        stock_percentage = driver.find_element(By.CSS_SELECTOR, ".stock-trend.trend-drop").text

        cleaned_stock_percentage = float(re.sub(r"[^\d.-]", "", stock_percentage))     #\d = any decimal, . = literal dot, - = literal minus, ^ in square brackets is boolean NOT, so we're saying anything that is not a digit, dot, or minus sign, take it out

        if cleaned_stock_percentage < -10.0:
            send_email(cleaned_stock_percentage)
    finally:
        driver.quit()

main()