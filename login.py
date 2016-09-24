from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://hautdebitmobile.orange.fr:8443/home/index')

elem = browser.find_element_by_css_selector('#mwf_choix4')
elem.click()

elem2 = browser.find_element_by_css_selector('#mwf_operators')
elem2.click()

elem3 = browser.find_element_by_css_selector('#operator0 > a:nth-child(1)')
elem3.click()

elem4 = browser.find_element_by_css_selector('#coche6')
elem4.click()

searchElem = browser.find_element_by_css_selector('#loginPartner')
searchElem.send_keys('RNOCH3U')

searchElem2 = browser.find_element_by_css_selector('#passwordPartner')
searchElem2.send_keys('PES2V7181')


elem4 = browser.find_element_by_css_selector('#connectPartner')
elem4.click()

#searchElem.submit();
