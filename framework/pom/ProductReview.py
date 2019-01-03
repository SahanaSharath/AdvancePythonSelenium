from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class ProductReview(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _searchBar = "twotabsearchtextbox"
    _searchSymbol = "//input[@class='nav-input' and @value='Go']"
    _avgReview = "//*[@id='leftNavContainer']/ul[14]/div/li//span[@class='a-list-item']"

    def searchProduct(self):
        self.getElement(self._searchBar, "id")
        data = self.jsonFileRead("F:\\PythonQSP\\AdvancePython\\AdvancePythonSelenium\\framework\\productToSearch.json")
        pname = data["product_name"]
        self.sendKeys(pname, self._searchBar)
        print(pname)
        self.elementClick(self._searchSymbol, "xpath")
        return True

    def getAvgReview(self):
        actionChains = ActionChains(self.driver)
        # reviewList = self.getElement(self._avgReview, "xpath")
        reviewList = self.driver.find_elements_by_xpath(self._avgReview)
        for item in reviewList:
            actionChains.context_click(item).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            self.driver.implicitly_wait(5)
        return True