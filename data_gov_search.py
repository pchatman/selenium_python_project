from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Set up Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 1. Open data.gov
    driver.get("https://data.gov/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 15)

    # 2. Locate the search box
    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # 3. Enter search text and submit
    search_query = "Supply Chain Greenhouse Gas Emission Factors v1.3 by NAICS-6"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # 4. Wait for search results and click the dataset link
    result_link = wait.until(
        EC.element_to_be_clickable((
            By.PARTIAL_LINK_TEXT,
            "Supply Chain Greenhouse Gas Emission Factors"
        ))
    )

    result_link.click()

    # Optional pause so you can see the page
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
