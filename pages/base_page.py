from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BaseUIMethods:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # получение элемента
    def element_presence(self, locator: tuple[str, str], driver: WebDriver, message: str='',
                         waiting_time: int = 10) -> WebElement:
        """
        Функция на поиск элемента на странице
        """
        return WebDriverWait(driver, waiting_time).until(expected_conditions.presence_of_element_located(locator),
                                                         message=message)

