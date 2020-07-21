# -*-conding:utf-8-*-
import sys
sys.path.append('D:\\Users\\tina.gong\\Pycharmprojects\\untitled')#否则在命令行中执行会报错，找不到common包
import pytest
from commons import Request
from commons import Assert
from data.tianChuang import tianChuang_creditSinanData
from commons import Result
import os
import json




#把案例保存到excel文件中
def saveResult(filename,i,param,response,expected_msg,passOrNot,url):
    path = 'tianChuang\\' + os.path.abspath(__file__).split('\\')[-1].split('.')[0] + filename#这里不用jsondata的原因是，dumps序列化时对中文默认使用的ascii编码，如果指定ensure_ascii=False，可以输出想要的中文，但是在执行调接口时又会报错
    result = Result.Result(path, url, i, str(param), response,expected_msg, passOrNot)
    result.saveExcel()

#response 要看text和status_code
#response["text"]["code"]：01,10000,10002的时候系统提示的错误
#response["text"]["code"],200的时候是查询成功，但是查询成功并不代表数据没问题
#response["text"]["data"]['status']为1时正常
#response["text"]["data"]['status']为2时表示有错误
#response["text"]["data"]['errorMessage']的错误


# 参数缺失验证
@pytest.mark.parametrize('param', tianChuang_creditSinanData.blank_test_data)
def test_paramBlank(param,setCreditSiNanUrl):
    i = tianChuang_creditSinanData.blank_test_data.index(param)+1
    param = json.dumps(param)
    req = Request.Request()
    response = req.post_request(setCreditSiNanUrl, param, {'Content-Type': 'application/json'})
    a = Assert.Assert()
    a.assert_scode(response["status_code"], 200, i)
    passOrNot = a.assert_expect_in_text( '参数缺失',response["text"],i)
    interfaceRes = json.loads(response["text"])
    a.assert_data_in_expect('code',interfaceRes["code"], '10000', i)
    saveResult('_blank_test_data',i,param,response["text"],"参数缺失",passOrNot,setCreditSiNanUrl)



# 参数为空验证
@pytest.mark.parametrize('param', tianChuang_creditSinanData.missing_test_data)
def test_paramMissing(param,setCreditSiNanUrl):
    i = tianChuang_creditSinanData.missing_test_data.index(param)+1
    param = json.dumps(param)
    req = Request.Request()
    response = req.post_request(setCreditSiNanUrl, param, {'Content-Type': 'application/json'})
    a = Assert.Assert()
    a.assert_scode(response["status_code"], 200, i)
    passOrNot = a.assert_expect_in_text('参数缺失',response["text"],i)
    interfaceRes = json.loads(response["text"])
    a.assert_data_in_expect('code',interfaceRes["code"], '10000', i)
    saveResult('_missing_test_data',i,param,response["text"],"输入参数缺失",passOrNot,setCreditSiNanUrl)



# 能成功查到有效数据的案例
@pytest.mark.parametrize('param', tianChuang_creditSinanData.success_test_data)
def test_paramSucc(param,setCreditSiNanUrl):
    i = tianChuang_creditSinanData.success_test_data.index(param)+1
    param = json.dumps(param)
    req = Request.Request()
    response = req.post_request(setCreditSiNanUrl, param, {'Content-Type':'application/json'})
    a = Assert.Assert()
    a.assert_scode(response["status_code"], 200,i )
    print(response["text"])
    pass1 = a.assert_expect_in_text( 'SUCCESS', response["text"], i)
    pass2 = a.assert_expect_in_text( '"isFee":1', response["text"], i)
    pass3 = a.assert_expect_in_text( '"code":"0"', response["text"], i)
    passOrNot = (pass1 and  pass2 and pass3) ==True
    saveResult('_succ_test_data', i, param, response["text"], "成功,且收费", passOrNot,setCreditSiNanUrl)

@pytest.mark.parametrize('param', tianChuang_creditSinanData.history_test_data)
def test_paramHis(param,setCreditSiNanUrl):
    i = tianChuang_creditSinanData.history_test_data.index(param)+1
    param = json.dumps(param)
    req = Request.Request()
    response = req.post_request(setCreditSiNanUrl, param, {'Content-Type':'application/json'})
    a = Assert.Assert()
    a.assert_scode(response["status_code"], 200,i )
    print(response["text"])
    pass1 = a.assert_expect_in_text( '"message":"SUCCESS"', response["text"], i)
    pass2 = a.assert_expect_in_text( '"isFee":0', response["text"], i)
    pass3 = a.assert_expect_in_text( '"code":"0"', response["text"], i)
    passOrNot = (pass1 and  pass2 and pass3) ==True
    saveResult('_his_test_data', i, param, response["text"], "成功,不收费", passOrNot,setCreditSiNanUrl)

if __name__ == "__main__":
    pass