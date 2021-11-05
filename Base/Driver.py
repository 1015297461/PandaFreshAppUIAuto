import uiautomator2 as u2

class Driver:

    @classmethod
    def get_app_driver(cls):
        """声明app driver"""
        app_driver = u2.connect()
        # 自带的隐式等待方法
        app_driver.implicitly_wait(15.0)
        return app_driver

    @classmethod
    def quit_app_driver(cls):
        """退出app driver"""
        cls.get_app_driver().app_stop("com.hungry.panda.market")