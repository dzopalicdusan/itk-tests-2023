import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://10.15.1.204:3000/menu"


meals = {  # number : Meals_name
          1: 'Stuffed veal with pomigrante',
          2: 'Chicken with parsley',
          3: 'Breaded Zuchinni with garlic sauce',
          4: 'Skewered pork with Chives',
          5: 'Mussels with oyster sauce',
          6: 'Catfish with Dragon friit',
          7: 'Mango Chicken',
          8: 'Beef Gozleme',
          9: 'Pancakes with strawberry cream',
          10: 'Stawberry Sudnae',
          11: 'Chocolate Mousse',
          12: 'Malaga Cornetto',
          13: 'Baklava with Vanilla Ice Cream',
        }


def test_3_menu():
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()

    final_price = 0                                 # setting final price of meals to 0
    choice6 = [0]                                   # for while loop we need array that is not empty
    while max(choice6) < 9 or min(choice6) > 8:     # while there are only meals or only desserts in list
        choice6 = random.sample(range(1, 14), 5)    # generate a list of 5 random numbers brom 1 to 13

    choice6.append((random.sample(choice6, 1))[0])  # then we take one of those 5 numbers and repeat it
    choice6.sort()                                  # and sort the list of 6 items

    for i in range(len(choice6)):
        if choice6[i] in [1, 2, 9, 10]:                          # if the item is in upper part of the page
            driver.execute_script("window.scrollBy(0,-2000);")   # scroll all the way up
        elif choice6[i] in [7, 8]:                               # if the item is in bottom part of the page
            driver.execute_script("window.scrollBy(0,2000);")    # scroll all the way down
        else:                                                    # else go the middle part of page
            driver.execute_script("window.scrollBy(0,-2000);")   # by scrolling all the way up
            driver.execute_script("window.scrollBy(0,600);")     # and go down by 600 pixels

        meal = meals[choice6[i]]                                 # getting the name of the meal from meals dict

        cart_previous = driver.find_element(By.ID, 'ukupno').text
        button_xpath = '//h3[text()="{}"]//parent::div//parent::div/following-sibling::button'.format(meal)
        button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, button_xpath)))
        button.click()    # finding and clicking on add button to add a certain meal

        while driver.find_element(By.ID, 'ukupno').text == cart_previous:  # waiting for price in cart to change
            time.sleep(0.2)

        price_xpath = '//h3[text()="{}"]//parent::div//parent::div//following-sibling::div[2]//span'.format(meal)
        price = driver.find_element(By.XPATH, price_xpath).text[1:]    # get the price '$12' and making it to '12'
        final_price += int(price)                                # adding meal price to final price

    assert str(final_price) == driver.find_element(By.ID, 'ukupno').text
