from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver.get("https://www.python.org")
driver.get("https://www.google.com/")
# driver.implicity_wait(200) # wait 30 seconds
# driver.manage().timeouts().implicitlyWait(160, TimeUnit.SECONDS) # wait time before closing
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()