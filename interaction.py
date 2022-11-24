import selenium.webdriver.common.action_chains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element(By.CSS_SELECTOR, "div#articlecount a")
# print(article_count.text)
# article_count.click()
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email_address = driver.find_element(By.NAME, "email")
sign_up = driver.find_element(By.CSS_SELECTOR, "button")

first_name.send_keys("Victor")
last_name.send_keys("Ponce")
email_address.send_keys("vicmanuelr@gmail.com")
sign_up.click()

