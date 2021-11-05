from Base.Base import Base
from Page.PageElements import PageElements


class GoodsDetailPage(Base):
    """商品详情页"""

    def __init__(self):
        super().__init__()

    def click_add_car(self):
        """点击下方加入购车"""
        self.click_ele(PageElements.add_cart)

    def click_top_cart(self):
        """点击进入右上角购物车"""
        self.click_ele(PageElements.right_top_cart)



