from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com")
driver.maximize_window()

search = driver.find_element(By.NAME, "q")
search.send_keys("Python Selenium")
search.send_keys(Keys.RETURN)

time.sleep(3)

print("Page Title:", driver.title)

driver.quit()
