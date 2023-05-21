from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.pro-shooter.ru/collection/kollimatory"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='C:\\Users\\dns\\Desktop\\Selenium_py\\ChromeDriver\\chromedriver',
options=options
)


try:
    url = driver.get(url)                                                   ## .get(url) - for getting url;
    print(f'The current URL is {driver.current_url}')
    time.sleep(3)

    item_1 = driver.find_element(By.CLASS_NAME, 'card-image').click()
    time.sleep(3)

    button_1 = driver.find_element(By.CLASS_NAME, 'btn-wrap').click()
    time.sleep(3)

    button_2 = driver.find_element(By.CLASS_NAME, 'js_link_cart').click()
    time.sleep(3)

    button_3 = driver.find_element(By.CLASS_NAME, 'cart-submit').click()
    time.sleep(4)

    input_1 = driver.find_element(By.CLASS_NAME, 'co-input-field')
    input_1.clear()
    input_1.send_keys('89651787654')
    time.sleep(3)

    input_2 = driver.find_element(By.ID, 'client_surname')
    input_2.clear()
    input_2.send_keys('Максимов')
    time.sleep(4)

    input_3 = driver.find_element(By.ID, 'client_name')
    input_3.clear()
    input_3.send_keys('Сергей')
    time.sleep(4)

    input_4 = driver.find_element(By.ID, 'client_email')
    input_4.clear()
    input_4.send_keys('are-german@mail.com')
    time.sleep(3)

    button_4 = driver.find_element(By.CLASS_NAME, 'co-button').click()
    time.sleep(14)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
