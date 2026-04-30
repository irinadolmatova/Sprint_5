from selenium.webdriver.common.by import By

class Locators:
    #Ссылка на главную страницу
    MAIN_PAGE_URL = "https://stellarburgers.education-services.ru/"
    #Ссылка на страницу регистрации
    REGISTER_URL = "https://stellarburgers.education-services.ru/register"
    #Поле ввода имени
    NAME_INPUT=(By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    #Поле ввода Email
    EMAIL_INPUT=(By.XPATH, ".//label[text()='Email']/following-sibling::input")
    #Поле ввода пароля
    PASSWORD_INPUT=(By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
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
    BUN=(By.XPATH, ".//span[text()='Булки']/parent::div")
    #Кнопка Соусы
    SAUCES=(By.XPATH, ".//span[text()='Соусы']/parent::div")
    #Кнопка Начинки 
    FILLINGS=(By.XPATH, ".//span[text()='Начинки']/parent::div")
    