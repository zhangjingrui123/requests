'''
封装房型管理接口
'''
import requests,json,sys
sys.path.append("..")
from Config.config import list_roomparams
from api_login import LoginClass
class RoomClass:
    def add_room(self,token,params):
        roominfo_url = "http://47.111.108.116:8081/1.0/app/room_type/roomInfo"
        content_type = {"Content-Type":"application/json","Authentication":token}
        response = requests.post(roominfo_url,headers=content_type,json=params)     #传入字典
        return response.json()
    def list_room(self,token,params):
        app_url = "http://47.111.108.116:8081/1.0/app"
        content_type={"Content-Type": "application/graphql","Authentication":token}
        response = requests.post(app_url,headers=content_type,data=params)                     #传入字符串
        return response.json()
    def delete_room(self,token,params):
        delete_url="http://47.111.108.116:8081/1.0/app/room_type/deleteRoom"
        content_type = {"Content-Type": "application/json","Authentication":token}
        response = requests.post(delete_url,headers=content_type,json=params)
        return response.json()
    def modifiy_room(self,token,params):
        modifity_url = "http://47.111.108.116:8081/1.0/app/room_type/roomInfo"
        content_type = {"Content-Type": "application/json","Authentication":token}
        response = requests.post(modifity_url,headers=content_type,json=params)
        return response.json()

# if __name__ == "__main__":
#     token = LoginClass().login({"account":"15266905059","password":"123456"})["data"]["token"]
#     res = RoomClass().list_room(token,list_roomparams)
#     room_id = res["data"]["find_room_type"][0]["id"]
#     reson = RoomClass().delete_room(token,{"id":room_id})
#     print(reson)