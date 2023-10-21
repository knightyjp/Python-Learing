# 集合最主要的特点是自带去重功能，并且内容无序
"""
定义集合的字面量：{元素, 元素, 元素, ...}
定义集合变量： 变量名称 = {...}
定义空集合：变量名称 = set()
"""
# 因为集合是无序的，所以不支持下标索引。但是可以修改
my_set = {5, "yjp", 9, "math", "faiz", 10, 5}
print(my_set)
# 集合的添加："集合.add(元素)"
my_set.add(20)
print(my_set)
# 移除元素："集合.remove(元素)"
my_set.remove(10)
print(my_set)
# 从集合中随机取出一个元素："集合.pop()"   因为没有下标所以取出是随机的
i = my_set.pop()
print(i)
# 清空一个集合：clear
my_set.clear()
print(my_set)
# 统计集合元素："len()"

# 取出两个集合的差集："集合1.difference(集合2)"  (集合1有而集合2没有的,不会改变集合本身并生成一个新集合)
set1 = {2, 3, 6}
set2 = {2, 4, 8}
set3 = set1.difference(set2)
print(set3)
# 消除两个集合的差集："集合1.difference_update(集合2)" (在集合1内消除与集合2相同的元素，只改变1不改变2)
set1.difference_update(set2)
print(set1)
# 两个集合的合并："集合1.union(集合2)"  (保持1、2不变并合并一个新集合)
set4 = set3.union(set2)
print(set4)

# 集合的遍历
# 因为不能用下标所以不能使用while，但可以使用for
for x in set4:
    print(x)