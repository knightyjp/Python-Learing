my_dict = {"trq": 98, "hza": 90, "wyq": 100, "yjp": 80}
# 新增元素："字典[key] = value"
# 更新元素："字典[key] = value" (key不存在时是新增，存在时是更新)
print(my_dict)
# 删除元素:"字典.pop(key)"
my_dict.pop("yjp")
print(my_dict)
# 清空元素："字典.clear()"
my_dict.clear()
print(my_dict)

# 获取字典中全部的key："字典.keys()"
my_dict = {"trq": 98, "hza": 90, "wyq": 100, "yjp": 80}
d = my_dict.keys()
print(d)

# 遍历字典
# 1.通过key来遍历
for keys in d:
    print(f"本次参与考试的人有{keys}")
    print(f"他的得分为{my_dict[keys]}")
# 2.直接遍历
for keys in my_dict:
    print(f"本次参与考试的人有{keys}")
    print(f"他的得分为{my_dict[keys]}")

# 统计字典中的元素数量："len(字典)"
num = len(my_dict)
print(num)