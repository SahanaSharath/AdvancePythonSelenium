from framework.pom.ProductReview import ProductReview
import pytest
import unittest
import json

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_ProductReview(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.pr = ProductReview(self.driver)

    @pytest.mark.run(order=1)
    def test_search(self):
        self.pr.searchProduct()
        self.pr.getAvgReview()

    # @pytest.mark.run(order=2)
    # def test_reviews(self):
    #     self.pr.getAvgReview()
