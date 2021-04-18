'''pip install selenium'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''install chrome driver and save it in program*86'''

PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get('https://www.techwithtim.net/')

search=driver.find_element_by_id("year-link-2020")
search.send_keys("Test")
search.send_keys(Keys.RETURN) 
print(driver.page_source)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles=main.find_elements_by_tag_name("article")
    for article in articles:
        header=article.find_element_by_class_name("entry-summary")
        print(header.text)
        main=driver.find_element_by_id("main")
        print(main.text)

finally:
    driver.quit()

 

time.sleep(5)

driver.quit()
