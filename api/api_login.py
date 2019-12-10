import requests

import api


class ApiLogin:

    # 初始化
    def __init__(self):
        # 初始化url  ---> 调用init里的BASE_URL,导api包
        self.url = api.BASE_URL + "/api/sys/login"



    # 登录
    def api_login(self,mobile,password):
        # 定义json字符串 data = {手机号,密码}
        data = {"mobile": mobile, "password": password}

        # 请求登录 ---> post
        return requests.post(url=self.url,json=data,headers=api.headers)

