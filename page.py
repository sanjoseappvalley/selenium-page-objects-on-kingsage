import time
from locators import FrontPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class FrontPage(BasePage):

    def login(self):
        loginBox = self.driver.find_element(*FrontPageLocators.LOGIN_BOX)
        loginBox.click()
        time.sleep(1)
        self.driver.find_element(*FrontPageLocators.USERNAME).send_keys('name')  # change name
        self.driver.find_element(*FrontPageLocators.PASSWORD).send_keys('pass')  # change pass
        self.driver.find_element(*FrontPageLocators.LOGIN_BUTTON).click()

    def is_welcomeText_matches(self):
        welcomeText = self.driver.find_element(*FrontPageLocators.CONTENT_HEADER).text
        return "Welcome NightBaron" in welcomeText

    def is_number_of_servers_correct(self):
        servers = self.driver.find_elements(*FrontPageLocators.SERVERS)
        """Check if there are 26 servers total"""
        return len(servers) == 26

    def go_into_a_server(self):
        self.driver.find_element(*FrontPageLocators.SERVERLIST).click()
        time.sleep(1)
        """Choose server 23"""
        self.driver.find_element(*FrontPageLocators.SERVER_23).click()
        self.driver.find_element(*FrontPageLocators.PLAY_BUTTON).click()


class GamePage(BasePage):

    def is_title_matches(self):
        """Search in page title"""
        return "KingsAge - NightBaron" in self.driver.title
