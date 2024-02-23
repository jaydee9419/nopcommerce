from selenium.webdriver.common.by import By

class CatalogPage():

    lnk_catalog_xpath = "//p[normalize-space()='Catalog']"
    lnk_products_xpath = "//a[@href='/Admin/Product/List']"
    lst_products_list_xpath = "//tr"

    def __init__(self, driver):
        self.driver = driver

    def clickCatolog(self):
        self.driver.find_element(By.XPATH, self.lnk_catalog_xpath).click()

    def clickProducts(self):
        self.driver.find_element(By.XPATH, self.lnk_products_xpath).click()

    def getProductsList(self):
        products = self.driver.find_elements(By.XPATH, self.lst_products_list_xpath)
        for items in products:
            print(items.text)
