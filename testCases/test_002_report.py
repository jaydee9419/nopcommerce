
from pageObjects.ReportPage import ReportPage
from pageObjects.LoginPage import LoginPage


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

        self.rp = ReportPage(self.driver)
        self.rp.clickReportlink()
        self.rp.clickSalesSummary()
        self.rp.getTableHeading()
        self.rp.getTableBody()

