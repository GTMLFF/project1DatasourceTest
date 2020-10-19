# -*-conding:utf-8-*-
import pymysql
import json

class Mysql:
    def connectMysql(self):
        conn = pymysql.connect(host="",user ="", password ="12345678",database ="",charset ="utf8")
        # cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
        # 获取一个光标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 返回字典数据类型

        return  cursor


if __name__ =="__main__":
    m = Mysql()
    m.connectMysql()