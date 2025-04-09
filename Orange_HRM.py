import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define Variables
URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"
PAUSE = 8

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
wait = WebDriverWait(driver, PAUSE)

# Valid Username Login
Enter_Email = wait.until(EC.presence_of_element_located((By.NAME, "username")))
Enter_Email.send_keys(USERNAME)

# Valid Password Login
Enter_Password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
Enter_Password.send_keys(PASSWORD)

# Valid Login Button
Enter_Login = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Enter_Login.click()

# Navigate to the Admin Page
Enter_Admin = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')))
Enter_Admin.click()

# Navigate to the Admin page header

# View User Management
Enter_UserManagement = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')))
Enter_UserManagement.click()
time.sleep(PAUSE)

# Select User from the User Management drop-down menu.
Enter_User = wait.until(EC.presence_of_element_located((By.XPATH,  '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li')))
Enter_User.click()
time.sleep(PAUSE)

# View Job
Enter_Job = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')))
Enter_Job.click()
time.sleep(PAUSE)

# Select Job Title from the Job drop-down menu.
Enter_JobTitle = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a')))
Enter_JobTitle.click()
time.sleep(PAUSE)

# Select Pay Grades from the job drop-down menu.
Enter_PayGrades = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]')))
Enter_PayGrades.click()
time.sleep(PAUSE)

# Select Employment Status from the Job drop-down menu
Enter_EmploymentStatus = wait.until(EC.element_to_be_clickable((By.XPATH, 'Enter_EmploymentStatus = wait.until(EC.element_to_be_clickable((By.XPATH,')))
Enter_EmploymentStatus.click()
time.sleep(PAUSE)

# Select Job Categories from the Job drop-down menu
Enter_JobCategories = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[4]')))
Enter_JobCategories.click()
time.sleep(PAUSE)

# Select Work Shifts from the Job drop-down menu
Enter_WorkShifts = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[5]')))
Enter_WorkShifts.click()
time.sleep(PAUSE)

# View Organisation
Enter_Organisation = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span')))
Enter_Organisation.click()
time.sleep(PAUSE)

# Select General Information from the Organisation drop-down menu
Enter_GeneralInformation = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]')))
Enter_GeneralInformation.click()
time.sleep(PAUSE)

# Select Location from the Organisation drop-down menu
Enter_Location = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]')))
Enter_Location.click()
time.sleep(PAUSE)

# Select Structure from the Organisation drop-down menu
Enter_Structure = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]')))
Enter_Structure.click()
time.sleep(PAUSE)

# View Qualification
Enter_Qualification = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')))
Enter_Qualification.click()
time.sleep(PAUSE)

# Select Skills from the Qualification drop-down menu
Enter_Skills = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]')))
Enter_Skills.click()
time.sleep(PAUSE)

# Select Education from the Qualification drop-down menu
Enter_Education = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]')))
Enter_Education.click()
time.sleep(PAUSE)

# Select License from the Qualification drop-down menu
Enter_Licenses = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[3]')))
Enter_Licenses.click()
time.sleep(PAUSE)

# Select Languages from the Qualification drop-down menu
Enter_Languages = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[4]')))
Enter_Languages.click()
time.sleep(PAUSE)

# Select Memberships from the Qualification drop-down menu
Enter_Memberships = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[5]')))
Enter_Memberships.click()
time.sleep(PAUSE)

# View Nationalities
Enter_Nationalities = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a')))
Enter_Nationalities.click()
time.sleep(PAUSE)

# Click on Add from Nationalities Page
Enter_Add = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button')))
Enter_Add.click()
time.sleep(PAUSE)

# Click on Records Found from Nationalities Page
Enter_RecordsFound = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]')))
Enter_RecordsFound.click()
time.sleep(PAUSE)

# Click on More Drop-down
Enter_More = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/span')))
Enter_More.click()
time.sleep(PAUSE)

# Click Corporate Branding
Enter_CorporateBranding = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[1]/li')))
Enter_CorporateBranding.click()
time.sleep(PAUSE)

# Click Primary Color from Corporate Branding page
Enter_PrimaryColour = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]')))
Enter_PrimaryColour.click()
time.sleep(PAUSE)

# Click Secondary Color from Corporate Branding page
Enter_SecondaryColor = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]')))
Enter_SecondaryColor.click()
time.sleep(PAUSE)

# Click Primary Front Color from Corporate Branding page
Enter_PrimaryFrontColor = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]')))
Enter_PrimaryFrontColor.click()
time.sleep(PAUSE)

# Click on Secondary Front Color from Corporate Branding page
Enter_SecondaryFrontColor = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]')))
Enter_SecondaryFrontColor.click()
time.sleep(PAUSE)

# Click on Primary Gradient Color 1 from Corporate Branding page
Enter_PrimaryGradientColor1 = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[5]')))
Enter_PrimaryGradientColor1.click()
time.sleep(PAUSE)

# Click on Primary Gradient Color 2 from Corporate Branding page
Enter_PrimaryGradientColor2 = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[6]')))
Enter_PrimaryGradientColor2.click()
time.sleep(PAUSE)

# Click Configuration
Enter_Configuration = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/li/a')))
Enter_Configuration.click()
time.sleep(PAUSE)

# Click Email Configuration from Configuration dropdown Menu
Enter_EmailConfiguration = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/ul/li[1]')))
Enter_EmailConfiguration.click()
time.sleep(PAUSE)

# Click Email Subscriptions from Configuration dropdown Menu
Enter_EmailSubscriptions = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/ul/li[2]')))
Enter_EmailSubscriptions.click()
time.sleep(PAUSE)

# Click localization from Configuration dropdown Menu
Enter_Localization = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/ul/li[3]')))
Enter_Localization.click()
time.sleep(PAUSE)

# Click Language Packages from Configuration dropdown Menu
Enter_LanguagesPackages = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/ul/li[4]')))
Enter_LanguagesPackages.click()
time.sleep(PAUSE)

# Click Modules from Configuration dropdown Menu
Enter_Modules = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/ul/li[5]')))
Enter_Modules.click()
time.sleep(PAUSE)

# Click Social Media Authentication from Configuration dropdown Menu
Enter_SocialMediaAuthentication = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/ul/li[6]')))
Enter_SocialMediaAuthentication.click()
time.sleep(PAUSE)

# Click Register OAuth Client from Configuration dropdown Menu
Enter_RegisterOAuthClient = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/ul/li[7]')))
Enter_RegisterOAuthClient.click()
time.sleep(PAUSE)

# Click LDAP Configuration from Configuration dropdown Menu
Enter_LDAPConfiguration = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/ul/li[8]')))
Enter_LDAPConfiguration.click()
time.sleep(PAUSE)

# Pause for demonstration
time.sleep(PAUSE)

# Close Browser
driver.quit()