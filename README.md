Selenium  scrypt with Python - login to a web page, with steps ( #comments)

I used locators and XPATH, for Chrome browser, in this example. Any other browser can be used ( like Firefox, Safari, IE), with the correct driver.

driver.maximize_window() #to get a full size screen browser.

Another way to load the driver:
PATH = "your_file_location/chromedriver.exe"
driver = webdriver.Chrome(PATH)
