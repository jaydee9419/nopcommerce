import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
import time
import os


class Test_login():
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"

    def test_login(self, setup):
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setEmail()
        self.lp.setPassword()
        self.lp.clickLoginButton()
        self.lp.isLoginpagedisplayed()
        self.lp.getconfirmationmsg()
        confirmation_msg = self.lp.getconfirmationmsg()
        print("Confirmation Message:", confirmation_msg)

        self.hp = HomePage(self.driver)
        self.hp.clickCustomer()
        time.sleep(3)
        self.hp.clickCustomerData()
        self.hp.clickNewcustomer()

        self.hp.setEmail()
        self.hp.setPassword()
        self.hp.setFirstname()
        self.hp.setLastname()
        self.hp.clickGender()
        self.hp.setDateofbirth()
        self.hp.setCompany()
        self.hp.clickSave()

        self.lp.getconfirmationmsg()

        self.lp.clickLogout()

        time.sleep(3)


