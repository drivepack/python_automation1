from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
  #Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ['enable-automation'])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  url = 'http://automated.pythonanywhere.com'
  driver.get(url)
  return driver

def main():
  driver = get_driver()
  element = driver.find_element(By.XPATH, '//h1[@class="animated fadeIn mb-4"]')
  return element.text

print(main())