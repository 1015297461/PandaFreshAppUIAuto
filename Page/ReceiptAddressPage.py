from Base.Base import Base
from Page.PageElements import PageElements


class ReceiptAddressPage(Base):
    """收货地址页"""

    def __init__(self):
        super().__init__()

    def click_add_address(self):
        """点击新增地址,进入新增地址页"""
        self.click_ele(PageElements.add_address)

    def select_address(self):
        """选择列表中的收货地址"""
        self.click_ele(PageElements.select_status)
