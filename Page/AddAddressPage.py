from Base.Base import Base
from Page.PageElements import PageElements


class AddAddressPage(Base):
    """新增地址页"""

    def __init__(self):
        super().__init__()

    def send_address_detail(self, name, phone_num, postcode, build_name, unit):
        """输入地址详情"""
        self.set_ele(PageElements.contact_name, name)
        self.set_ele(PageElements.phone, phone_num)
        self.click_ele(PageElements.postcode_id)
        self.send_ele(postcode)
        self.set_ele(PageElements.build, build_name)
        self.set_ele(PageElements.unit, unit)
        self.click_ele(PageElements.tag_home)
        self.click_ele(PageElements.true_address)

    def click_location(self):
        """点击地址栏进入选择地址页"""
        self.click_ele(PageElements.address_location)

