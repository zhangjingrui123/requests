'''
房型管理测试用例.批量执行测试用例
'''
import os,sys,pytest,xlrd,json,allure
sys.path.append("E:\package1\module6\Lib")
sys.path.append("E:\package1\module6\Config")
from api_login import LoginClass
from api_room import RoomClass
from api_getexceldata import get_exceldata
from config import list_roomparams
@allure.feature("房型模块")
class Test_Room:
    def setup_class(self):                         #每次执行脚本前自动执行setup_class
        self.token = LoginClass().login({"account":"15266905059","password":"123456"})["data"]["token"]
    @allure.story("新增房型接口")
    @pytest.mark.room_add
    @pytest.mark.parametrize("tc_number,request_param",get_exceldata("房型管理",1,4,6))
    def test_addroom_case(self,tc_number,request_param):
        add_response = RoomClass().add_room(self.token,json.loads(request_param))
        if add_response["code"] == 200:
            print(f"用例编号：{tc_number} | 请求传入的参数是：{request_param} | 返回响应结果是 %s " % add_response["message"])
        else:
            print(f"用例编号：{tc_number} | 请求传入的参数是：{request_param} | 返回响应结果是 %s " % add_response["message"])
    @allure.story("列出房型接口")
    @pytest.mark.room_list
    @pytest.mark.parametrize("tc_number,request_param",get_exceldata("房型管理",4,5,6))
    def test_list_case(self,tc_number,request_param):
        list_response = RoomClass().list_room(self.token,request_param)
        rooms = list_response["data"]["find_room_type"]
        for room in rooms:
            print(f"用例编号：{tc_number} | 请求传入的参数是：{request_param} | 已添加的房型名称有：%s" % room["room_name"])   
    @allure.story("删除房型接口")
    @pytest.mark.room_delete
    def test_delete_case(self):
        all_room = RoomClass().list_room(self.token,list_roomparams)["data"]["find_room_type"]
        for one_room in all_room:
            room_id = one_room["id"]
            delete_response = RoomClass().delete_room(self.token,{"id":room_id})
            if delete_response["code"] == 200:
                print("房型删除成功,返回的响应信息为: %s " % delete_response["message"])
            else:
                print("房型删除失败，返回的失败信息为：%s" % delete_response["message"])

if __name__== "__main__":
    pytest.main(["test_room.py","-s","--alluredir","../Report/temp"])
    os.system("allure generate  ../Report/temp -o  ../Report/report  --clean")

    


