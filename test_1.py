from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# User input data:
URL = "http://10.15.1.204:3000/reserve"
ORGANIZER = 'Pera Peric'
CELEBRANT = 'Mika Mikic'
AGE_OF_BP = '2'
DATE = "2023-01-01"  # YYYY-MM-DD format
TIME = "14:01"  # 24hour: HH:MM format
HOW_MANY_PEOPLE = "2-5"  # "6-10" , "11-20" , "21+"
ALLERGIES = ['Wallnuts', 'Chestnuts', 'Fish', 'Meat', 'Shrimp', 'Gluten']


def test_1_organize():
    driver = webdriver.Chrome()
    driver.get(URL)

    organizer_field = WebDriverWait(driver, 5, 1).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'form-control.org')))
    organizer_field.send_keys(ORGANIZER)

    birthday_person_field = driver.find_element(By.CLASS_NAME, 'form-control.bp')
    birthday_person_field.send_keys(CELEBRANT)

    age_of_bp_field = driver.find_element(By.ID, 'age')
    age_of_bp_field.send_keys(AGE_OF_BP)

    when_field = driver.find_element(By.ID, 'date')
    date = DATE.split('-')[2] + DATE.split('-')[1] + DATE.split('-')[0]
    when_field.send_keys(date)

    time_field = driver.find_element(By.ID, 'time')
    hours = TIME.split(':')[0]
    minutes = TIME.split(':')[1]
    pm_or_am = "P" if int(TIME.split(':')[0]) > 11 else "A"
    hours_pm_am = hours if int(hours) < 13 else ('0' + str(int(hours) % 12))[-2:]
    time_pm_am = hours_pm_am + minutes + pm_or_am
    time_field.send_keys(time_pm_am)

    people_field = driver.find_element(By.ID, 'persons')
    people_field.send_keys(HOW_MANY_PEOPLE)
    # clicking the allergies radiobutton
    allergies_yes_button = driver.find_element(By.ID, 'alg_y')
    allergies_yes_button.click()
    allergies_no_button = driver.find_element(By.ID, 'alg_n')
    allergies_no_button.click()
    allergies_maybe_button = driver.find_element(By.ID, 'alg_m')
    allergies_maybe_button.click()
    # checking the allergies checkbox
    allergic_to_walnuts_checkbox = driver.find_element(By.ID, 'alg1')
    if 'Wallnuts' in ALLERGIES:
        allergic_to_walnuts_checkbox.click()
    allergic_to_chestnuts_checkbox = driver.find_element(By.ID, 'alg2')
    if 'Chestnuts' in ALLERGIES:
        allergic_to_chestnuts_checkbox.click()
    allergic_to_fish_checkbox = driver.find_element(By.ID, 'alg3')
    if 'Fish' in ALLERGIES:
        allergic_to_fish_checkbox.click()
    allergic_to_meat_checkbox = driver.find_element(By.ID, 'alg4')
    if 'Meat' in ALLERGIES:
        allergic_to_meat_checkbox.click()
    allergic_to_shrimps_checkbox = driver.find_element(By.ID, 'alg5')
    if 'Shrimp' in ALLERGIES:
        allergic_to_shrimps_checkbox.click()
    allergic_to_gluten_checkbox = driver.find_element(By.ID, 'alg6')
    if 'Gluten' in ALLERGIES:
        allergic_to_gluten_checkbox.click()
    # submit all inputs by clicking on Organize button
    organize_button = driver.find_element(By.CLASS_NAME, 'btn.btn-primary.px-5.py-3')
    organize_button.click()
    # getting the user inputs from Local Storage
    local_storage = driver.execute_script("return window.localStorage;")

    # waiting modal to load and compare the modal output with the user inputs and Local Storage data
    modal_celebrant = WebDriverWait(driver, 5, 1).until(expected_conditions.presence_of_element_located((By.ID, 'cbr')))
    assert modal_celebrant.text == CELEBRANT == local_storage['Birthday_Person']
    assert driver.find_element(By.ID, 'orr').text == ORGANIZER == local_storage['Organizer']
    assert driver.find_element(By.ID, 'agr').text == AGE_OF_BP == local_storage['Age']
    assert driver.find_element(By.ID, 'dtr').text == DATE == local_storage['Date']
    assert driver.find_element(By.ID, 'tmr').text == TIME == local_storage['Time']
    assert driver.find_element(By.ID, 'alr').text == local_storage['alergy']
    assert driver.find_element(By.ID, 'alr').text in ['Yes', 'No', 'Maybe']
    assert ",".join(ALLERGIES) == local_storage['alergies']
