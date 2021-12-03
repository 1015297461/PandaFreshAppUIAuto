import os
import shutil
import pytest
from Base.Base import Base
from Base.Driver import Driver
from Base.GetData import GetData
from Base.Page import Page


def login_data():
    """
    获取yml中登录的测试数据
    :return: 将数据组成新列表返回
    """
    loginDataList = []
    data = GetData.get_yml_data("login.yml")
    for i in data.values():
        loginDataList.append((i.get("phone"), i.get("exp"), i.get("code")))

    return loginDataList

class Test_Login:

    # @pytest.fixture(scope="class", autouse=True)
    # def removeReport(self):
    #     print("zhixingyici")
    #     base().removeReport()

    @pytest.fixture(autouse=True)
    def clear_app(self):
        """每次执行"""
        Base.os_clear()
        Base.os_rm()

    @pytest.fixture(autouse=True)
    def star_app(self):
        """每次执行"""
        Base().start()
        Page.get_setting().allow_sys()
        Page.get_home().click_my_btn()
        Page.get_person().click_login_sign_btn()
        Page.get_login().switch_county()
        Page.get_country().click_country()

    @pytest.mark.parametrize("phone, exp, code", login_data())
    def test_login(self, phone, exp, code):
        Page.get_login().login(phone)
        Page.get_input_code().input_code(code)
        message = Page.get_person().get_user_name()
        assert message == exp

    def  teardown(self):
        Driver.quit_app_driver()



