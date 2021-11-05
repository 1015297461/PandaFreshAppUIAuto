from Base.Base import Base
from Page.PageElements import PageElements


class RightTopCarPage(Base):
    """右上角进入的购物车页"""

    def __init__(self):
        super().__init__()

    def click_single_box(self):
        """点击单选框,再去结算进入提交订单页"""
        self.click_ele_id(PageElements.single_check_box)

    def to_settle(self):
        self.click_ele(PageElements.to_settle)
