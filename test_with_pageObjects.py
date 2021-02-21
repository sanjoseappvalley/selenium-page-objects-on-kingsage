import unittest
from selenium import webdriver
import page
import time


class KingsageGameTest(unittest.TestCase):
    """A test class to connect the game on Chrome browser"""

    def setUp(self):
        PATH = "C:\\Users\\NightBaron\\chromedriver_win32\\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://us.kingsage.gameforge.com/")

    def test_kingsage_usa_server(self):
        """Connect to kingsage. Logs in and check the servers. Choose a server and go in"""

        front_page = page.FrontPage(self.driver)
        front_page.login()
        time.sleep(1)
        assert front_page.is_welcomeText_matches()
        assert front_page.is_number_of_servers_correct()
        front_page.go_into_a_server()
        time.sleep(1)

        game_page = page.GamePage(self.driver)
        assert game_page.is_title_matches()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
