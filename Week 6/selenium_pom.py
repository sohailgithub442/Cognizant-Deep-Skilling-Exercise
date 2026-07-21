from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Login Page Object
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Dashboard Page Object
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()

# Test Execution
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

login = LoginPage(driver)
login.login("tomsmith", "SuperSecretPassword!")

dashboard = DashboardPage(driver)
dashboard.logout()

driver.quit()
