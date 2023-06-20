import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class TestLocators(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.service = ChromeService(ChromeDriverManager().install())

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=self.service)

    def tearDown(self) -> None:
        self.driver.quit()

    # def test_tag_name(self):
    #     self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    #     textarea = self.driver.find_element(By.TAG_NAME, "textarea")
    #     self.assertEqual(textarea.get_dom_attribute("rows"), "3")
    #
    # def test_by_html_attribute(self):
    #     self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    #
    #     # By name
    #     text_by_name = self.driver.find_element(By.NAME, "my-text")
    #     self.assertTrue(text_by_name.is_enabled())
    #
    #     # By ID
    #     text_by_id = self.driver.find_element(By.ID, "my-text-id")
    #     self.assertEqual(text_by_id.get_attribute("type"), "text")
    #     self.assertEqual(text_by_id.get_dom_attribute("type"), "text")
    #     self.assertEqual(text_by_id.get_property("type"), "text")
    #
    #     # By Class name
    #     by_class_name = self.driver.find_elements(By.CLASS_NAME, "form-control")
    #     self.assertTrue(len(by_class_name) > 0)
    #     self.assertEqual(by_class_name[0].get_attribute("name"), "my-text")
    #
    # def test_by_css_basic(self):
    #     self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    #     hidden_element = self.driver.find_element(By.CSS_SELECTOR, "input[type=hidden]")
    #     self.assertFalse(hidden_element.is_displayed())
    #
    # def test_by_css_advanced(self):
    #     self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    #
    #     checkbox1 = self.driver.find_element(By.CSS_SELECTOR, "[type=checkbox]:checked")
    #     self.assertEqual(checkbox1.get_attribute("id"), "my-check-1")
    #     self.assertTrue(checkbox1.is_selected())
    #
    #     checkbox2 = self.driver.find_element(By.CSS_SELECTOR, "[type=checkbox]:not(:checked)")
    #     self.assertEqual(checkbox2.get_attribute("id"), "my-check-2")
    #     self.assertFalse(checkbox2.is_selected())

    # def test_locator_advanced(self):
    #     self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
    #     date_picker_tb = self.driver.find_element(By.NAME, "my-date")
    #     date_picker_tb.click()
    #     time.sleep(5)
    #     self.driver.find_element(By.XPATH, "//th[contains(text(), 'June')]").click()
    #     time.sleep(5)
    #     self.driver.find_element(By.XPATH, "//div[@class='datepicker-months']//th[@class='prev']").click()
    #     time.sleep(5)
    #     self.driver.find_element(By.XPATH, "//span[@class='month focused']").click()
    #     time.sleep(5)
    #     self.driver.find_element(By.XPATH, "//td[@data-date='1655856000000']").click()
    #     time.sleep(5)
    #     self.assertEqual(date_picker_tb.get_attribute("value"), "22")

    # def test_explicit_wait(self):
    #     self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    #     webdriver_wait = WebDriverWait(self.driver, 10)
    #     landscape = webdriver_wait.until(EC.presence_of_element_located((By.ID, "landscape")))
    #     self.assertTrue(landscape.get_attribute("src").contains("img/landscape.png"))

    def test_explicit_wait_second(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        webdriver_wait = WebDriverWait(self.driver, 10)

        # 7 + 3
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='3']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()
        time.sleep(2)

        webdriver_wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "10"))





if __name__ == '__main__':
    unittest.main()
