# 你想要怎样的生活
# 开发时间：2025/2/19 16:00
import yaml
import os
import configparser

ini_path = (os.path.join((os.path.dirname(os.path.dirname(os.path.realpath(__file__)))),'config','settings.ini'))

class FileRead():
    def __init__(self):
        self.ini_path = ini_path

    def read_data(self, filename):
        file_path = (os.path.join((os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'data', filename))
        f = open(file_path, encoding='utf8')
        data = yaml.safe_load(f)
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf8')
        return config

base_data = FileRead()