import time
from selenium.webdriver.common.by import By

def login(driver):
    try:
        CSS_selector = "input[type='email']"
        username_field = driver.find_element(By.CSS_SELECTOR, CSS_selector)
        username_field.send_keys("singleproductorder@mail.com")  # Replace with the desired email
        time.sleep(4)

        # Password
        CSS_selector = "input[type='password']"
        password_field = driver.find_element(By.CSS_SELECTOR, CSS_selector)
        password_field.send_keys("123456")  # Replace with the desired password
        time.sleep(4)

        # Login Button
        CSS_selector = "button[type='submit']"
        login_button = driver.find_element(By.CSS_SELECTOR, CSS_selector)
        login_button.click()
        time.sleep(4)

        print("Successfully logged in!")
    except Exception as e:
        print(f"An error occurred during logged in: {e}")