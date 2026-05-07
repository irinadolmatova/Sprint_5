from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import MAIN_PAGE_URL


class TestConstructor:
    def test_constructor_bun(self, driver, wait):
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(Locators.SAUCES)).click()
        wait.until(EC.element_to_be_clickable(Locators.BUN)).click()
        assert wait.until(EC.visibility_of_element_located(Locators.SECTION_BUN_ACTIVE))

    def test_constructor_sauces(self, driver, wait):
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(Locators.SAUCES)).click()
        assert wait.until(EC.visibility_of_element_located(Locators.SECTION_SAUCES_ACTIVE))

    def test_constructor_fillings(self, driver, wait):
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(Locators.FILLINGS)).click()
        assert wait.until(EC.visibility_of_element_located(Locators.SECTION_FILLINGS_ACTIVE))
