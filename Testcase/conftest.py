print("--------------------环境数据初始化-----------------------")
import pytest,sys,os
sys.path.append("E:\package1\module6\Lib")
sys.path.append("E:\package1\module6\Config")
from api_login import LoginClass
from api_room import RoomClass
from Config.config import list_roomparams
@pytest.fixture(scope="function",autouse=False)
def delete_room():
    #登录
    token = LoginClass().login({"account":"15266905059","password":"123456"})["data"]["token"]
    # 列出课程
    response = RoomClass().list_room(token,list_roomparams)
    room_id = response["data"]["find_room_type"][0]["id"]
    print(room_id)
    #删除课程
    res = RoomClass().delete_room(token,{"id":room_id})
    print(res["message"])
    
# if __name__ == "__main__":
#     pytest.main(["conftest.py","-s"])