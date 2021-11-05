from Base.Base  import Base
from Page.PageElements import PageElements


class LoginPage(Base):
    """登录页面"""

    def __init__(self):
        super().__init__()

    def switch_county(self):
        """
        选择国别码
        :return: 点击进入选择国别码页
        """
        self.click_ele(PageElements.area_code)

    def login(self, phone):
        """
        登录方法
        :param phone: 登录手机号
        :return: 点击获取验证码进入获取验证码页
        """
        # 登录操作
        self.set_ele(PageElements.input_phone_text, phone)
        # 登录按钮点击
        self.click_ele(PageElements.get_code)

