import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class KingsAgeTest(unittest.TestCase):

    def setUp(self):
        driverPath = "C:\\Users\\NightBaron\\chromedriver_win32\\chromedriver.exe"
        self.driver = webdriver.Chrome(driverPath)
        self.driver.get("https://us.kingsage.gameforge.com")

    def test_login_a_kingsage_server(self):
        driver = self.driver
        # driver.get("https://us.kingsage.gameforge.com")
        loginBox = driver.find_element_by_id('loginButton')
        loginBox.click()
        time.sleep(1)
        driver.find_element_by_id('loginPlayerName').send_keys('name')  # Change name
        driver.find_element_by_id('loginPlayerPassword').send_keys('pass')  # Change password
        driver.find_element_by_class_name('styledInputButton').click()
        time.sleep(1)
        welcomeText = driver.find_element_by_class_name('content_header').text
        self.assertEqual("Welcome NightBaron", welcomeText)
        servers = driver.find_elements_by_xpath("//option[@value]")
        self.assertEqual(26, len(servers))
        driver.find_element_by_id("serverlist_title").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id=\"serverlist_child\"]/ul/li[23]/span").click()
        driver.find_element_by_id("serverStartPlaying").click()
        time.sleep(1)
        self.assertIn("KingsAge - name", driver.title)  # Change name

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    import xmlrunner

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False
    )
