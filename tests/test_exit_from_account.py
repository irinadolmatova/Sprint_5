from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from utils import Email_and_Password

class TestExitAccount:
    def test_exit_from_account(self, driver, wait):
        driver.get(Locators.MAIN_PAGE_URL)
        driver.find_element(*Locators.ACCOUNT_ENTER_MAIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Email_and_Password.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Email_and_Password.password)
        driver.find_element(*Locators.ACCOUNT_ENTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.element_to_be_clickable(Locators.EXIT_BUTTON)).click()
        assert wait.until(EC.visibility_of_element_located(Locators.ACCOUNT_ENTER_BUTTON))
