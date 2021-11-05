class PageElements:
    """
        存储所需定位的所有元素值
    """

    """----系统----"""
    # 临时允许
    allow = '//*[@resource-id="com.android.permissioncontroller:id/'\
            'permission_allow_foreground_only_button"]'

    """----首页----"""
    # 我的
    home_my_btn =  '//*[@resource-id="com.hungry.panda.market:id/' \
    'm_base_ll_bottom_navigation_bar_item_container"]/' \
    'android.widget.FrameLayout[4]/android.widget.FrameLayout[1]/' \
    'android.widget.FrameLayout[1]/android.widget.ImageView[1]'
    # 顶部搜索
    search_input = "com.hungry.panda.market:id/tv_home_search"
    search_input_xpath = '//*[@resource-id="com.hungry.panda.market:id/tv_home_search"]'

    """----搜索---"""
    # 搜索页搜索输入框
    search_input_text = "搜索商品"
    # 搜索页热搜词
    hot_search = "UI"
    # 搜索结果页商品名称
    search_goods_name = '//*[@resource-id="com.hungry.panda.market:id/tv_home_flow_goods_price"]'

    """---商品详情----"""
    # 加入购物车
    add_cart = '//*[@resource-id="com.hungry.panda.market:id/scnv_cart_num"]'
    # 右上角购物车
    right_top_cart = '//*[@resource-id="com.hungry.panda.market:id/iv_shopping_bag"]'

    """----右上角购物车----"""
    # 右上角购物车页
    single_check_box = "com.hungry.panda.market:id/iv_select_status"
    to_settle = '//*[@resource-id="com.hungry.panda.market:id/tv_to_settle"]'


    """----提交订单页------"""
    # 选择收货地址
    chose_address = '//*[@resource-id="com.hungry.panda.market:id/tv_checkout_null_address_hint"]'
    # 备注
    checkout_remark = '//*[@resource-id="com.hungry.panda.market:id/tv_checkout_remark"]'
    # 提交订单
    checkout = '//*[@resource-id="com.hungry.panda.market:id/tv_checkout"]'

    """----支付成功----"""
    # 支付成功title
    pay_title = '//*[@resource-id="com.hungry.panda.market:id/tv_pay_result_view_order"]'

    """----订单详情----"""
    order_status = '//*[@resource-id="com.hungry.panda.market:id/tv_order_status"]'

    """----我的银行卡------"""
    # 新增银行卡
    add_new_card = '//*[@resource-id="com.hungry.panda.market:id/tv_add_bank"]'
    # 选择银行卡
    check_card = '//*[@resource-id="com.hungry.panda.market:id/rv_bank_card"]/android.view.ViewGroup[1]'

    """----新增银行卡信息------"""
    card_num = '//*[@resource-id="com.hungry.panda.market:id/til_card_number"]'
    valid_date = '//*[@resource-id="com.hungry.panda.market:id/til_valid_date"]'
    delivery_date = '//*[@text="2023"]'
    delivery_date_text = "2023"
    delivery_time = '//*[@text="3"]'
    delivery_time_text = "3"
    cvv_number = '//*[@resource-id="com.hungry.panda.market:id/til_cvv_number"]'
    til_postcode = '//*[@resource-id="com.hungry.panda.market:id/til_postcode"]'
    til_postcode_text = "请填写邮编"
    true_btn = "//android.view.View[1]"

    """----在线支付页----"""
    # 选择支付方式
    payment_name = "com.hungry.panda.market:id/tv_payment_name"
    # stripe
    stripe = "银行卡/信用卡stripePay"
    stripe_xpath = '//*[@text="银行卡/信用卡stripePay"]'
    # 提交订单
    submit = '//*[@resource-id="com.hungry.panda.market:id/tv_confirm_pay"]'


    """----填写备注页-----"""
    remark_text = "在这里填写您的备注信息"
    # 右上角完成
    completed = '//*[@resource-id="com.hungry.panda.market:id/m_base_tv_title_right"]'


    """----收货地址页----"""
    # 右上角新增地址
    add_address ='//*[@resource-id="com.hungry.panda.market:id/m_base_tv_title_right"]'
    # 选择收货地址单选框
    select_status = '//*[@resource-id="com.hungry.panda.market:id/rv_address_list"]/android.view.ViewGroup[1]'


    """----新增地址页----"""
    # 选择收货地址按钮
    address_location = '//*[@resource-id="com.hungry.panda.market:id/tv_address"]'
    # contact_name = "com.hungry.panda.market:id/et_contact"
    contact_name  = "姓名"
    phone = "手机号码"
    postcode = "邮编"
    postcode_id = '//*[@resource-id="com.hungry.panda.market:id/et_postcode"]'
    build = "大楼名称/公司名称（非必填）"
    unit = "楼层/门牌号/公寓号( 非必填）"
    tag_home = '//*[@resource-id="com.hungry.panda.market:id/rb_tag_home"]'
    true_address = '//*[@resource-id="com.hungry.panda.market:id/tv_confirm"]'


    """----选择地址页---"""
    # 底部定位的地址tab
    # address_local_map = '//*[@resource-id="root"]/android.view.View[1]/android.view.View[3]/android.view.View[1]'
    address_local_map_x = 0.403
    address_local_map_y = 0.866

    """---个人中心---"""
    #登录/注册
    login_btn = '//*[@resource-id="com.hungry.panda.market:id/tv_account_username"]'
    # 点击首页
    home_btn = '//*[@resource-id="com.hungry.panda.market:id/m_base_ll_bottom_navigation_bar_item_container"]/' \
               'android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/' \
               'android.widget.FrameLayout[1]/android.widget.ImageView[1]'

    """----登录----"""
    # 手机号
    phone_num = '//*[@resource-id="com.hungry.panda.market:id/et_phone_number"]'
    # 获取验证码
    get_code = '//*[@resource-id="com.hungry.panda.market:id/btn_get_verify_code"]'
    # 国别码
    area_code = '//*[@resource-id="com.hungry.panda.market:id/tv_area_code"]'
    # 手机号输入框text
    input_phone_text = "请输入手机号"

    """----选择区号----"""
    country_china = '//*[@resource-id="com.hungry.panda.market:id/rv_country"]/android.view.ViewGroup[2]'

    """----输入验证码----"""
    code1 = '//*[@resource-id="com.hungry.panda.market:id/tvCode1"]'
    code2 = '//*[@resource-id="com.hungry.panda.market:id/tvCode2"]'
    code3 = '//*[@resource-id="com.hungry.panda.market:id/tvCode3"]'
    code4 = '//*[@resource-id="com.hungry.panda.market:id/tvCode4"]'
    code5 = '//*[@resource-id="com.hungry.panda.market:id/tvCode5"]'
    code6 = '//*[@resource-id="com.hungry.panda.market:id/tvCode6"]'
    # 重新发送
    resend = '//*[@resource-id="com.hungry.panda.market:id/tv_count_down"]'






