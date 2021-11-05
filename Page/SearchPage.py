from Base.Base import Base
from Page.PageElements import PageElements


class SearchPage(Base):
    """搜索页"""

    def __init__(self):
        super().__init__()

    def input_search_text(self):
        """

        :param search_text: 输入需要搜索的文本内容
        :return: 调用系统搜索进入搜索结果页
        """
        # self.set_ele(PageElements.search_input_text,search_text)
        # self.press_enter_ele()
        self.click_ele(PageElements.hot_search)