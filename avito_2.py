from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.avito.ru/ekaterinburg/noutbuki'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='C:\\Users\\dns\\Desktop\\Selenium_py\\ChromeDriver\\chromedriver',
    options=options
)

try:
    url = driver.get(url)
    #print(driver.window_handles)                                          ##window_handles method is used for getting infro about opening windows
    print(f"current url is: {driver.current_url}")
    time.sleep(3)

    items = driver.find_elements(By.XPATH, "//div[@data-marker='item-photo']")
    items[0].click()
    #print(driver.window_handles)
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[1])                      ## switch_to.window allows to switch from window to another one
    time.sleep(5)
    print(f"current url is: {driver.current_url}")

    get_name = driver.find_element(By.XPATH, "//div[@data-marker='seller-info/name']")
    print(f"the seller name is: {get_name.text}")
    time.sleep(5)

    brand = driver.find_element(By.CLASS_NAME, 'style-title-info-main-_sKj0')
    print(f"an offered laptop: {brand.text}")

    price = driver.find_element(By.CLASS_NAME, 'style-item-price-PuQ0I')
    print(f"the price is: {price.text}")
    time.sleep(3)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)

    items[1].click()
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    print(f"current URL is: {driver.current_url}")

    get_name_2 = driver.find_element(By.XPATH, "//div[@data-marker='seller-info/name']")
    print(f"the seller name is: {get_name_2.text}")
    time.sleep(3)

    brand_2 = driver.find_element(By.CLASS_NAME, 'style-title-info-main-_sKj0')
    print(f"an offered laptop: {brand_2.text}")

    price_2 = driver.find_element(By.CLASS_NAME, 'style-item-price-PuQ0I')
    print(f"the price is: {price_2.text}")
    time.sleep(3)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)

    items[3].click()
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[2])
    time.sleep(3)
    print(f"current URL is: {driver.current_url}")


    #driver.close()

    #driver.switch_to.window(driver.window_handles[0])
    #time.sleep(3)

    #items[3].click()
    #time.sleep(3)

    #driver.switch_to.window(driver.window_handles[3])
    #time.sleep(3)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()