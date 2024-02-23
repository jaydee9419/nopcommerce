
from pageObjects.CatalogPage import CatalogPage
from pageObjects.LoginPage import LoginPage
import time


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

        self.cp = CatalogPage(self.driver)
        self.cp.clickCatolog()
        self.cp.clickProducts()
        self.cp.getProductsList()
        time.sleep(5)
