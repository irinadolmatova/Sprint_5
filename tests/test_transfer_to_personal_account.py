from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from utils import Email_and_Password

class TestEntrance:
    #Тест на проверку перехода в личный кабинет при условии авторизованного пользователя
    def test_entrance_account_authorized(self, driver, wait):
        driver.get(Locators.MAIN_PAGE_URL)
        driver.find_element(*Locators.ACCOUNT_ENTER_MAIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Email_and_Password.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Email_and_Password.password)
        driver.find_element(*Locators.ACCOUNT_ENTER_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.CANCEL_BUTTON))

    #Тест на проверку перехода в личный кабинет при неавторизованном пользователе
    def test_entrance_not_authorized(self, driver, wait):
        driver.get(Locators.MAIN_PAGE_URL)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.ACCOUNT_ENTER_BUTTON))