# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('http://inventwithpython.com')
# try:
#     elem = browser.find_element_by_class_name('card-img-top')
#     print('Found {} element with that class name!'.format(elem.tag_name))
# except:
#     print('Was not able to find an element with that name.')

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('http://inventwithpython.com')
# link_element = browser.find_elements_by_link_text('More Info')
# print(type(link_element))
# link_element[5].click()

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://mail.yahoo.com')
# email_element = browser.find_element_by_id('login-username')
# email_element.send_keys('not_my_real_email')
# password_element = browser.find_element_by_id('login-passwd')
# password_element.send_keys('12345')
# password_element.submit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://nostarch.com')
html_element = browser.find_element_by_tag_name('html')
html_element.send_keys(Keys.END)
html_element.send_keys(Keys.HOME)
