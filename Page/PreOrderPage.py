from Base.Base import Base
from Page.PageElements import PageElements


class PreOrderPage(Base):
    """提交订单页"""

    def __init__(self):
        super().__init__()

    def click_address(self):
        """点击请选择收货地址进入收货地址页"""
        self.click_ele(PageElements.chose_address)

    def swipe_to_notice(self):
        self.swipe(0.412, 0.877, 0.412, 0.292)
        self.click_ele(PageElements.checkout_remark)

    def click_checkout(self):
        self.click_ele(PageElements.checkout)
