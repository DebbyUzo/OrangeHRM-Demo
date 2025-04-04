import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define Variables
URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"
PAUSE = 5

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
wait = WebDriverWait(driver, PAUSE)

# Valid Username Login
Enter_Email = wait.until(EC.presence_of_element_located((By.NAME, "username")))
Enter_Email.send_keys("Admin")

# Valid Password Login
Enter_Password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
Enter_Password.send_keys("admin123")

# Valid Login Button
Enter_Login = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Enter_Login.click()

# Navigate to the Admin Page
Enter_Admin = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')))
Enter_Admin.click()

# Navigate to the Admin page header

# View User Management
Enter_UserManagement = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')))
Enter_UserManagement.click()

# Select User from the User Management drop-down menu.
Enter_User = wait.until(EC.presence_of_element_located((By.XPATH,  '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li')))
Enter_User.click()

# View Job
Enter_Job = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')))
Enter_Job.click()

# Select Job Title from the Job drop-down menu.
Enter_JobTitle = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a')))
Enter_JobTitle.click()

# Select Pay Grades from the Job drop=down menu
Enter_PayGrades = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]')))
Enter_PayGrades.click()

# Select Employment Status from the Job drop=down menu
Enter_EmploymentStatus = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]')))
Enter_EmploymentStatus.click()

# Select Job Categories from the Job drop=down menu
Enter_JobCategories = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[4]')))
Enter_JobCategories.click()

# Select Work Shifts from the Job drop=down menu
Enter_WorkShifts = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[5]')))
Enter_WorkShifts.click()

# View Organisation
Enter_Organisation = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span')))
Enter_Organisation.click()

# Select General Information from the Organisation drop=down menu
Enter_GeneralInformation = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]')))
Enter_GeneralInformation.click()

# Select Location from the Organisation drop=down menu
Enter_Location = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]')))
Enter_Location.click()

# Select Structure from the Organisation drop=down menu
Enter_Structure = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]')))
Enter_Structure.click()

# View Qualification
Enter_Qualification = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')))
Enter_Qualification.click()

# Select Skills from the Qualification drop=down menu
Enter_Skills = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]')))
Enter_Skills.click()

# Select Education from the Qualification drop=down menu
Enter_Education = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]')))
Enter_Education.click()

# Select License from the Qualification drop=down menu
Enter_Licenses = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[3]')))
Enter_Licenses.click()

# Select Languages from the Qualification drop=down menu
Enter_Languages = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[4]')))
Enter_Languages.click()

# Select Memberships from the Qualification drop=down menu
Enter_Memberships = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[5]')))
Enter_Memberships.click()

# View Nationalities
Enter_Nationalities = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a')))
Enter_Nationalities.click()

# Click on Add from Nationalities Page
Enter_Add = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button')))
Enter_Add.click()

# Click on Records Found from Nationalities Page
Enter_RecordsFound = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]')))
Enter_RecordsFound.click()


# Pause for demonstration
time.sleep(PAUSE)

# Close Browser
driver.quit()