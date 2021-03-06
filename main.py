from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

options = Options()
options.firefox_binary = r'/usr/local/bin/geckodriver'
driver = webdriver.Firefox(options=options)
# driver.get("http://lacoste.ru")

driver.get('https://kiwitaxi.com')
links = driver.find_elements(By.TAG_NAME, "a")

with open('links.txt', 'w') as f:
    for link in links:
        f.write(link.get_attribute('href'))
        f.write('\n')

# assert "Python" in driver.title

# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("ozzy")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

driver.close()
