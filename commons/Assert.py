# -*-conding:utf-8-*-

from commons import Log


class Assert:
    def __init__(self):
        self.log = Log.MyLog()

    #验证状态码
    def assert_scode(self,code,expected_code,i):
        try:
            assert code == expected_code
            self.log.info("******************************测试案例{}的状态码{}与预期一致" .format(i,code))
            return True
        except:
            self.log.error("******************************测试案例{}的状态码不是200，错误".format(i))
            # raise
            return False


    #验证某个参数的值，比如code的值，status的值，msg的值assert_data_in_expect('status','0000','0000',i)
    def assert_data_in_expect(self,param,data,expected_data,i):
        try:
            assert data  in expected_data
            self.log.info("******************************测试案例{}的{}={}，在预期结果({})中".format(i, param,data,expected_data))
            return True
        except:
            self.log.error("******************************测试案例{}的{}={}，不在预期结果({})中".format(i,param,data,expected_data))
            # raise
            return False

    # 验证某个参数的值，比如code的值，status的值，msg的值assert_data_in_expect('status','0000','0000',i)
    def assert_data_equal_expect(self, param, data, expected_data, i):
        try:
            assert  data == expected_data
            self.log.info("******************************测试案例{}的{}={}，符合预期({})".format(i, param, data,expected_data))
            return True
        except:
            self.log.error("******************************测试案例{}的{}={}，不符合预期({})".format(i, param, data,expected_data))
            # raise
            return False

    #验证返回的response.text中包含预期的内容
    def assert_expect_in_text(self, expected_msg,text,i ):
        try:
            assert expected_msg in text
            self.log.info("******************************开始匹配测试案例{}******************************".format(i))
            self.log.info("接口返回的:{}".format(text))
            self.log.info("接口返回包含预期字段:%s" % expected_msg)
            self.log.info("******************************测试案例{}匹配结束******************************".format(i))
            return True
        except:
            self.log.info("******************************开始匹配测试案例{}******************************".format(i))
            self.log.info("接口返回的:{}".format(text))
            self.log.error("响应信息中不包含预期字段:%s"%expected_msg)
            self.log.info("******************************测试案例{}匹配结束******************************".format(i))
            # raise
            return False

    #验证返回的response.text中不包含预期的内容
    def assert_expect_not_in_data(self,expected_msg, body ,i ):
        try:
            assert expected_msg not in body
            self.log.info("******************************开始匹配测试案例{}******************************".format(i))
            self.log.info("接口返回:%s" % body)
            self.log.info("接口返回不包含:%s" % expected_msg)
            self.log.info("******************************测试案例{}匹配结束******************************".format(i))
            return True
        except:
            self.log.info("******************************开始匹配测试案例{}******************************".format(i))
            self.log.info("接口返回:%s" % body)
            self.log.error("响应信息中存在:%s"%expected_msg)
            self.log.info("******************************测试案例{}匹配结束******************************".format(i))
            # raise
            return False



