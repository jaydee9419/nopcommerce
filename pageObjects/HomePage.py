from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class HomePage():
    txt_customers_xpath = "(//p[contains(text(),'Customers')])[1]"
    txt_customers_data_xpath = "//a[@href='/Admin/Customer/List']"
    btn_newcustomer_xpath = "//a[normalize-space()='Add new']"

    input_email_name = "Email"
    input_password_name = "Password"
    input_fname_name= "FirstName"
    input_lname_name = "LastName"
    radbtn_gender_xpath = "//input[@id='Gender_Male']"
    input_dob_xpath = "//input[@id='DateOfBirth']"
    input_company_name = "Company"
    btn_save_xpath = "//button[@name='save']"

    input_confmsg_xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomer(self):
        new = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.txt_customers_xpath)))
        new.click()


    def clickCustomerData(self):
        self.driver.find_element(By.XPATH, self.txt_customers_data_xpath).click()

    def clickNewcustomer(self):
        self.driver.find_element(By.XPATH, self.btn_newcustomer_xpath).click()



    def setEmail(self):
        self.driver.find_element(By.NAME, self.input_email_name).send_keys("12347898@gmail.com")

    def setPassword(self):
        self.driver.find_element(By.NAME, self.input_password_name).send_keys("4321")

    def setFirstname(self):
        self.driver.find_element(By.NAME, self.input_fname_name).send_keys("cba")

    def setLastname(self):
        self.driver.find_element(By.NAME, self.input_lname_name).send_keys("abc")

    def clickGender(self):
        self.driver.find_element(By.XPATH, self.radbtn_gender_xpath).click()

    def setDateofbirth(self):
        self.driver.find_element(By.XPATH, self.input_dob_xpath).send_keys("1/05/2000")

    def setCompany(self):
        self.driver.find_element(By.NAME, self.input_company_name).send_keys("IlC")

    def clickSave(self):
        try:
            self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
            assert True
        except:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "login.png")
            assert False

    def getconfirmationmsg(self):
        try:
            self.driver.find_element(By.XPATH, self.input_confmsg_xpath).is_displayed()
        except:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "login.png")
            None














