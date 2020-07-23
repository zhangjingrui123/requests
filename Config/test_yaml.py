import yaml
#读取yaml数据
yaml_path = "./test.yaml"
firl1 = open(yaml_path,"r",encoding="utf-8")
print(yaml.load(firl1,Loader=yaml.FullLoader))

#写入yaml数据
firl2 = open(yaml_path,"w",encoding="utf-8")
data1 = {"name":"zjr","age":18}
data2 = [1,2,3,{"name":"tom","age":20}]
yaml.dump([data1,data2],firl2)