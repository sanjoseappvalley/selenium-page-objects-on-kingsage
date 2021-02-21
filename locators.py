from selenium.webdriver.common.by import By


class FrontPageLocators(object):
    LOGIN_BOX = (By.ID, 'loginButton')
    USERNAME = (By.ID, 'loginPlayerName')
    PASSWORD = (By.ID, 'loginPlayerPassword')
    LOGIN_BUTTON = (By.CLASS_NAME, 'styledInputButton')
    CONTENT_HEADER = (By.CLASS_NAME, 'content_header')
    SERVERS = (By.XPATH, '//option[@value]')
    SERVERLIST = (By.ID, 'serverlist_title')
    SERVER_23 = (By.XPATH, '//*[@id="serverlist_child"]/ul/li[23]/span')
    PLAY_BUTTON = (By.ID, 'serverStartPlaying')
