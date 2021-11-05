import yaml, os


class GetData:

    @classmethod
    def get_yml_data(cls, name):
        """
        读取yaml数据
        :param name: 文件名字
        :return: 返回yaml数据
        """
        # 获取当前系统当前文件夹的上一级绝对路径
        path2 = os.path.abspath('.')
        with open(path2 + "/Data/" + name, "r", encoding="utf-8") as f:
            # 返回读取数据
            return yaml.safe_load(f)

# if __name__ == '__main__':
#     getData.getYmlData("login.yml")