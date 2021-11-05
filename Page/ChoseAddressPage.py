from Base.Base import Base
from Page.PageElements import PageElements


class ChoseAddressPage(Base):
    """选择地址页"""

    def __init__(self):
        super().__init__()

    def click_location(self):
        self.click_xy(PageElements.address_local_map_x,PageElements.address_local_map_y)