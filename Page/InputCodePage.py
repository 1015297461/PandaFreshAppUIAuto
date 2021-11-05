from Base.Base import Base
from Page.PageElements import PageElements
from selenium.common.exceptions import TimeoutException


class InputCodePage(Base):

    def __init__(self):
        super().__init__()

    def input_code(self, code):
        """输入万能验证码"""
        self.click_ele(PageElements.code1)
        self.send_ele(code)
        self.click_ele(PageElements.code2)
        self.send_ele(code)
        self.click_ele(PageElements.code3)
        self.send_ele(code)
        self.click_ele(PageElements.code4)
        self.send_ele(code)
        self.click_ele(PageElements.code5)
        self.send_ele(code)
        self.click_ele(PageElements.code6)
        self.send_ele(code)





