from Base.Base import Base
from Page.PageElements import PageElements


class SearchResultPage(Base):
    """搜索结果页"""

    def __init__(self):
        super().__init__()

    def click_goods_name(self):
        """搜索结果页点击进入商品详情"""
        self.click_ele(PageElements.search_goods_name)