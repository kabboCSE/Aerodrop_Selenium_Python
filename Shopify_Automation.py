import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# Set up the WebDriver with webdriver-manager
service = Service(ChromeDriverManager().install())  # Automatically installs and manages the ChromeDriver
driver = webdriver.Chrome(service=service)  # Pass the service to the Chrome WebDriver
# Open the target URL
url = "https://admin.shopify.com/store/sayed-test/apps/sayed-personalizer"
driver.get(url)
time.sleep(4)

# username_xpath = "//input[@id='account_email']"
# username_field = driver.find_element(By.XPATH, username_xpath)
# username_field.send_keys("kabbo@ibos.io")  # Replace with the desired username
# time.sleep(4)

#Google_Button

google_xpath = "//div[@class='login-card ']//a[3]"
google = driver.find_element(By.XPATH, google_xpath)
google.click()
time.sleep(4)

#Email
email_xpath = "//input[@id='identifierId']"
email_field = driver.find_element(By.XPATH, email_xpath)
email_field.send_keys("kabbo@ibos.io")  # Replace with the desired username
time.sleep(4)

#Password
#//input[@name='Passwd']
pass_xpath = "//input[@id='account_email']"
pass_field = driver.find_element(By.XPATH, pass_xpath)
pass_field.send_keys("00786196Kabbo@")  # Replace with the desired username
time.sleep(4)
