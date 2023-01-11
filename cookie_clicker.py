from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")


def purchase_element():
    # Getting current money value in cookies (Exception handling for values that includes ","
    try:
        current_money = int(driver.find_element(By.CSS_SELECTOR, "#money").text)
    except ValueError:
        comma_money = driver.find_element(By.CSS_SELECTOR, "#money").text.split(",")
        current_money = int("".join(comma_money))

    # For element purchase web_element
    xpath_list = ['//*[@id="buyCursor"]', '//*[@id="buyGrandma"]', '//*[@id="buyFactory"]', '//*[@id="buyMine"]',
                  '//*[@id="buyShipment"]', '//*[@id="buyAlchemy lab"]', '//*[@id="buyPortal"]',
                  '//*[@id="buyTime machine"]']
    purchase_list = [driver.find_element(By.XPATH, f"{x}") for x in xpath_list]

    # Finding cost of each purchase element
    prices_list = []
    for element in purchase_list[:-1]:
        try:
            new_element = int(element.text.split(" - ")[1].split("\n")[0])
        except ValueError:
            comma_value = element.text.split(" - ")[1].split("\n")[0].split(",")
            new_element = int("".join(comma_value))
        finally:
            prices_list.append(new_element)

    # Finding name of each purchase element
    elements_names = [element.text.split(" - ")[0] for element in purchase_list[:-1]]

    # Creating a dictionary with all elements found previously (name, cost, purchase element to click)
    purchase_dictionary = {}
    for index in range(len(purchase_list) - 1):
        purchase_dictionary[elements_names[index]] = {"cost": prices_list[index],
                                                      "buy": purchase_list[index]
                                                      }

    # making purchase according to price
    for item_name, item_values in reversed(purchase_dictionary.items()):
        if item_values["cost"] < current_money:
            item_values["buy"].click()


timeout = time.time() + 5  # 5 [seconds]
five_minutes = time.time() + 60 * 5  # 5 [minutes]

while True:
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()

    # after 5 seconds purchase an upgrade
    if time.time() > timeout:
        purchase_element()

    # after 5 minutes
    if time.time() > five_minutes:
        cookies_per_second = driver.find_element(By.XPATH, '//*[@id="cps"]').text
        print(cookies_per_second)
        break
