from selenium.webdriver.common.by import By

class ConstructorLocator:
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/' and p[text()='Конструктор']]") # Ссылка на конструктор
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип Stellar Burgers

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")  # Вкладка Булки
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Вкладка Соусы
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Вкладка Начинки
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]")  # Активная вкладка