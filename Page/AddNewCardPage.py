from Base.Base import Base
from Page.PageElements import PageElements


class AddNewCardPage(Base):
    """新增卡信息页"""

    def __init__(self):
        super().__init__()

    def add_new_card(self, card_num, card_cvv, postcode9):
        self.click_ele(PageElements.card_num)
        self.send_ele(card_num)
        self.click_ele(PageElements.valid_date)
        self.click_ele(PageElements.delivery_date)
        self.click_ele(PageElements.delivery_time)
        self.click_xy(0.51, 0.964)
        self.click_ele(PageElements.cvv_number)
        self.send_ele(card_cvv)
        self.click_ele(PageElements.til_postcode)
        self.send_ele(postcode9)
        Base().sys_back()
        self.click_xy(0.51, 0.964)


