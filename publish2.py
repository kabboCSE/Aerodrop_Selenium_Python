from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def review_and_publish(driver):
    try:
        # Set up explicit wait
        wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for elements to appear

        # Review and Publish
        publish_xpath = "(//button[normalize-space()='Review & Publish'])[1]"
        # Wait until the 'Review & Publish' button is clickable
        publish_button = wait.until(EC.element_to_be_clickable((By.XPATH, publish_xpath)))

        # Click the publish button
        publish_button.click()

        # Wait for a confirmation or completion (optional, adjust based on your app's behavior)
        confirmation_xpath = "//div[contains(text(), 'Successfully reviewed and published')]"
        confirmation = wait.until(EC.presence_of_element_located((By.XPATH, confirmation_xpath)))

        print("Successfully reviewed and published!")
    except Exception as e:
        print(f"An error occurred during the publishing process: {e}")
