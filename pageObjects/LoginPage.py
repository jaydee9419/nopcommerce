from selenium.webdriver.common.by import By
import time
class LoginPage():
    input_email_xpath = "//input[@id='Email']"
    input_password_xpath = "//input[@id='Password']"
    btn_login_xpath = "//button[normalize-space()='Log in']"
    txt_confmsg_xpath = "//h1[normalize-space()='Dashboard']"
    btn_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self):
        email_input = self.driver.find_element(By.XPATH, self.input_email_xpath)
        email_input.clear()
        time.sleep(2)
        email_input.send_keys("admin@yourstore.com")

    def setPassword(self):
        password_input = self.driver.find_element(By.XPATH, self.input_password_xpath)
        password_input.clear()
        password_input.send_keys("admin")

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_confmsg_xpath).text
        except:
            None

    def isLoginpagedisplayed(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_confmsg_xpath).is_displayed()
        except:
            None

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()
