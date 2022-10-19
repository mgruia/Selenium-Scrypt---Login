from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#load chrome(or other OS driver)
driver = webdriver.Chrome("your_chromedriver_file_location/chromedriver.exe")
#access the desired link
driver.get('https://COINGECKO.COM')

#locate the login button/menu with XPATH
login = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[3]/div[4]/a/i")
#press the login button
login.click()

#locate the username field by ID(with Inspect or F12)
email_input = driver.find_element(By.ID, "signInEmail")

#enter your username
email_input.send_keys("name@gmail.com")

#hit Enter
email_input.send_keys(Keys.RETURN)


#locate the password field by ID(with Inspect or F12)
pass_input = driver.find_element(By.ID, "signInPassword")

#enter your password
pass_input.send_keys("Password")

#locate the Remember me box by XPATH
remember = driver.find_element(By.XPATH, '//*[@id="user_remember_me"]')

#click the Remember me box
remember.click()

#locate the Sign in button by ID ( Inspect or F12)
confirm = driver.find_element(By.ID, "sign-in-button")

#Press the button
confirm.click()

#suspends execution for a n number of seconds ( 5, in our example)
time.sleep(5)

#kill browser
driver.quit()


