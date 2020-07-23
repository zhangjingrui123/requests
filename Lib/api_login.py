'''
封装登录接口
'''
import requests,json
class LoginClass:
    def login(self,loginparams):
        login_url = "http://47.111.108.116:8082/1.0/app/user/login"
        content_type = {"Content-Type":"application/json"}
        response = requests.post(login_url,headers=content_type,json=loginparams)
        return response.json()
        
# if __name__ == "__main__":
#     LoginClass().login({"account":"15266905059","password":"123456"})                                #请求传入的是字典
