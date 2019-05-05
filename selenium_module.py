from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('card-img-top')
    print('Found {} element with that class name!'.format(elem.tag_name))
except:
    print('Was not able to find an element with that name.')
