# 可以通过key来找到对应的value
"""
定义字典字面量：{key: value, key: value,......} 是键值对
定义字典变量：名称 = {......}
定义空字典：名称 = {} 或 名称 = dict()
"""
my_dict = {"trq": 95, "hza": 90, "wyq": 100}
# 字典中的key不能重复
# 基于字典中的key来获取value:"字典名[key]"
score = my_dict["wyq"]
print(score)
# 字典的key和value可以是任何类型的（key不能为字典），即可以嵌套
dict1 = {
    "yjp": {
        "语文": 90,
        "数学": 100,
        "英语": 80
    }, "trq": {
        "语文": 93,
        "数学": 98,
        "英语": 87
    }, "wyq": {
        "语文": 80,
        "数学": 73,
        "英语": 75
    }
}
# 从嵌套字典中获取数据："字典[key1][key2]"
q = dict1["wyq"]["语文"]
print(f"wyq的语文成绩为{q}")