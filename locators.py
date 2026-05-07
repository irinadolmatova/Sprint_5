from selenium.webdriver.common.by import By

class Locators:
    #Поле ввода имени
    NAME_INPUT=(By.XPATH, ".//label[text()='Имя']/..//input")
    #Поле ввода Email
    EMAIL_INPUT=(By.XPATH, ".//label[text()='Email']/..//input")
    #Поле ввода пароля
    PASSWORD_INPUT=(By.XPATH, ".//label[text()='Пароль']/..//input")
    #Кнопка Зарегистрироваться
    REGISTRATION_BUTTON=(By.XPATH, ".//button[text()='Зарегистрироваться']")
    #Кнопка Войти
    ACCOUNT_ENTER_BUTTON=(By.XPATH, ".//button[text()='Войти']")
    #Кнопка Войти в аккаунт на главной
    ACCOUNT_ENTER_MAIN_BUTTON=(By.XPATH, ".//button[text()='Войти в аккаунт']")
    #Кнопка Оформить заказ
    ORDER_BUTTON=(By.XPATH, ".//button[text()='Оформить заказ']")
    #Кнопка личный кабинет на главной странице
    PERSONAL_ACCOUNT_BUTTON=(By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")
    #Кнопка Восстановить пароль
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")
    #Кнопка Войти на форме регистрации и восстановление пароля
    ENTER_ACCOUNT_REGISTRATION_BUTTON=(By.XPATH, ".//a[text()='Войти']")
    #Сообщение о некорректном пароле
    MESSAGE_UNCORRECT=(By.XPATH, ".//p[contains(text(),'Некорректный пароль')]")
    #Кнопка Отмена при переходе в личный кабинет
    CANCEL_BUTTON=(By.XPATH, ".//button[text()='Отмена']")
    #Кнопка Конструктор
    CONSTRUCTOR_BUTTON=(By.XPATH, ".//p[text()='Конструктор']")
    #Заголовок Соберите бургер
    HEADER_BURGER=(By.XPATH, ".//h1[text()='Соберите бургер']")
    #Кнопка Выход
    EXIT_BUTTON=(By.XPATH, ".//button[text()='Выход']")
    #Кнопка Булки
    BUN=(By.XPATH, "//span[text()='Булки']")
    #Кнопка Соусы
    SAUCES=(By.XPATH, "//span[text()='Соусы']")
    #Кнопка Начинки 
    FILLINGS=(By.XPATH, "//span[text()='Начинки']")
    #Выбран раздел "Булки"
    SECTION_BUN_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Булки']]")
    #Выбран раздел "Соусы"
    SECTION_SAUCES_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Соусы']]")
    #Выбран раздел "Начинки"
    SECTION_FILLINGS_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Начинки']]")
    