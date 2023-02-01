import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://10.15.1.204:3000/questionaire"
# dictionary with result and meals based on result
recommendations = {0: 'Avocado Benedict', 1: 'Avocado Benedict',
                   2: 'Strawberry Sundae', 3: 'Strawberry Sundae',
                   4: 'Soy Salmon', 5: 'Soy Salmon',
                   6: 'Culiflower Dipper', 7: 'Culiflower Dipper',
                   8: 'Blonde', 9: 'Blonde'}


# 5 different combinations of answers for 5 meals
@pytest.mark.parametrize(
    ('answers', 'recommendation'),
    (
            ([10, 20, 30, 40, 50, 60, 70, 80, 90], 'Avocado Benedict'),
            ([11, 21, 30, 40, 50, 60, 70, 80, 90], 'Strawberry Sundae'),
            ([11, 21, 31, 41, 50, 60, 70, 80, 90], 'Soy Salmon'),
            ([11, 21, 31, 41, 51, 61, 70, 80, 90], 'Culiflower Dipper'),
            ([11, 21, 31, 41, 51, 61, 71, 81, 90], 'Blonde')
    )
)
def test_2_questionaire(answers, recommendation):
    driver = webdriver.Chrome()
    driver.get(URL)

    # selectors for question 1
    leto_sel = driver.find_element(By.ID, 'btn1')
    zima_sel = driver.find_element(By.ID, 'btn2')
    result1 = driver.find_element(By.CLASS_NAME, 'resultText1')
    # selectors for question 2
    caj_sel = driver.find_element(By.ID, 'btn3')
    kafa_sel = driver.find_element(By.ID, 'btn4')
    result2 = driver.find_element(By.CLASS_NAME, 'resultText2')
    # selectors for question 3
    belo_sel = driver.find_element(By.ID, 'btn5')
    crno_sel = driver.find_element(By.ID, 'btn6')
    result3 = driver.find_element(By.CLASS_NAME, 'resultText3')
    # selectors for question 4
    slatko_sel = driver.find_element(By.ID, 'btn7')
    slano_sel = driver.find_element(By.ID, 'btn8')
    result4 = driver.find_element(By.CLASS_NAME, 'resultText4')
    # selectors for question 5
    kiselo_sel = driver.find_element(By.ID, 'btn9')
    ljuto_sel = driver.find_element(By.ID, 'btn10')
    result5 = driver.find_element(By.CLASS_NAME, 'resultText5')
    # selectors for question 6
    kasika_sel = driver.find_element(By.ID, 'btn11')
    viljuska_sel = driver.find_element(By.ID, 'btn12')
    result6 = driver.find_element(By.CLASS_NAME, 'resultText6')
    # selectors for question 7
    duboki_sel = driver.find_element(By.ID, 'btn13')
    plitki_sel = driver.find_element(By.ID, 'btn14')
    result7 = driver.find_element(By.CLASS_NAME, 'resultText7')
    # selectors for question 8
    voce_sel = driver.find_element(By.ID, 'btn15')
    povrce_sel = driver.find_element(By.ID, 'btn16')
    result8 = driver.find_element(By.CLASS_NAME, 'resultText8')
    # selectors for question 9
    koktel_sel = driver.find_element(By.ID, 'btn17')
    pivo_sel = driver.find_element(By.ID, 'btn18')
    result9 = driver.find_element(By.CLASS_NAME, 'resultText9')
    #
    read_my_mind_button = driver.find_element(By.ID, 'readmymind')

    # first number in key is answer number, second number is value od answer
    dict2 = {11: leto_sel, 10: zima_sel,
             21: caj_sel, 20: kafa_sel,
             31: belo_sel, 30: crno_sel,
             41: slatko_sel, 40: slano_sel,
             51: kiselo_sel, 50: ljuto_sel,
             61: kasika_sel, 60: viljuska_sel,
             71: duboki_sel, 70: plitki_sel,
             81: voce_sel, 80: povrce_sel,
             91: koktel_sel, 90: pivo_sel}

    results_list = [result1, result2, result3, result4, result5, result6, result7, result8, result9]

    result = 0
    WebDriverWait(driver, 5, 1).until(expected_conditions.presence_of_element_located((By.ID, 'readmymind')))
    driver.execute_script("window.scrollBy(0, 450);")
    for i in range(9):
        dict2[answers[i]].click()  # from parametrize it is clicking on certain combination of answers
        assert results_list[i].text is not ""  # checking if all 9 answers have result
        if answers[i] % 2 == 1:  # if number is odd
            result += 1  # it will add 1 to result

    read_my_mind_button.click()  # click on button to generate result
    assert recommendation == driver.find_element(By.ID, 'recHeader').text
