from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.litres.ru/'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path='C:\\Users\\dns\\Desktop\\Selenium_py\\ChromeDriver\\chromedriver',
    options=options
)

try:
    url = driver.get(url)
    time.sleep(3)
    #search_input = driver.find_element(By.CLASS_NAME, 'SearchForm-module__input_krNG2')
    #search_input.clear()
    #search_input.send_keys('Ambrose Bierce')
    #time.sleep(5)
    #search_button = driver.find_element(By.CLASS_NAME, 'SearchForm-module__button_zMwhB').click()
    #time.sleep(5)
    enter_but = driver.find_element(By.CLASS_NAME, 'LowerMenu-module__item_3QP99').click()
    time.sleep(5)
    login_but = driver.find_element(By.CLASS_NAME, 'User-module__wrapper_26_f1').click()
    time.sleep(5)
    vk_login = driver.find_element(By.CLASS_NAME, 'AuthorizationPopup-module__socials__link_19A5Y').click()
    time.sleep(5)



    phone_in = driver.find_element(By.CLASS_NAME, 'vkc__TextField__input')
    phone_in.clear()
    phone_in.send_keys('9655195982')
    log_in = driver.find_element(By.CLASS_NAME, 'vkuiButton__in').click()
    time,sleep(45)





except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

