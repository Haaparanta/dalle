from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

from dotenv import load_dotenv # Load .env file
import os # Load .env file

load_dotenv()


driver = webdriver.Chrome(executable_path='C:\\chromedriver_win32\\chromedriver.exe') # need to install from web

sleep = 1 # seconds

data = 'robot in cyperpunk' # Test data

try:
    driver.get('https://openai.com/api/login/')
    time.sleep(sleep)
    windowsLive = driver.find_element(By.CLASS_NAME, 'cc51749b4').click()
    time.sleep(sleep)
    driver.find_element(By.ID, 'i0116').send_keys(os.environ["email"])
    time.sleep(sleep)
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(sleep)
    driver.find_element(By.ID, 'i0118').send_keys(os.environ["password"])
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(sleep)
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(sleep)
    driver.get('https://labs.openai.com/')
    time.sleep(sleep*5)
    driver.find_elements(By.TAG_NAME, 'input')[0].send_keys(data)
    time.sleep(sleep)
    driver.find_elements(By.CLASS_NAME, 'btn')[2].click() # click on the button to generate image
    time.sleep(sleep*60) # wait for the model to be ready it should be ready in about a 20 seconds, but minute for sure
    print(driver.find_elements(By.TAG_NAME, 'img')[0].get_attribute('src')) # get the image url

except Exception as e:
    print('Error' + e)


