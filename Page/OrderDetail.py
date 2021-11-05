from Base.Base import Base
from Page.PageElements import PageElements


class OrderDetail(Base):
    """在线支付页"""

    def __init__(self):
        super().__init__()

    def get_title_order(self):
        """选择支付方式,确认支付"""
        return self.get_text_xpath(PageElements.order_status)
