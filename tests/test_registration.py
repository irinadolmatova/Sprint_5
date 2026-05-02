from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from utils import generate_email, generate_password
from URL import REGISTER_URL

class TestRegistrationAccount:
    def test_successful_registration(self, driver, wait):
        driver.get(REGISTER_URL)
        test_email = generate_email()
        test_password = generate_password()
        driver.find_element(*Locators.NAME_INPUT).send_keys('Irina')
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.ACCOUNT_ENTER_BUTTON))
    

    def test_invalid_password_registration(self, driver, wait):
        driver.get(REGISTER_URL)
        test_email = generate_email()
        invalid_password = '1234'
        driver.find_element(*Locators.NAME_INPUT).send_keys('Irina')
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(invalid_password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.MESSAGE_UNCORRECT))

