from selenium import webdriver


option=webdriver.ChromeOptions()
option.add_argument("headless")
driver=webdriver.Chrome(chrome_options=option)
driver.get("https://baidu.com")
print(driver.title)