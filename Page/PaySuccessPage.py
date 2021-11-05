from Base.Base import Base
from Page.PageElements import PageElements


class PaySuccessPage(Base):
    """支付成功页"""

    def __init__(self):
        super().__init__()

    def get_title(self):
        return self.get_text_xpath(PageElements.pay_title)
