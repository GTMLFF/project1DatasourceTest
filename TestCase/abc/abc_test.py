# -*-conding:utf-8-*-

import sys
sys.path.append('E:\\TEST\\DataSourceTest')#否则在命令行中执行会报错，找不到common包
import pytest
from commons import Request
from commons import Assert
from data.abc import abcData
from commons import Result
import os
import json




#把案例保存到excel文件中
def saveResult(filename,i,param,response,expected_msg,passOrNot,url):
    path = 'abc\\' + os.path.abspath(__file__).split('\\')[-1].split('.')[0] + filename#这里不用jsondata的原因是，dumps序列化时对中文默认使用的ascii编码，如果指定ensure_ascii=False，可以输出想要的中文，但是在执行调接口时又会报错
    result = Result.Result(path, url, i, str(param), response,expected_msg, passOrNot)
    result.saveExcel()

#response 要看text和status_code
#response["text"]["code"]：01,210,10002的时候系统提示的错误
#response["text"]["code"],200的时候是查询成功，但是查询成功并不代表数据没问题
#response["text"]["data"]['status']为1时正常
#response["text"]["data"]['status']为2时表示有错误
#response["text"]["data"]['errorMessage']的错误


# 不能为空验证
@pytest.mark.parametrize('param', abcData.blank_test_data)
def test_paramBlank(param,setabcUrl):
    i = abcData.blank_test_data.index(param)+1
    param = json.dumps(param)
    req = Request.Request()
    response = req.post_request(setabcUrl, param, {'Content-Type': 'application/json'})
    a = Assert.Assert()
    a.assert_scode(response["status_code"], 200, i)
    a.assert_expect_in_text( '不能为空',response["text"],i)
    interfaceRes = json.loads(response["text"])
    passOrNot =  a.assert_data_in_expect('code',interfaceRes["code"], '210', i)
    saveResult('_blank_test_data',i,param,response["text"],"不能为空",passOrNot,setabcUrl)


if __name__ == "__main__":
    pass
