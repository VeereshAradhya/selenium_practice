import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class TestSelenium(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.service = ChromeService(ChromeDriverManager().install())

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=self.service)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_first(self):
        suturl = "https://bonigarcia.dev/selenium-webdriver-java/"
        self.driver.get(suturl)
        title = self.driver.title
        self.assertEquals(title, "Hands-On Selenium WebDriver with Java")
        self.driver.find_element()

    def test_by_tagname(self):
        suturl = "https://bonigarcia.dev/selenium-webdriver-java/web-form.html"
        self.driver.get(suturl)
        textarea = self.driver.find_element(By.TAG_NAME, "textarea")
        self.assertEqual(textarea.get_dom_attribute("rows"), "3")




if __name__ == '__main__':
    unittest.main()
