import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define Variables
URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"
WAIT_TIME = 10  # Increased for better stability

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
wait = WebDriverWait(driver, WAIT_TIME)

# Perform Login
wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(USERNAME)
wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(PASSWORD)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'oxd-button')]"))).click()

# Click on Admin button
admin_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")))
admin_button.click()
time.sleep(2)  # Allow navigation

# Click on "Add" Button
add_user_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add')]")))
print("Successfully clicked the 'Add' button!")

