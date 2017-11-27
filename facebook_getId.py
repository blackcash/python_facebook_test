from selenium import webdriver
import re
import time

fburl = input("please input facebook address : ")
url_web = 'http://lookup-id.com/'
browser = webdriver.Chrome('chromedriver.exe') 
browser.get(url_web)
time.sleep(2)
furl = browser.find_element_by_xpath('//*[@id="input_url"]')
furl.send_keys(fburl)
time.sleep(2)
clickme = browser.find_element_by_xpath('//*[@id="facebook_lookup_botton"]')
clickme.click()
time.sleep(5)
html_code = browser.page_source
#print(html_code)
ma = re.search('<span id="code">(.*?)</span>', html_code)
print(ma.group(1))
browser.quit()