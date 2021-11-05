import time

import pytest
from Base.Base import Base
from Base.Driver import Driver
from Base.GetData import GetData
from Base.Page import Page


def create_order_data():
    """
    获取yml中登录的测试数据
    :return: 将数据组成新列表返回
    """
    OrderDataList = []
    data = GetData.get_yml_data("createOrder.yml")
    for i in data.values():
        OrderDataList.append((i.get("phone"), i.get("exp"), i.get("code"), i.get("name"),
                              i.get("phone_num"),i.get("postcode"),i.get("build_name"),i.get("unit"),i.get("remark"),i.get("card_num"),
                              i.get("card_cvv"),i.get("postcode9"),i.get("exp_pay")
                              ))
    print(OrderDataList)
    return OrderDataList


class TestCreateOrder:

    @pytest.fixture(autouse=True)
    def clear_app(self):
        """每次执行"""
        Base.os_clear()

    @pytest.fixture(autouse=True)
    def star_app(self):
        """每次执行"""
        Base().start()
        Page.get_setting().allow_sys()
        Page.get_home().click_my_btn()
        Page.get_person().click_login_sign_btn()

    @pytest.mark.parametrize("phone, exp, code, name, phone_num,"
                             "postcode, build_name, unit, remark,"
                             "card_num, card_cvv, postcode9, exp_pay", create_order_data())
    def test_create_order(self, phone, exp, code, name, phone_num,
                   postcode, build_name, unit, remark,
                   card_num, card_cvv, postcode9, exp_pay
                   ):
        Page.get_login().login(phone)
        Page.get_input_code().input_code(code)
        message = Page.get_person().get_user_name()
        assert message == exp
        # 点击首页
        Page.get_person().click_home()
        # 使用返回关闭弹窗
        time.sleep(5)
        Base().sys_back()
        # 点击搜索
        # time.sleep(3)
        Page.get_home().click_search()
        # 输入搜索内容
        Page.search_page().input_search_text()
        # 搜索结果页进入商品详情
        time.sleep(5)
        Page.search_result().click_goods_name()
        #  商品详情加入购物车,进入购物车
        Page.goods_detail().click_add_car()
        time.sleep(3)
        Page.goods_detail().click_top_cart()
        # 购物车去结算
        Page.right_top_car().to_settle()
        # 提交订单页选择收货地址
        Page.pre_order().click_address()
        # 收货地址页点击新增地址
        Page.receipt_address().click_add_address()
        # 新增地址页先点击选择收货地址进入地图页
        Page.add_address().click_location()
        # 地图页选择默认地址
        time.sleep(3)
        Page.chose_address().click_location()
        # 新增地址页填写其他信息
        Page.add_address().send_address_detail(name, phone_num, postcode, build_name, unit)
        Page.receipt_address().select_address()
        time.sleep(5)
        # 提交订单页输入备注信息
        Page.pre_order().swipe_to_notice()
        # 输入备注
        Page.input_remark().input_remark(remark)
        Page.pre_order().click_checkout()
        time.sleep(6)
        Page.pay_order().click_stripe()
        Page.pay_order().true_submit()
        # 新增银行卡页
        Page.my_card().click_add_card()
        # 新增银行卡信息
        Page.add_new_card().add_new_card(card_num, card_cvv, postcode9)
        Page.my_card().check_card()
        time.sleep(6)

        # 获取支付成功页
        title_text = Page.pay_success().get_title()
        assert title_text == exp_pay

    def  teardown(self):
        Driver.quit_app_driver()
