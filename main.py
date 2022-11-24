from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# driver.get("https://www.amazon.com/AmazonBasics-Premium-Dual-Monitor-Stand/dp/B00MIBN71I/ref=cs_sr_dp_2?crid=80BFBS7GV3OB&keywords=Amazon%2BBasics%2BDual%2BMonitor&qid=1668398027&sprefix=amazon%2Bbasics%2Bdual%2Bmonitor%2B%2Caps%2C133&sr=8-1&th=1")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# url = driver.find_element(By.XPATH, '/html/body/div/footer/div[2]/div/ul/li[3]/a')
# print(url.get_attribute("href"))

events_links = driver.find_elements(By.CSS_SELECTOR, ".event-widget > div:nth-child(1) > ul:nth-child(3) > li")

event_text = [event.text for event in events_links]
keys = range(len(event_text))
event_dict = dict(list(enumerate(event_text)))
for key, value in event_dict.items():
    event_dict[key] = {"time": value.split("\n")[0],
                       "name": value.split("\n")[1]}

print(event_dict)
# driver.close()
driver.quit()

