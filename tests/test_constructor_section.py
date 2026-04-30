from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestConstructor:
    def test_constructor_bun(self, driver, wait):
        driver.get(Locators.MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(Locators.SAUCES)).click()
        wait.until(EC.element_to_be_clickable(Locators.BUN)).click()
        wait.until(EC.text_to_be_present_in_element_attribute(Locators.BUN, "class", "tab_tab_type_current"))
        current_tab = driver.find_element(*Locators.BUN).get_attribute("class")
        assert "tab_tab_type_current" in current_tab

    def test_constructor_sauces(self, driver, wait):
        driver.get(Locators.MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(Locators.SAUCES)).click()
        wait.until(EC.text_to_be_present_in_element_attribute(Locators.SAUCES, "class", "tab_tab_type_current"))
        current_tab = driver.find_element(*Locators.SAUCES).get_attribute("class")
        assert "tab_tab_type_current" in current_tab

    def test_constructor_fillings(self, driver, wait):
        driver.get(Locators.MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(Locators.FILLINGS)).click()
        wait.until(EC.text_to_be_present_in_element_attribute(Locators.FILLINGS, "class", "tab_tab_type_current"))
        current_tab = driver.find_element(*Locators.FILLINGS).get_attribute("class")
        assert "tab_tab_type_current" in current_tab
