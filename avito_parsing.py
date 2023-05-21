from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.avito.ru/ekaterinburg/noutbuki?cd=1&q=%D0%B8%D0%B3%D1%80%D0%BE%D0%B2%D0%BE%D0%B9+%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='C:\\Users\\dns\\Desktop\\Selenium_py\\ChromeDriver\\chromedriver',
    options=options
)

try:
    url = driver.get(url)
    #print(driver.window_handles)
    print(f"Current url is: {driver.current_url}")
    time.sleep(3)

    #search_1 = driver.find_element(By.XPATH, "//div[@data-marker='catalog-serp']").click()
    #time.sleep(3)

    step_1 = driver.find_element(By.CLASS_NAME, 'iva-item-titleStep-pdebR').click()
    time.sleep(3)
    #print(driver.window_handles)

    driver.switch_to.window(driver.window_handles[1])
    print(f"Current url is: {driver.current_url}")

    get_name_1 = driver.find_element(By.CLASS_NAME, 'style-seller-info-value-vOioL')
    print(f"the seller name is: {get_name_1.text}")
    time.sleep(5)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    step_1[1].click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    get_name_2 = driver.find_element(By.XPATH, "//div[@data-marker='seller-info/name']")
    print(f"the seller name is: {get_name_2.text}")

    #get_price_1 = driver.find_element(By.CLASS_NAME, 'js-item-price style-item-price-text-_w822 text-text-LurtD text-size-xxl-UPhm')
    #print(f"the price is: {get_price_1.text}")

    #get_data = driver.find_element(By.CLASS_NAME, 'style-seller-info-value-vOioL')
    #print(f"the seller is registered by: {get_data.text}")

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()