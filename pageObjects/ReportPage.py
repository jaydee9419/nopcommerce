
from selenium.webdriver.common.by import By

class ReportPage():
    lnk_reports_xpath = "//p[normalize-space()='Reports']"
    lnk_sales_summary_xpath = "//p[normalize-space()='Sales summary']"
    lst_table_heading_xpath = "//div[@class='dataTables_scrollHeadInner']//th"
    lst_table_content_xpath = "//tbody//tr//td"

    def __init__(self, driver):
        self.driver = driver

    def clickReportlink(self):
        self.driver.find_element(By.XPATH, self.lnk_reports_xpath).click()

    def clickSalesSummary(self):
        self.driver.find_element(By.XPATH, self.lnk_sales_summary_xpath).click()

    def getTableHeading(self):
        headdings = self.driver.find_elements(By.XPATH, self.lst_table_heading_xpath)
        combined_head_text = "      ".join([element.text for element in headdings])

        # Print the combined text
        print(combined_head_text)
        print("   ")

    def getTableBody(self):
        body_content = self.driver.find_elements(By.XPATH, self.lst_table_content_xpath)
        combined_body_text = "        ".join([element.text for element in body_content])

        # Print the combined text
        print(combined_body_text)












