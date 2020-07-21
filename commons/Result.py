# -*-conding:utf-8-*-
from commons import Excel
from commons import Log
import time
import os

class Result:
    def __init__(self,filename,url,i,param,response,expectmsg,passOrNot):
        self.filename = filename
        path = 'D:\\Users\\tina.gong\\PycharmProjects\\untitled\\Result\\' + self.filename+time.strftime("%Y-%m-%d %H-%M")+ '_Result.xls'
        print(self.filename)
        print(path)
        self.e = Excel.Excel(path)
        if os.path.exists(path):
            pass
        else:
            self.e.create_excel()
        self.log = Log.MyLog()

        self.url = url
        self.i = i
        self.param = param
        self.response = response
        self.expectmsg = expectmsg
        self.passOrNot = passOrNot



    def saveExcel(self):
        self.log.info("生成测试案例成功")
        self.e.update_excel(0, 1, "{}".format(self.url))
        self.e.update_excel(self.i+1, 0, "案例{}".format(self.i))
        self.e.update_excel(self.i+1, 1,str(self.param))  # 这里不用jsondata的原因是，dumps序列化时对中文默认使用的ascii编码，如果指定ensure_ascii=False，可以输出想要的中文，但是在执行调接口时又会报错
        self.e.update_excel(self.i+1, 2, self.response)
        self.e.update_excel(self.i+1, 3, self.expectmsg)
        self.e.update_excel(self.i+1, 4, self.passOrNot)
        self.e.update_excel(self.i+1, 5, time.strftime("%Y-%m-%d %H:%M:%S"))
