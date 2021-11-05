from Page.AddAddressPage import AddAddressPage
from Page.AddNewCardPage import AddNewCardPage
from Page.ChoseAddressPage import ChoseAddressPage
from Page.CountryPage import CountryPage
from Page.GoodsDetailPage import GoodsDetailPage
from Page.HomePage import HomePage
from Page.InputCodePage import InputCodePage
from Page.InputRemarkPage import InputRemarkPage
from Page.LoginPage import LoginPage
from Page.MyCardPage import MyCardPage
from Page.OrderDetail import OrderDetail
from Page.PayOrderPage import PayOrderPage
from Page.PaySuccessPage import PaySuccessPage
from Page.PersonPage import PersonPage
from Page.PreOrderPage import PreOrderPage
from Page.ReceiptAddressPage import ReceiptAddressPage
from Page.RightTopCarPage import RightTopCarPage
from Page.SearchPage import SearchPage
from Page.SearchResultPage import SearchResultPage
from Page.SettingPage import SettingPage


class Page:

    @classmethod
    def get_setting(cls):
        """返回系统设置对象"""
        return SettingPage()

    @classmethod
    def get_home(cls):
        """返回首页对象"""
        return HomePage()

    @classmethod
    def get_person(cls):
        """返回个人中心页对象"""
        return PersonPage()

    @classmethod
    def get_login(cls):
        """返回登录页对象"""
        return LoginPage()

    @classmethod
    def get_country(cls):
        """返回切换国别码页对象"""
        return CountryPage()

    @classmethod
    def get_input_code(cls):
        """返回输入验证码页对象"""
        return InputCodePage()

    @classmethod
    def add_address(cls):
        """返回添加地址页对象"""
        return AddAddressPage()

    @classmethod
    def add_new_card(cls):
        """返回添加新银行卡对象"""
        return AddNewCardPage()

    @classmethod
    def chose_address(cls):
        """返回选择地址页对象"""
        return ChoseAddressPage()

    @classmethod
    def goods_detail(cls):
        """返回商品详情页对象"""
        return GoodsDetailPage()

    @classmethod
    def input_remark(cls):
        """返回输入备注页对象"""
        return InputRemarkPage()

    @classmethod
    def my_card(cls):
        """返回我的银行卡页对象"""
        return MyCardPage()

    @classmethod
    def pay_order(cls):
        """返回支付订单页对象"""
        return PayOrderPage()

    @classmethod
    def pay_success(cls):
        """返回支付成功页对象"""
        return PaySuccessPage()

    @classmethod
    def pre_order(cls):
        """返回预处理订单页对象"""
        return PreOrderPage()

    @classmethod
    def receipt_address(cls):
        """返回收货地址页对象"""
        return ReceiptAddressPage()

    @classmethod
    def right_top_car(cls):
        """返回右上角购物车页对象"""
        return RightTopCarPage()

    @classmethod
    def search_page(cls):
        """返回搜索页对象"""
        return SearchPage()

    @classmethod
    def search_result(cls):
        """返回搜索页对象"""
        return SearchResultPage()

    @classmethod
    def order_detail(cls):
        """返回搜索页对象"""
        return OrderDetail()




