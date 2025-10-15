from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#set chrome and launch web page
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/iframes.html")

# --- Switch to iframe using WebElement ---
iframe = driver.find_element(By.ID, "iframe1")
driver.switch_to.frame(iframe)
assert "We Leave From Here" in driver.page_source

time.sleep(5)  # Just to visually see the switch

email_element = driver.find_element(By.ID, "email")
email_element.send_keys("admin@selenium.dev")
email_element.clear()
driver.switch_to.default_content()

# --- Switch to iframe using name or ID ---
iframe1=driver.find_element(By.NAME, "iframe1-name")  # (This line doesn't switch, just locates)
driver.switch_to.frame(iframe1)
assert "We Leave From Here" in driver.page_source

time.sleep(5)  # Just to visually see the switch

email = driver.find_element(By.ID, "email")
email.send_keys("admin@selenium.dev")
email.clear()
driver.switch_to.default_content()

# --- Switch to iframe using index ---
driver.switch_to.frame(0)
assert "We Leave From Here" in driver.page_source

# --- Final page content check ---
driver.switch_to.default_content()
assert "This page has iframes" in driver.page_source

#quit the driver
driver.quit()