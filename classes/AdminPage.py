import time
import re
import allure
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException
from classes.selectors import Selector
from classes.Browser import Browser
from classes.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pymysql.cursors

connection_db = pymysql.connect(host='192.168.0.13',
                                user='bn_suitecrm',
                                password='',
                                db='bitnami_suitecrm',
                                charset='utf8',
                                port=3308,
                                cursorclass=pymysql.cursors.DictCursor)


class AdminPage(BasePage, Selector):
    filePath = "./tests/test.png"
    filePath_2 = "./tests/import_calls.csv"

    def create_document(self):
        with allure.step(f"Удалить в БД записи с именем 'test.png'"):
            cursor_db = connection_db.cursor()
            cursor_db.execute("DELETE FROM documents WHERE document_name = 'test.png'")
            connection_db.commit()
            cursor_db.close()
        self.authorize('user', 'bitnami')
        with allure.step(f"Создание документа"):
            with allure.step(f"В меню Create выбрать Create Documents"):
                create_doc = self.find_element(self.CREATE_DOCUMENT)
                href = create_doc.get_attribute('href')
                self.wd.get(href)
            with allure.step(f"Загрузить файл"):
                self.find_element(self.DOWNLOAD_FILE_DOC).send_keys(self.filePath)
            with allure.step(f"Ввести текст описания"):
                self.send_keys(self.DESCRIPTION, "Тестовый тест")
            with allure.step(f"Сохранить документ"):
                self.click_element(self.SAVE)
        try:
            cursor_db = connection_db.cursor()
            cursor_db.execute("SELECT * FROM documents WHERE document_name = 'test.png'")
            row = cursor_db.fetchone()
            if row == None:
                return False
            else:
                return True
        finally:
            cursor_db.close()

    def create_delete_tasks(self):
        with allure.step(f"Удалить из таблицы tasks, записи с именем 'Тестовая запись'"):
            cursor_db = connection_db.cursor()
            cursor_db.execute("DELETE FROM `tasks` WHERE `name` = 'Тестовая запись'")
            connection_db.commit()
        self.authorize('user', 'bitnami')
        with allure.step(f"Создание задания"):
            with allure.step(f"В меню Create выбрать Create Tasks"):
                create_task = self.find_element(self.CREATE_TASK)
                href = create_task.get_attribute('href')
                self.wd.get(href)
            with allure.step(f"Заполнить кому назначено задание"):
                self.send_keys(self.ASSIGNED_TO, "Василий")
            with allure.step(f"Заполнить кому назначено задание"):
                self.send_keys(self.DESCRIPTION, "Описание документ")
            with allure.step(f"Выбрать статус"):
                select_status = Select(self.find_element(self.SELECT_STATUS))
                select_status.select_by_index(1)
            with allure.step(f"Заполнить название задания"):
                self.send_keys(self.NAME_SUBJECT, "Тестовая запись")
            with allure.step(f"Сохранить задание"):
                self.click_element(self.SAVE)
        with allure.step(f"Удаление нового таска"):
            with allure.step(f"Открыть вкладку Просмотр заданий"):
                view_task = self.find_element(self.VIEW_TASK)
                view_task.click()
            with allure.step(f"Подсчитать количество заданий, после создания нового таска"):
                count_checkbox = self.find_elements(self.ALL_CHECKBOX)
            with allure.step(f"Выбрать созданный таск"):
                cl = self.find_element(self.CHECKBOX)
                cl.click()
            with allure.step(f"Удалить созданный таск"):
                self.click_element(self.DELETE_TASK)
                self.wd.execute_script(
                    "return sListView.send_mass_update('selected', 'Please select at least 1 record to proceed.', 1)")
                # закрытие аллерта
                self.wd.switch_to_alert().accept()
            with allure.step(f"Подсчитать количество заданий, после удаления таска"):
                count_checkbox_2 = self.find_elements(self.ALL_CHECKBOX)
        # сравнение количества тасков
        if len(count_checkbox) > len(count_checkbox_2):
            return True

    def create_edit_calls(self):
        with allure.step(f"Удалить из таблицы calls, записи с именем 'Тестовая запись', 'Тестовый звонок(перенос времени)'"):
            cursor_db = connection_db.cursor()
            cursor_db.execute("DELETE FROM calls WHERE name = 'Тестовый звонок(перенос времени)'")
            cursor_db.execute("DELETE FROM calls WHERE name = 'Тестовый звонок'")
            connection_db.commit()
        self.authorize('user', 'bitnami')
        self.cr_call('Тестовый звонок', 'Описание звонка')
        with allure.step(f"Редактирование созданного звонка"):
            with allure.step(f"В меню Actions выбрать редактировать"):
                self.click_element(self.MENU_ACTIONS)
                self.click_element(self.ACTION_EDIT)
            with allure.step(f"Отредактировать название и время (часы)"):
                self.find_element(self.NAME_SUBJECT).clear()
                self.send_keys(self.NAME_SUBJECT, "Тестовый звонок(перенос времени)")
                input_sort2 = Select(self.find_element(self.SELECT_DURATION_MINUTES))
                input_sort2.select_by_index(1)
            with allure.step(f"Сохранить изменения"):
                    self.click_element(self.SAVE_HEADER)
        # проверка, что изменения сохранились в БД
        try:
            cursor_db = connection_db.cursor()
            cursor_db.execute(
                "SELECT * FROM calls WHERE name = 'Тестовый звонок(перенос времени)' AND duration_hours = 13 AND duration_minutes=15")
            row = cursor_db.fetchone()
            if row == None:
                return False
            else:
                return True
        finally:
            cursor_db.close()

    def create_delete_post(self):
        self.authorize('user', 'bitnami')
        with allure.step(f"Ввести текст для поста"):
            self.send_keys(self.TEXT_POST, 'Хорошая погода')
        with allure.step(f"Опубликовать пост"):
            self.click_element(self.BUTTON_POST)
        with allure.step(f"Удалить пост"):
            post_deleted = self.find_elements(self.BUTTON_DELETED)
            post_deleted[1].click()
        # проверка, что пост удален
        search_records = self.find_element(self.NO_DATA).get_attribute('innerHTML')
        return search_records

    def upload_photo_profile(self):
        self.authorize('user', 'bitnami')
        with allure.step(f"Перейти в профиль администратора"):
            profile = self.find_element(self.PROFILE)
            href = profile.get_attribute('href')
            self.wd.get(href)
        with allure.step(f"Проверить, что изображение не загружено, если да - удалить его"):
            button_mapping = self.find_element(self.REMOVE).is_displayed()
            if button_mapping == True:
                self.click_element(self.REMOVE)
        with allure.step(f"Загрузить изображение"):
            self.find_element(self.PHOTO_FILE_DOWNLOAD).send_keys(self.filePath)
        with allure.step(f"Сохранить изменения"):
            self.click_element(self.SAVE_HEADER)
        # проверка, что фото загружено
        photo_profile = self.find_element(self.PHOTO).get_attribute('src')
        if photo_profile == None:
            return False
        else:
            return True

    def create_new_user(self):
        with allure.step(f"Удалить таблице users записи с именем User_test'"):
            cursor_db = connection_db.cursor()
            cursor_db.execute("DELETE FROM users WHERE user_name = 'User_test'")
            connection_db.commit()
        self.authorize('user', 'bitnami')
        with allure.step(f"Перейти в профиль администратора"):
            profile = self.find_element(self.PROFILE)
            href = profile.get_attribute('href')
            self.wd.get(href)
        with allure.step(f"Создать нового пользователя"):
            with allure.step(f"В боковом меню выбрать Create New User"):
                create_new_user = self.find_element(self.CREATE_NEW_USER)
                create_new_user.click()
            with allure.step(f"Ввести имя"):
                self.send_keys(self.SEND_USER_NAME, 'User_test')
            with allure.step(f"Ввести фамилию"):
                self.send_keys(self.LAST_NAME, 'Test')
            with allure.step(f"Перейти на вкладку Password. Ввести пароль, повторить ввод пароля"):
                self.click_element(self.PASSWORD_TAB)
                self.send_keys(self.NEW_PASSWORD, 'User')
                self.send_keys(self.CONFIRM_PASSWORD, 'User')
            with allure.step(f"Сохранить данные"):
                self.click_element(self.SAVE_FOOTER)
                # закрытие всплывающего окна
                window_name_2 = self.wd.window_handles[1]
                w = self.wd.switch_to.window(window_name_2)
                self.wd.close()
                window_name_1 = self.wd.window_handles[0]
                w = self.wd.switch_to.window(window_name_1)
        with allure.step(f"Выйти из учетной записи администратора"):
            profile = self.find_element(self.LOGOUT)
            href = profile.get_attribute('href')
            self.wd.get(href)
        with allure.step(f"Авторизоваться под новым пользователем"):
            self.authorize('User_test', 'User')
        h2 = self.find_element(self.H2)
        # проверка, что при входе в учетную запись, отображается окно настроек
        heading = h2.get_attribute('innerHTML')
        return heading

    def search_call(self):
        with allure.step(f"Удалить из таблицы calls, записи с именем 'Test call'"):
            cursor_db = connection_db.cursor()
            cursor_db.execute("DELETE FROM calls WHERE name = 'Test call'")
            connection_db.commit()
        self.authorize('user', 'bitnami')
        self.cr_call('Test call', 'Описание звонка')
        with allure.step(f"Нажать на поиск"):
            click_search_button = self.find_element(self.CLICK_SEARCH_BUTTON)
            click_search_button.click()
        with allure.step(f"В появившейся поисковой строке ввести название созданного звонка"):
            search = self.find_element(self.INPUT_REQUEST)
            search.send_keys("Test call")
        with allure.step(f"Нажать на поиск"):
            self.click_element(self.CLICK_BUTTON_LOUPE)
        # сравнение результатов поиска
        list_results = self.find_elements(self.SEARCH_RESULTS)
        for i in list_results:
            if i.get_attribute('innerHTML') == 'Test call':
                return True
            else:
                return False

    def import_list_call(self):
        with allure.step(f"Удалить из таблицы calls, записи с именем 'Test call_1', 'Test call_2', 'Test call_3'"):
            cursor_db = connection_db.cursor()
            cursor_db.execute("DELETE FROM calls WHERE name = 'Test_call_1'")
            cursor_db.execute("DELETE FROM calls WHERE name = 'Test_call_2'")
            cursor_db.execute("DELETE FROM calls WHERE name = 'Test_call_3'")
            connection_db.commit()
        self.authorize('user', 'bitnami')
        with allure.step(f"В горизонтальном меню выбрать Calls"):
            self.click_element(self.MENU_ACTIV)
            self.click_element(self.MENU_ACTIV_CALLS)
        with allure.step(f"Открыть импорт звонков"):
            self.click_element(self.IMPORT_CALL_BUTTON)
        with allure.step(f"Выбрать файл для импорта"):
            self.find_element(self.USER_FILE).send_keys(self.filePath_2)
        with allure.step(f"Для выполнения импорта нажимать Next и Import Now"):
            self.click_element(self.NEXT)
            self.click_element(self.NEXT)
            self.click_element(self.NEXT)
            self.click_element(self.CLICK_BUTTON_IMPORT_NOW)
        # получение текста сообщения об успешном импорте
        message = self.find_element(self.RESULT_MESSAGE).get_attribute('innerHTML')
        message = message.replace("&nbsp;", " ").replace("<b>", "").replace("</b>", '').replace("<br>", '')
        message = re.sub(r"\W", '', message)
        return message

    def favorites_address_cash(self):
        with allure.step(f"Удалить из таблицы jjwg_address_cache, записи с именем 'ADDRESS'"):
            cursor_db = connection_db.cursor()
            cursor_db.execute("DELETE FROM jjwg_address_cache WHERE name = 'ADDRESS'")
            connection_db.commit()
        self.authorize('user', 'bitnami')
        with allure.step(f"В меню Create выбрать Maps Address Cach"):
            self.click_element(self.MENU_ALL)
            self.click_element(self.MENU_ALL_MAPS_ADDR_CACHE)
            self.click_element(self.CREATE_ADDRESS_CACHE)
        with allure.step(f"Ввести название"):
            self.send_keys(self.NAME_SUBJECT, 'ADDRESS')
        with allure.step(f"Ввести координаты"):
            self.send_keys(self.LAT, '54.721281')
            self.send_keys(self.LNG, '55.945486')
        with allure.step(f"Сохранить изменения"):
            self.click_element(self.SAVE)
        with allure.step(f"Добавить созданный адрес в избранные"):
            self.click_element(self.ADD_FAVORITES)
            self.wd.refresh()
        list_results = self.find_elements(self.LIST_FAVORITES)
        for i in list_results:
            if i.get_attribute('innerHTML') == 'ADDRESS':
                return True
        return False

    def create_project(self):
        with allure.step(f"Удалить из таблицы project, записи с именем 'НОВЫЙ ПРОЕКТ'/n"
                         f" Удалить из таблицы project_task, записи с именем 'НОВАЯ ЗАДАЧА'"):
            cursor_db = connection_db.cursor()
            cursor_db.execute("DELETE FROM project WHERE name = 'НОВЫЙ ПРОЕКТ'")
            cursor_db.execute("DELETE FROM project_task WHERE name = 'НОВАЯ ЗАДАЧА'")
            connection_db.commit()
            connection_db.close()
        self.authorize('user', 'bitnami')
        with allure.step(f"Создать новый проект"):
            with allure.step(f"В меню COLLABORATION выбрать PROJECT и открыть создание проекта"):
                self.click_element(self.COLLABORATION)
                self.click_element(self.COLLABORATION_PROJECT)
                self.click_element(self.CREATE_PROJECT)
            with allure.step(f"Ввести название, дату начала и дату окончания"):
                self.send_keys(self.NAME_SUBJECT, "НОВЫЙ ПРОЕКТ")
                self.send_keys(self.DATE_START, "03/03/2021")
                self.send_keys(self.DATE_END, "05/03/2021")
            with allure.step(f"Сохранить изменения"):
                self.click_element(self.SAVE_HEADER)
        self.click_element(self.ADD_NEW_TASK)
        with allure.step(f"Для нового проекта добавить таск"):
            with allure.step(f"Ввести название, дату начала и сохранить изменения"):
                self.send_keys(self.TASK_NAME, "НОВАЯ ЗАДАЧА")
                self.send_keys(self.START, "03/04/2021")
                self.wd.find_element_by_xpath("/html/body/div[4]/div[11]/div/button[1]").click()
        # проверка, что в таблице добавлен таск
        elem = self.find_element(self.TABLE_TASK).get_attribute('innerHTML')
        return elem