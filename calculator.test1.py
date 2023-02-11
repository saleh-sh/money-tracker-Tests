import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import randint


class SampleTeseCase(unittest.TestCase):

    def setUp(self):
        # open Chrome browser
        self.driver = webdriver.Chrome()
        # maximize the window size
        self.driver.maximize_window()
        # delete the cookies
        self.driver.delete_all_cookies()
        # navigate to the url
        self.driver.get('http://localhost:3000/')

    def test(self):
        x1 = randint(0, 100)
        x2 = randint(20, 50)
        result = x1 + x2

        self.resultDiv = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[1]/div'
        )
        self.plusBtn = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div[4]/button'
        )
        self.equalBtn = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[3]/button'
        )

        # inject x1 as first operand
        self.driver.execute_script(
            f"arguments[0].innerText={x1}", self.resultDiv
        )
        sleep(1)

        # click plus button
        self.plusBtn.click()
        sleep(1)

        # inject x2 as second operand
        self.driver.execute_script(
            f"arguments[0].innerText={x2}", self.resultDiv
        )
        sleep(1)

        # click equal button
        self.equalBtn.click()
        sleep(1)

        # results
        print('actual result : ', self.resultDiv.text)
        print('expected result :', f'{x1} + {x2} = {result}')

        self.assertNotEqual(str(result), self.resultDiv.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
