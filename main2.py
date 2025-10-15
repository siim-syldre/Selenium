from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

projects = ["DDA156922", "DDA146525"]


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)


driver.get('https://dstsurvey.dk/confirm/authoring/Confirmit.aspx')

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'username'))
)
username = driver.find_element(By.ID, 'username')
username.send_keys('SiimS')

pw = driver.find_element(By.ID, 'password')
pw.send_keys('NorsDST' + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'searchfield'))
)

for project in projects:
    project_search = driver.find_element(By.ID, 'searchfield')
    project_search.clear()
    project_search.send_keys(project + Keys.ENTER)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, '__button_design_inner'))
    )
    time.sleep(2)
    driver.find_element(By.ID, '__button_design_inner').click()
    
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, '__button_proj_exp'))
    )

    driver.find_element(By.ID, '__button_des_exp').click()

    time.sleep(3) 


    iframe = driver.find_elements(By.TAG_NAME, 'iframe')[1]



    time.sleep(2)
    driver.switch_to.frame(iframe)


    email_field = driver.find_element(By.ID, 'RecipientEmail')
    email_field.clear()

    email_field.send_keys("siimyldre@gmail.com")


    submit = driver.find_element(By.ID, 'okbutton')
    submit.click()
    submit.click()

    WebDriverWait(driver, 90).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Task completed")]'))
    )

    submit2 = driver.find_element(By.ID, 'okbutton')
    submit2.click()


    driver.switch_to.default_content()


    driver.find_element(By.ID, '__button_proj_exp').click()
    time.sleep(5)

    iframe2 = driver.find_elements(By.TAG_NAME, 'iframe')[1]

    driver.switch_to.frame(iframe2)

    time.sleep(2)
    """folder = driver.find_element(By.ID, 'chkDisplayFolders')
    folder.click()
    driver.find_element(By.ID, 'chkDisplayEmails').click()
    driver.find_element(By.ID, 'chkDisplayPageSkips').click()
    driver.find_element(By.ID, 'chkDisplayInvitations').click()"""
    driver.find_element(By.ID, 'lstMultiLanguage').click()
    driver.find_element(By.XPATH, '//*[contains(text(), "All languages")]').click()

    submit3 = driver.find_element(By.ID, 'btnExport')
    submit3.click()
    time.sleep(10)
    submit4 = driver.find_element(By.ID, 'hrefCancel').click()
    

    driver.switch_to.default_content()


    

driver.quit()