from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):
    url = "https://www.avtodispetcher.ru/distance/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    name_from = 'from'
    name_to = 'to'
    name_fuel_consumption = 'fc'
    name_fuel_price = 'fp'
    xpath_calculate = "//input[@value='Рассчитать']"
    reminder_xpath = "//a[@aria-label='dismiss cookie message']"

    # Values
    value_from = "Уфа"
    value_to = "Ржев"
    value_fuel_consumption = "7.6"
    value_fuel_price = "50"

    # Getters
    def get_from(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, self.name_from)))

    def get_to(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, self.name_to)))

    def get_fuel_consumption(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, self.name_fuel_consumption)))

    def get_fuel_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, self.name_fuel_price)))

    def get_calculate(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xpath_calculate)))

    def get_close_reminder(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reminder_xpath)))


    # Actions
    def input_from(self):
        self.get_from().send_keys(self.value_from)
        print("input value from")

    def input_to(self):
        self.get_to().send_keys(self.value_to)
        print("input value from")

    def input_fuel_consumption(self):
        self.get_fuel_consumption().clear()
        self.get_fuel_consumption().send_keys(self.value_fuel_consumption)
        print("input value fuel consumption")

    def input_fuel_price(self):
        self.get_fuel_price().clear()
        self.get_fuel_price().send_keys(self.value_fuel_price)
        print("input value fuel price")

    def close_reminder(self):
        self.get_close_reminder().click()

    def click_calculate(self):
        self.get_calculate().click()
        print("Click calculate")

    # Methods

    def calculate_way(self):
        self.driver.get(self.url)
        self.input_from()
        self.input_to()
        self.input_fuel_consumption()
        self.input_fuel_price()
        self.close_reminder()
        self.click_calculate()


