import os
import shutil
import time

from Base.Driver import Driver


class Base:

    def __init__(self):
        """声明driver"""
        self.driver = Driver().get_app_driver()

    @classmethod
    def os_clear(cls):
        return os.system('adb shell pm clear com.hungry.panda.market')

    def remove_report(self):
        path = os.path.abspath('.') + "/report/"
        # Get directory name
        # dir = input(path)
        try:
           return shutil.rmtree(path)
        except OSError as e:
            return print("Error: %s - %s." % (e.filename, e.strerror))

    def start(self):
        """启动app"""
        return self.driver.app_start("com.hungry.panda.market")

    def search_ele(self, loc):
        """定位元素xpath方法,并加上等待时间,默认10s"""
        return self.driver.xpath(loc).wait()

    def search_ele_id(self,loc):
        """定位元素id方法"""
        return self.driver(resourceId=loc).wait()

    def search_ele_text(self, loc, text):
        return self.driver(resourceId=loc, text=text).wait()

    def click_ele(self, loc):
        """点击方法xpath"""
        self.search_ele(loc).click()

    def click_ele_id(self, loc):
        """点击方法id"""
        self.search_ele_id(loc).click()

    def click_xy(self,x, y):
        "点击坐标方法"
        self.driver.click(x, y)

    def click_ele_xpath_text(self, loc, text):
        self.search_ele_text(loc, text).click()

    def set_ele(self, loc, text):
        """输入文本方法1-直接定位元素中text值"""
        self.driver(text=loc).set_text(text)

    def send_ele(self, text, clear=True):
        """输入文本方法2-前提需要先点击到元素位置"""
        self.driver.send_keys(text, clear)

    def press_enter_ele(self):
        self.driver.press("enter")

    def swipe(self,x,y,z,i):
        return self.driver.swipe(x,y,z,i)

    def sys_back(self):
        return self.driver.press("back")

    def get_text_xpath(self, loc):
        """获取元素文本信息"""
        return self.search_ele(loc).text

    def get_title_text(self,loc):
        return self.search_ele(loc).get_text()

#
# if __name__ == '__main__':
#     # os.system('adb shell pm clear com.hungry.panda.market')
#     Base().start()
#     Base().set_ele("搜索商品", "ui")
#     Base().remove_report()
    # base().start()
    # time.sleep(3)
    # text = base().get_text(pageElements.allow)
    # print(text)
    # Driver.quit_app_driver()
