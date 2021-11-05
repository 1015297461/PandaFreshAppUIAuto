from Base.Base import Base
from Page.PageElements import PageElements


class SettingPage(Base):
    """首次打开app,系统页"""

    def __init__(self):
        super().__init__()

    def allow_sys(self):
        """
        首次进入app-允许系统操作
        :return: 允许进入app
        """
        self.click_ele(PageElements.allow)