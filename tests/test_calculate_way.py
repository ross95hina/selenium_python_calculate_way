import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.final_page import Final_page
from pages.main_page import Main_page


def test_calculate_way1():
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    print("Start test")
    mp = Main_page(driver)
    mp.calculate_way()
    time.sleep(6)
    fp = Final_page(driver)
    fp.compare_with()
    driver.quit()


