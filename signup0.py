import time
from selenium.webdriver.common.by import By

def signup(driver):
    try:
        tik_selector = "button[id=':r2fk:-form-item']"
        tik_field = driver.find_element(By.CSS_SELECTOR, tik_selector)
        tik_field.click()
        time.sleep(4)

        CSS_selector = "input[id=':r2fh:-form-item']"
        username_field = driver.find_element(By.CSS_SELECTOR, CSS_selector)
        username_field.send_keys("MD. SHAHRIAR KABBO")  # Replace with the desired email
        time.sleep(4)

        # # Password
        # CSS_selector = "input[type='password']"
        # password_field = driver.find_element(By.CSS_SELECTOR, CSS_selector)
        # password_field.send_keys("123456")  # Replace with the desired password
        # time.sleep(4)
        #
        # # Login Button
        # CSS_selector = "button[type='submit']"
        # login_button = driver.find_element(By.CSS_SELECTOR, CSS_selector)
        # login_button.click()
        # time.sleep(4)

        print("Successfully Signup!")
    except Exception as e:
        print(f"An error occurred during the publishing process: {e}")