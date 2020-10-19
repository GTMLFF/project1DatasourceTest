# -*- conding:utf-8 -*-

import os
import xlrd
import xlwt
from xlutils.copy import copy

class Excel:
    def __init__(self,path):
        dir = os.path.dirname(path)
        if os.path.exists(dir):
            pass
        else:
            os.makedirs(dir)
        self.filename = path

    def create_excel(self):

        workbook = xlwt.Workbook(encoding='utf-8') #创建工作簿
        sheet = workbook.add_sheet('demo') #创建sheet
        title = ['案例编号','入参','测试结果','预期结果','是否通过','测试时间']
        sheet.write(0, 0, '接口地址')
        for i in range(len(title)):
            sheet.write(1,i,title[i])
        workbook.save(self.filename)

    def update_excel(self,m,n,value):
        oldWorkBook = xlrd.open_workbook(self.filename)
        newWorkBook = copy(oldWorkBook)
        newWorkBookSheet = newWorkBook.get_sheet(0)
        newWorkBookSheet.write(m,n,value)
        newWorkBook.save(self.filename)


if __name__ == '__main__':
    e = Excel("123")
    e.create_excel()
    e.update_excel()

