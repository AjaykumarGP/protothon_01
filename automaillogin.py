
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


browser = webdriver.Chrome(ChromeDriverManager().install())



browser.get('http://gmail.com')
time.sleep(10)
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('ajaykumar.16cs@kct.ac.in')
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(5)
passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys('******')
signinButton = browser.find_element_by_id('passwordNext')
signinButton.click()
print("logged in")