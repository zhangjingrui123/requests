'''
登录测试用例
'''

import sys,json,xlrd,pytest,allure,os
sys.path.append("..")
from Lib.api_login import LoginClass
from Lib.api_getexceldata import get_exceldata

@allure.feature("登录模块")
@allure.story("登录接口")
@pytest.mark.login                                                                   #打标识，指定运行
@pytest.mark.parametrize("test_number,request_param",get_exceldata("登录",1,3,6))    #把excel单元格数据参数化，封装成列表（可迭代对象）
def test_case(test_number,request_param):
    para_dict = json.loads(request_param)
    response = LoginClass().login(para_dict)
    if response["code"] == 200:
        print(f"用例编号：{test_number} | 请求传入的参数是{request_param} | 响应返回结果是：%s" % response["message"])
    else:
        print(f"用例编号：{test_number} | 请求传入的参数是{request_param} | 响应返回结果是：%s" % response["message"])
 

if __name__ == "__main__":
    pytest.main(["test_login.py","-s","--alluredir","../Report/temp"])
    os.system("allure generate  ../Report/temp -o  ../Report/report  --clean")

