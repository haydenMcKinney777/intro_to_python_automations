from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get('https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6')

stock_trend = driver.find_element(By.CSS_SELECTOR, ".stock-trend.trend-drop")
print(type(stock_trend))