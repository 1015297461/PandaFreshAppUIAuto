from Base.Base import Base
from Page.PageElements import PageElements


class PayOrderPage(Base):
    """在线支付页"""

    def __init__(self):
        super().__init__()

    def click_stripe(self):
        """选择支付方式,确认支付"""
        self.click_ele(PageElements.stripe_xpath)

    def true_submit(self):
        self.click_ele(PageElements.submit)
