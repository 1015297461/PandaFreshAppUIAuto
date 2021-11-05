from Base.Base import Base
from Page.PageElements import PageElements


class MyCardPage(Base):
    """我的银行卡页"""

    def __init__(self):
        super().__init__()

    def click_add_card(self):
        """点击新增银行卡,进入新增银行卡页"""
        self.click_ele(PageElements.add_new_card)

    def check_card(self):
        self.click_ele(PageElements.check_card)
