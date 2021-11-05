from Base.Base import Base
from Page.PageElements import PageElements


class HomePage(Base):
    """首页"""

    def __init__(self):
        super().__init__()

    def click_my_btn(self):
        """
        点击我的
        :return:进入个人中心页
        """
        self.click_ele(PageElements.home_my_btn)

    def click_search(self):
        self.click_ele(PageElements.search_input_xpath)
