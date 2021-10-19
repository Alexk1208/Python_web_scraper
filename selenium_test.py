from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

#added default path using executable_path
driver = webdriver.Chrome(executable_path=r'C:\Users\Alex\Downloads\chromedriver.exe')

url = 'http://the-internet.herokuapp.com/dynamic_loading/2'

driver.get(url)

driver.find_element_by_xpath('//*[@id="start"]/button').click()

driver.implicitly_wait(10)

text = driver.find_element_by_xpath('//*[@id="finish"]/h4').text

print(text)
