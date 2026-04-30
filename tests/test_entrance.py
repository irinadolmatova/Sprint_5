from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from utils import Email_and_Password

class TestAccountEnter:
    def test_enter_account_button(self, driver, wait):
        driver.get(Locators.MAIN_PAGE_URL)
        driver.find_element(*Locators.ACCOUNT_ENTER_MAIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Email_and_Password.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Email_and_Password.password)
        driver.find_element(*Locators.ACCOUNT_ENTER_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    def test_enter_personal_account_button(self, driver, wait):
        driver.get(Locators.MAIN_PAGE_URL)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Email_and_Password.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Email_and_Password.password)
        driver.find_element(*Locators.ACCOUNT_ENTER_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    def test_enter_from_registration(self, driver, wait):
        driver.get(Locators.REGISTER_URL)
        driver.find_element(*Locators.ENTER_ACCOUNT_REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Email_and_Password.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Email_and_Password.password)
        driver.find_element(*Locators.ACCOUNT_ENTER_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
    
    def test_enter_from_recovery(self, driver, wait):
        driver.get('https://stellarburgers.education-services.ru/forgot-password')
        driver.find_element(*Locators.ENTER_ACCOUNT_REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Email_and_Password.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Email_and_Password.password)
        driver.find_element(*Locators.ACCOUNT_ENTER_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        