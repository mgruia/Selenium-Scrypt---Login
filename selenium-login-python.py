from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("your_chromedriver_file_location/chromedriver.exe")
driver.get('https://COINGECKO.COM')

login = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[3]/div[4]/a/i")
login.click()

email_input = driver.find_element(By.ID, "signInEmail")
email_input.send_keys("name@gmail.com")
email_input.send_keys(Keys.RETURN)

pass_input = driver.find_element(By.ID, "signInPassword")
pass_input.send_keys("Password")

remember = driver.find_element(By.XPATH, '//*[@id="user_remember_me"]')
remember.click()

confirm = driver.find_element(By.ID, "sign-in-button")
confirm.click()

time.sleep(5)

driver.quit()


