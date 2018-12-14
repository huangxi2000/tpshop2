import os

import yaml


class ReadYaml():
    def __init__(self, filename):
        # 获取文件名
        self.filename = os.getcwd() + os.sep + "data" + os.sep + filename

    # 读取yaml格式文件
    def read_yaml(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return yaml.load(f)
