# -*-conding:utf-8-*-

from configparser import ConfigParser
from commons import Log
import os


class Config:
    def __init__(self):
        self.config = ConfigParser()
        self.log = Log.MyLog()

        # path = os.path.dirname(os.path.dirname(os.path.realpath('__file__')))
        path = 'E:\\TEST\\DataSourceTest\\'
        self.config_path = path +'\\config'+'\\config.ini'
        # print(self.config_path)
        if not os.path.exists(self.config_path):
            self.log.error("请确保配置文件存在！")
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.config_path,encoding='utf-8')



    def get_value(self,title,option):
        result = self.config.get(title,option)
        if title =='ip_port':
            self.log.info("获取到ip和端口号的值为：{}".format(result))
        else:
            self.log.info("获取接口地址的值为：{}".format(result))
        return result
        # print(ip_port)


    def add_title(self,title):
        self.config.add_section(title)
        self.log.info("配置文件添加title:" + title)
        with open(self.config_path,"w") as f:
            return self.config.write(f)

    def add_optionandvalue(self,title,option,value):
        self.config.set(title,option,value)
        self.log.info("配置文件添加title:" + title)
        self.log.info("配置文件添加option:" + option)
        self.log.info("配置文件添加value:" + value)
        with open(self.config_path,"w") as f:
            return self.config.write(f)



if __name__ == "__main__":
    c = Config()
    c.add_optionandvalue('kk','ee','1')