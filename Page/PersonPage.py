from Base.Base import Base
from Page.PageElements import PageElements


class PersonPage(Base):
    """个人中心页"""

    def __init__(self):
        super().__init__()

    def click_login_sign_btn(self):
        """
        点击登录按钮
        :return: 进入登录页
        """
        self.click_ele(PageElements.login_btn)

    def get_user_name(self):
        """
        获取登录后的用户名
        :return: 用于断言
        """
        return self.get_text_xpath(PageElements.login_btn)

    def click_home(self):
        return self.click_ele(PageElements.home_btn)