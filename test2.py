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
        # find Additional country dropdown
        self.addCountryDropDown = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/form[1]/div/div[2]/div/i')
        self.addCountryDropDown.click()

        self.allAddCountries = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/form[1]/div/div[2]/div/div[2]'
        ).find_elements(By.TAG_NAME, 'div')

        allCountriesCount = len(self.allAddCountries)
        randomCountryIndex = randint(0, allCountriesCount)
        self.selectedAddCountry = self.allAddCountries[randomCountryIndex]
        self.selectedAddCountryName = self.selectedAddCountry.text.split(',')[
            0]
        self.selectedAddCountry.click()
        sleep(2)

        self.addCountryDropDown.click()

        self.allAddCountries = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/form[1]/div/div[2]/div/div[2]'
        ).find_elements(By.TAG_NAME, 'div')

        for country in self.allAddCountries:
            countryName = country.text.split(',')[0]
            print(countryName, ' != ', self.selectedAddCountryName)
            self.assertNotEqual(country, self.selectedAddCountry)
            self.assertNotEqual(countryName, self.selectedAddCountryName)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
