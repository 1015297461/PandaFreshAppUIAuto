from Base.Base import Base
from Page.PageElements import PageElements


class CountryPage(Base):
    """选择国别码页"""

    def __init__(self):
        super().__init__()

    def click_country(self):
        """
        选择指定的国别码
        :return: 返回登录页
        """
        self.click_ele(PageElements.country_china)
