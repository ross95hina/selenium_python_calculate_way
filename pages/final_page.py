import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Final_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    id_total_distance = 'totalDistance'
    xpath_text_with_total_price = "//a[contains(text(), 'Возьмите попутчиков через Едем.рф и сэкономьте')]"

    # Values

    value_right_distance = "1595"
    value_right_total_price = "6050"

    # Getters
    def get_total_distance(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.id_total_distance)))

    def get_text_with_total_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_text_with_total_price)))

    # Actions
    def total_distance_value(self):
        return self.get_total_distance()

    def text_with_total_price(self):
        full_text = self.get_text_with_total_price().text
        str_full_text = str(full_text)
        xpath_total_price_value1 = re.findall(r'\d+', str_full_text)
        str_xpath_total_price_value1 = ' '.join(map(str, xpath_total_price_value1))
        return str_xpath_total_price_value1

    # Methods

    def compare_with(self):
        self.assert_word(self.total_distance_value().text, self.value_right_distance)
        self.assert_word(self.text_with_total_price(), self.value_right_total_price)


