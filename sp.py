from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://wwws.mint.com/login.event')
browser.find_element_by_id('form-login-username').send_keys('')


