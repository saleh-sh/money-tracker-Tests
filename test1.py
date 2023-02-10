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
        # find Base country dropdown
        self.baseCountryDropDown = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/form[1]/div/div[1]/div/input')
        self.baseCountryDropDown.click()
        sleep(2)

        self.allBaseCountries = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/form[1]/div/div[1]/div/div[2]'
        ).find_elements(By.TAG_NAME, 'div')

        allCountriesCount = len(self.allBaseCountries)
        randomCountryIndex = randint(0, allCountriesCount)
        self.selectedBaseCountry = self.allBaseCountries[randomCountryIndex]
        self.selectedBaseCountryName = self.selectedBaseCountry.text.split(',')[
            0]
        self.selectedBaseCountry.click()

        self.addCountryDropDown = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/form[1]/div/div[2]/div/i')
        self.addCountryDropDown.click()

        self.allAddCountries = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/form[1]/div/div[2]/div/div[2]'
        ).find_elements(By.TAG_NAME, 'div')

        allCountriesCount = len(self.allAddCountries)
        randomCountryIndex = randint(0, allCountriesCount)
        self.selectedAddCountry = self.allAddCountries[randomCountryIndex]
        self.selectedAddCountryName = self.selectedAddCountry.text.split(',')[0]
        self.selectedAddCountry.click()
        sleep(4)

        print('------------------', 'Base Country: ',
              self.selectedBaseCountryName, '----------------')

        print('------------------', 'Additional Country: ',
              self.selectedAddCountryName, '----------------')

        self.firstTableCountryName = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/table/thead/tr/th[2]').text

        self.secondTableCountryName = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/table/thead/tr/th[3]').text

        self.assertEqual(self.selectedBaseCountryName,
                         self.firstTableCountryName)
        self.assertEqual(self.selectedAddCountryName,
                         self.secondTableCountryName)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
