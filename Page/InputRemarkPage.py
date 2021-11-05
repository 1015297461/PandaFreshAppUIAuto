from Base.Base  import Base
from Page.PageElements import PageElements


class InputRemarkPage(Base):
    """填写备注页面"""

    def __init__(self):
        super().__init__()

    def input_remark(self, remark):
        self.set_ele(PageElements.remark_text, remark)
        self.click_ele(PageElements.completed)


