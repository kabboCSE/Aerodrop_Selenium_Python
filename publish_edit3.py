import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def publishEdit(driver):
    try:
        # Set up explicit wait
        wait = WebDriverWait(driver, 10)
        # Add a tag (Review & Publish edit)
        tag_selector = "input[placeholder='Add new tag']"
        tag = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, tag_selector)))
        tag.send_keys("test")
        time.sleep(1)  # Replace with the desired tag

        addtag_selector = " (// button[normalize-space() = 'Add'])[1]"
        addtag = wait.until(EC.presence_of_element_located((By.XPATH, addtag_selector)))
        addtag.click()
        time.sleep(1)  # Replace with the desired tag

        tag_selector = "input[placeholder='Add new tag']"
        tag = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, tag_selector)))
        tag.send_keys("test2")
        time.sleep(1)  # Replace with the desired tag

        addtag_selector = " (// button[normalize-space() = 'Add'])[1]"
        addtag = wait.until(EC.presence_of_element_located((By.XPATH, addtag_selector)))
        addtag.click()
        time.sleep(1)  # Replace with the desired tag

        tag_selector = "input[placeholder='Add new tag']"
        tag = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, tag_selector)))
        tag.send_keys("test3")
        time.sleep(1)  # Replace with the desired tag

        addtag_selector = " (// button[normalize-space() = 'Add'])[1]"
        addtag = wait.until(EC.presence_of_element_located((By.XPATH, addtag_selector)))
        addtag.click()
        time.sleep(2)  # Replace with the desired tag

        # description
        description_selector = "(//button[normalize-space()='Description'])[1]"
        description = wait.until(EC.presence_of_element_located((By.XPATH, description_selector)))
        description.click()
        time.sleep(3)  # Replace with the desired tag

        # varients
        variants_selector = "(//button[normalize-space()='Variants'])[1]"
        variants = wait.until(EC.presence_of_element_located((By.XPATH, variants_selector)))
        variants.click()
        time.sleep(1)

        # button
        button_selector = "(//button[@value='on'])[1]"
        button = wait.until(EC.presence_of_element_located((By.XPATH, button_selector)))
        button.click()
        time.sleep(3)

        # images
        images_selector = "(//button[normalize-space()='Images'])[1]"
        images = wait.until(EC.presence_of_element_located((By.XPATH, images_selector)))
        images.click()
        time.sleep(1)

        imagesClick_selector = "(// button[@ id='allImageSelected'])[1]"
        imagesClick = wait.until(EC.presence_of_element_located((By.XPATH, imagesClick_selector)))
        imagesClick.click()
        time.sleep(1)

        #remove
        remove_selector = "(//button[normalize-space()='Remove from My Products'])[1]"
        remove = wait.until(EC.presence_of_element_located((By.XPATH, remove_selector)))
        remove.click()
        time.sleep(2)

        #cancel
        cancel_selector = "(//button[normalize-space()='No, cancel'])[1]"
        cancel = wait.until(EC.presence_of_element_located((By.XPATH, cancel_selector)))
        cancel.click()
        time.sleep(2)
    except Exception as e:
        print(f"publish edit error!: {e}")