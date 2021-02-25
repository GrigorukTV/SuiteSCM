import allure


class Tests:

    @allure.title('Создание документа')
    def test_create_documents(self, admin_page):
        """В учетной записи администратора создается новые документ и проверяется, что после сохранения он есть в БД"""
        assert admin_page.create_document() == True

    @allure.title('Создание и удаление таска')
    def test_create_task(self, admin_page):
        """В учетной записи администратора создается, а затем удаляется новый таск."""
        assert admin_page.create_delete_tasks() == True

    @allure.title('Создание и редактирование звонка')
    def test_create_calls(self, admin_page):
        """В учетной записи администратора создается новый звонок,
        в него вносятся изменения. Изменения сохранены"""
        assert admin_page.create_edit_calls() == True

    @allure.title('Создание и удаление поста')
    def test_create_delete_post(self, admin_page):
        """В учетной записи администратора добавляется новый пост и удаляется.
        После удаления пост отсутствует среди записей"""
        assert admin_page.create_delete_post() == 'No Data'

    @allure.title('Загрузка фото в профиль')
    def test_photo_upload(self, admin_page):
        """Загрузка и сохранение изображения в профиль администратора"""
        assert admin_page.upload_photo_profile() == True

    @allure.title('Создание нового пользователя')
    def test_new_user(self, admin_page):
        """В учетной записи администратора создается новый пользователь.
        При попытке авторизоваться под новым пользователем, отображается стартовая страница с настройками"""
        assert admin_page.create_new_user() == 'Welcome to SuiteCRM!'

    @allure.title('Создание и поиск звонка')
    def test_search_call(self, admin_page):
        """Создается новый звонок. При поиске по названию звонка, он отображается в результатах"""
        assert admin_page.search_call() == True

    @allure.title('Импорт списка звонков')
    def test_import_list_call(self, admin_page):
        """В учетной записи администратора выполняется импорт списка звонков"""
        assert admin_page.import_list_call() == '3recordswerecreated'

    @allure.title('Добавление координат в избранные')
    def test_favorites_call(self, admin_page):
        """В учетной записи администратора создается новый звонок и добавляется в избранные.
        После добавления, звонок отображается в разделе Избранные"""
        assert admin_page.favorites_address_cash() == True

    @allure.title('Добавление таска в созданный проект')
    def test_project(self, admin_page):
        """В учетной записи администратора создается новый проект и добавляется новый таск.
        Добавленный таск должен отображаться в таблице тасков """
        assert admin_page.create_project() == 'НОВАЯ ЗАДАЧА'






