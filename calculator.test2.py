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
        zeroBtn = self.driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[1]/button'
      )
        oneBtn = self.driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div[1]/button'
      )
        twoBtn = self.driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div[2]/button'
      )
        threeBtn = self.driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div[3]/button'
      )
        fourBtn = self.driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div[1]/button'
      )
        fiveBtn = self.driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div[2]/button'
      )
        sixBtn = self.driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div[3]/button'
      )
        sevenBtn = self.driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button'
      )
        eightBtn = self.driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/button'
      )
        nineBtn = self.driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/button'
      )

        self.digits = {
        '0' : zeroBtn,
        '1' : oneBtn,
        '2' : twoBtn,
        '3' : threeBtn,
        '4' : fourBtn,
        '5' : fiveBtn,
        '6' : sixBtn,
        '7' : sevenBtn,
        '8' : eightBtn,
        '9' : nineBtn 
      }
    
        
        self.resultDiv = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[1]/div'
        )
        self.plusBtn = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div[4]/button'
        )
        self.equalBtn = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[3]/button'
        )

        x1 = randint(0, 1000)
        x2 = randint(0, 5000)
        result = x1 + x2

        # input x1
        for charDigit in str(x1):
            self.digits[charDigit].click()
            sleep(1)

        # click '+' button
        self.plusBtn.click();

        # input x2
        for charDigit in str(x2):
            self.digits[charDigit].click()
            sleep(1)

        # click '=' button
        self.equalBtn.click()

        # results
        print('actual result : ', self.resultDiv.text)
        print('expected result :',f'{x1} + {x2} = {result}')

        self.assertEqual(str(result), self.resultDiv.text)
        self.assertNotEqual(str(x1), self.resultDiv.text)
        self.assertNotEqual(str(x2), self.resultDiv.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
