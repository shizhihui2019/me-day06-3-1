# 登录
import unittest
import api
from api.api_login import ApiLogin
from tools.assert_common import assert_common


# 创建测试类
class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        #  获取ApiLogin对象  --> 调用api_login类
        cls.login = ApiLogin()


    # 登录测试方法
    def test01_login(self,mobile="13800000002",password="123456"):
        # 调用业务方法
        r = self.login.api_login(mobile,password)

        # 提取token
        token = r.json().get("data")
        api.headers['Authorization'] = "Bearer " + token
        print("登录成功后的headers值为:",api.headers)

        # 断言
        print(r.json())
        # status_code 响应码状态
        # print(r.status_code)
        assert_common(self,r)



































