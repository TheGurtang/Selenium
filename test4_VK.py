from selenium import webdriver
from selenium.webdriver.common.by import By                          ## it is important to import this, outherwise a finding of elements will be impossible
import time


url = 'https://vk.com/'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path='C:\\Users\\dns\\Desktop\\Selenium_py\\ChromeDriver\\chromedriver',
    options=options
)



try:
    driver.get(url)
    time.sleep(3)
    email_input = driver.find_element(By.ID, "index_email")
    email_input.clear()
    email_input.send_keys('89655195982')
    time.sleep(3)

    #pass_input = driver.find_element(By.ID, 'index_pass')
    #pass_input.clear()
    #pass_input.send_keys('1a3a7a9a')
    #time.sleep(5)

    login_button = driver.find_element(By.CLASS_NAME, 'JoinForm__form').click()
    time.sleep(5)

    id_input = driver.find_element(By.CLASS_NAME, 'vkc__TextField__input')
    id_input.clear()
    id_input.send_keys('9655195982')
    time.sleep(5)

    pass_in = driver.find_element(By.CLASS_NAME, 'vkuiButton__in').click()
    time.sleep(5)


except Exception as ex:
    print(ex)


finally:
    driver.close()
    driver.quit()