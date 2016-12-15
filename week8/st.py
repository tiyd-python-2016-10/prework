from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://google.com/')
#browser.get('http://www.theironyard.com/')

assert 'Google' in browser.title

from selenium.webdriver.common.keys import Keys
search_input = browser.find_element_by_name('q')
search_input.send_keys('kittens' + Keys.RETURN)

browser.quit()
