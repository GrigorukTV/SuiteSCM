from selenium.webdriver.common.by import By


class Selector:
    LOGIN = (By.CSS_SELECTOR, "#user_name")
    PASSWORD = (By.CSS_SELECTOR, "#username_password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "#bigbutton")
    SELECT_STATUS = (By.CSS_SELECTOR, "#status")
    CHECKBOX = (By.CSS_SELECTOR, ".oddListRowS1 > td  input[type='checkbox']")
    SUBJECT = (By.CSS_SELECTOR, ".oddListRowS1 > td:nth-child(4) a")
    ACTION_EDIT = (By.CSS_SELECTOR, "#tab-actions ul > li:nth-child(1) > #edit_button")
    TEXT_POST = (By.CSS_SELECTOR, "#text")
    BUTTON_DELETED = (By.CSS_SELECTOR, "#dashletPanel .oddListRowS1 .byLineBox > .byLineRight a")
    NO_DATA = (By.CSS_SELECTOR, "#dashletPanel .oddListRowS1 td  em")
    USER = (By.CSS_SELECTOR, "#with-label")
    PROFILE = (By.CSS_SELECTOR, "#globalLinks ul > li:first-child a")
    ADMIN = (By.CSS_SELECTOR, "#globalLinks ul > li:nth-child(3) a")
    LOGOUT = (By.CSS_SELECTOR, "#globalLinks ul > li:nth-child(6) a")
    PHOTO_FILE_DOWNLOAD = (By.CSS_SELECTOR, "#photo_file")
    PHOTO = (By.CSS_SELECTOR, "#photo > img")
    CREATE_NEW_USER = (By.CSS_SELECTOR, "#actionMenuSidebar ul > li:nth-child(2) a > .actionmenulink")
    SEND_USER_NAME = (By.CSS_SELECTOR, "#user_name")
    LAST_NAME = (By.CSS_SELECTOR, "#last_name")
    PASSWORD_TAB = (By.CSS_SELECTOR, "#tab2")
    NEW_PASSWORD = (By.CSS_SELECTOR, "#new_password")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#confirm_pwd")
    H2 = (By.CSS_SELECTOR, "h2")
    CLICK_SEARCH_BUTTON = (By.CSS_SELECTOR, "#ajaxHeader .desktop-bar > #toolbar #searchbutton")
    INPUT_REQUEST = (By.CSS_SELECTOR, "#ajaxHeader .desktop-bar > #toolbar #searchformdropdown #query_string")
    CLICK_BUTTON_LOUPE = (
        By.CSS_SELECTOR, "#ajaxHeader .desktop-bar > #toolbar #searchformdropdown > .input-group button")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "#pagecontent table tr td a")
    ACT = (By.CSS_SELECTOR, "#ajaxHeader .desktop-toolbar > ul > li:nth-child(5) .dropdown-menu")

    IMPORT_CALL_BUTTON = (By.CSS_SELECTOR, "#actionMenuSidebar ul li:nth-child(4) a")
    USER_FILE = (By.CSS_SELECTOR, "#userfile")
    NEXT = (By.CSS_SELECTOR, "#gonext")
    CLICK_BUTTON_IMPORT_NOW = (By.CSS_SELECTOR, "#importnow")
    RESULT_MESSAGE = (By.CSS_SELECTOR, "#pagecontent > div > div > div > span")
    ADD_FAVORITES = (By.CSS_SELECTOR, "#pagecontent > .moduleTitle > .favorite")
    LIST_FAVORITES = (By.CSS_SELECTOR, "#favoritesSidebar > ul > div > li > a > span")

    CREATE_ADDRESS_CACHE = (By.CSS_SELECTOR, "#actionMenuSidebar > ul > li:nth-child(2) > a > div.actionmenulink")
    CREATE_PROJECT = (By.CSS_SELECTOR, "#actionMenuSidebar > ul > li:nth-child(2) > a > div.actionmenulink")
    DATE_START = (By.CSS_SELECTOR, "#estimated_start_date")
    DATE_END = (By.CSS_SELECTOR, "#estimated_end_date")
    ADD_NEW_TASK = (By.CSS_SELECTOR, "#add_button")
    TASK_NAME = (By.CSS_SELECTOR, "#task_name")
    START = (By.CSS_SELECTOR, "#Start")
    TABLE_TASK = (
        By.CSS_SELECTOR, "#Task_table > tbody > tr.row_sortable.ui-sortable-handle > td:nth-child(2) > span > a")

    # Меню CREATE ->
    CREATE_DOCUMENT = (By.CSS_SELECTOR, "#quickcreatetop > ul > li:nth-child(5) > a")
    CREATE_TASK = (By.CSS_SELECTOR, "#toolbar > #quickcreatetop ul > li:nth-child(7) a")
    CREATE_CALLS = (By.CSS_SELECTOR, "#toolbar > #quickcreatetop ul > li:nth-child(6) a")
    # Горизонтальное меню
    MENU_ALL = (By.CSS_SELECTOR, "#ajaxHeader .desktop-toolbar > ul > li:nth-child(7) #grouptab_5")
    MENU_ALL_MAPS_ADDR_CACHE = (
        By.CSS_SELECTOR, "#toolbar > ul > li.topnav.all > span.notCurrentTab > ul > li:nth-child(31) > a")
    COLLABORATION = (By.CSS_SELECTOR, "#ajaxHeader .desktop-toolbar > ul > li:nth-child(6) #grouptab_4")
    COLLABORATION_PROJECT = (By.CSS_SELECTOR, "#moduleTab_9_Projects")
    MENU_ACTIV = (By.CSS_SELECTOR, "#ajaxHeader .desktop-toolbar > ul > li:nth-child(5) #grouptab_3")
    MENU_ACTIV_CALLS = (By.CSS_SELECTOR, "#ajaxHeader .desktop-toolbar > ul > li:nth-child(5) ul li:nth-child(3)")
    # Кнопки SAVE
    SAVE_HEADER = (By.CSS_SELECTOR, "#SAVE_HEADER")
    SAVE = (By.CSS_SELECTOR, "#SAVE")
    SAVE_FOOTER = (By.CSS_SELECTOR, "#SAVE_FOOTER")
    # Файлы для загрузки

    # Координаты
    LAT = (By.CSS_SELECTOR, "#lat")
    LNG = (By.CSS_SELECTOR, "#lng")
    # Документ
    DOWNLOAD_FILE_DOC = (By.CSS_SELECTOR, "#filename_file")
    DOC_NAME = (By.CSS_SELECTOR, "#document_name")
    # Таск
    ASSIGNED_TO = (By.CSS_SELECTOR, "#assigned_user_name")
    VIEW_TASK = (By.CSS_SELECTOR, "#actionMenuSidebar ul > li:nth-child(3) a > .actionmenulink")
    ALL_CHECKBOX = (By.CSS_SELECTOR, "#MassUpdate > div.list-view-rounded-corners > table > tbody > tr")
    DELETE_TASK = (By.CSS_SELECTOR, "#delete_listview_bottom")
    # Звонок
    BUTTON_DELETED_TASK = (By.CSS_SELECTOR, "#actionLinkBottom ul > li:nth-child(3) a")
    DURATION_HOURS = (By.CSS_SELECTOR, "#duration_hours")
    SELECT_DURATION_MINUTES = (By.CSS_SELECTOR, "#duration_minutes")
    OPEN_CALENDAR = (By.CSS_SELECTOR, "#date_start_trigger")
    CHOICE_DATE = (By.CSS_SELECTOR, "#date_start_trigger_div_t_cell28")
    # селекторы, которые используются в нескоких кейсах
    DESCRIPTION = (By.CSS_SELECTOR, "#description")
    NAME_SUBJECT = (By.CSS_SELECTOR, "#name")
    MENU_ACTIONS = (By.CSS_SELECTOR, "#content > #pagecontent .detail-view ul > #tab-actions")
    BUTTON_POST = (By.CSS_SELECTOR, ".dashletPanel > .bd .dashletNonTable tbody > tr td:nth-child(3) input")
    REMOVE = (By.CSS_SELECTOR, "#remove_button")
