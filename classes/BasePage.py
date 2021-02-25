import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from classes.selectors import Selector
from selenium.webdriver.support.ui import Select


class BasePage(Selector):

    def __init__(self, remote):
        self.wd = remote

    @allure.step("Авторизоваться под учетной записью {login}")
    def authorize(self, login='', password=''):
        with allure.step(f"Ввести логин"):
            self.send_keys(self.LOGIN, login)
        with allure.step(f"Ввести пароль"):
            self.send_keys(self.PASSWORD, password)
        with allure.step(f"Авторизоваться"):
            self.click_element(self.BUTTON_LOGIN)

    @allure.step("Создать новый звонок")
    def cr_call(self, name='', descript_call=''):
        with allure.step(f"Создание звонка"):
            with allure.step(f"В меню Create выбрать Create Calls"):
                create_calls = self.find_element(self.CREATE_CALLS)
                href = create_calls.get_attribute('href')
                self.wd.get(href)
            with allure.step(f"Заполнить название звонка"):
                self.send_keys(self.NAME_SUBJECT, name)
            with allure.step(f"Выбрать дату в календаре"):
                open_calendar = self.find_element(self.OPEN_CALENDAR)
                open_calendar.click()
                self.click_element(self.CHOICE_DATE)
            with allure.step(f"Очистить поле Продолжительность часов"):
                self.find_element(self.DURATION_HOURS).clear()
            with allure.step(f"Ввести часы"):
                self.send_keys(self.DURATION_HOURS, "13")
            with allure.step(f"Ввести минуты"):
                input_sort = Select(self.find_element(self.SELECT_DURATION_MINUTES))
                input_sort.select_by_index(3)
            with allure.step(f"Ввести описание звонка"):
                self.send_keys(self.DESCRIPTION, descript_call)
            with allure.step(f"Сохранить звонок"):
                self.click_element(self.SAVE_HEADER)

    @allure.step("Получен элемент {locator}")
    def find_element(self, locator, time=12):
        try:
            return WebDriverWait(self.wd, time).until(EC.presence_of_element_located(locator))
        except AssertionError:
            allure.attach(
                body=self.wd.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError

    @allure.step("Получены элементы {locator}")
    def find_elements(self, locator, time=6):
        try:
            return WebDriverWait(self.wd, time).until(EC.presence_of_all_elements_located(locator))
        except AssertionError:
            allure.attach(
                body=self.wd.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError

    @allure.step("Выполнен клик по элементу {locator}")
    def click_element(self, locator, time=6):
        try:
            WebDriverWait(self.wd, time).until(EC.element_to_be_clickable(locator)).click()
            return self
        except AssertionError:
            allure.attach(
                body=self.wd.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError

    @allure.step("Введен текст '{text}' в элемент {locator}")
    def send_keys(self, locator, text, time=6):
        try:
            WebDriverWait(self.wd, time).until(EC.presence_of_element_located(locator)).send_keys(text)
            return self
        except AssertionError:
            allure.attach(
                body=self.wd.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError