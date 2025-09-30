from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://ariregister.rik.ee/est/')

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'company_search'))
)

search_box = driver.find_element(By.ID, 'company_search')
search_box.send_keys('Norstat Eesti AS' + Keys.ENTER)
time.sleep(5)
driver.back()

data_request = driver.find_element(By.XPATH, '//*[contains(text(), "Päringud")]')
data_request.click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[contains(text(), "Detailotsing")]').click()

name = driver.find_element(By.ID, 's__company_name')
name.send_keys('Siim')

accordion_arrows = driver.find_elements(By.CLASS_NAME, 'accordion__arrow')
accordion_arrows[2].click()
print(accordion_arrows[2].text)

time.sleep(5)

country = driver.find_element(By.ID, ' s__address_country')
country.click()
driver.select_by_visible_text('Eesti')

driver.back()

link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Aruande esitamine')
link.click()
driver.back()

"""boxes = driver.find_elements(By.CLASS_NAME, 'quickbtn__image')

print(len(boxes))

for box in boxes:
    box.click()
    time.sleep(10)
    driver.back()
"""

box = driver.find_element(By.XPATH, '//*[contains(text(), "Aruande esitamine")]')
box.click()
driver.find_element(By.XPATH, '//*[contains(text(), "Smart-ID")]').click()
input = driver.find_element(By.ID, 'sid-personal-code')
input.send_keys('39001010015')
input.submit()

time.sleep(10)