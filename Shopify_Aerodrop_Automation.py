import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from publish2 import review_and_publish  # Import the function from publish2.py
from login1 import login  # Import the function from login1.py
from publish_edit3 import publishEdit



def shopify_aerodrop_automation():
    # Set up the WebDriver
    driver = webdriver.Chrome()

    # Maximize the browser window
    driver.maximize_window()

    # Set up explicit wait
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for elements to appear

    # Open the target URL
    url = "https://app.ibos.io/login"
    driver.get(url)

    # Login
    login(driver)

    # Find Products
    findproduct_xpath = "//span[normalize-space()='Find Products']"
    findproduct = wait.until(EC.element_to_be_clickable((By.XPATH, findproduct_xpath)))
    findproduct.click()

    # Click the dropdown button
    dropdown_xpath = "(//*[name()='svg'][@class='lucide lucide-chevron-down h-4 w-4 opacity-50'])[2]"
    dropdown_field = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
    dropdown_field.click()

    # Select "Athletic Shorts"
    Athletic_xpath = "//span[text()='Athletic Shorts']"
    Athletic_field = wait.until(EC.element_to_be_clickable((By.XPATH, Athletic_xpath)))
    actions = ActionChains(driver)
    actions.move_to_element(Athletic_field).perform()
    Athletic_field.click()

    # Scroll to a specific element
    target_element_CSS = "img[alt='SAINT Shorts Men Women High Street Summer Wash Water Make Old Rivets Casual Sports Shorts Y2k']"
    target_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, target_element_CSS)))
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", target_element)

    # Hover over the image
    actions.move_to_element(target_element).perform()

    # Click the image
    imgClick_css = "img[alt='SAINT Shorts Men Women High Street Summer Wash Water Make Old Rivets Casual Sports Shorts Y2k']"
    imgClick = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, imgClick_css)))
    imgClick.click()
    time.sleep(2)
    # Add to Draft or Remove from Draft
    draft_xpath = "//button[normalize-space()='Add to Draft']"
    removedraft_xpath = "//button[normalize-space()='Remove from Draft']"

    try:
        if driver.find_elements(By.XPATH, draft_xpath):
            draft = driver.find_element(By.XPATH, draft_xpath)
            draft.click()
            time.sleep(2)
        elif driver.find_elements(By.XPATH, removedraft_xpath):
            removedraft = driver.find_element(By.XPATH, removedraft_xpath)
            removedraft.click()
            time.sleep(2)
            # After removing, add to draft again
            if driver.find_elements(By.XPATH, draft_xpath):
                draft = driver.find_element(By.XPATH, draft_xpath)
                draft.click()
                time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")

    # Navigate to Draft Products
    draftProducts_css = "a[href='/dashboard/draft-products']"
    draftProducts = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, draftProducts_css)))
    draftProducts.click()

    # Review and Publish

    review_and_publish(driver)
    publishEdit(driver)



    # Close the browser


if __name__ == "__main__":
    shopify_aerodrop_automation()

