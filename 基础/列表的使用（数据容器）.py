# 列表用中括号[]表示
i = [2, "yjp", True, 9]
print(i)
print(type(i))

# 通过下标索引来取出数据
print(i[0])
print(i[-1])
# 可正向索引也可以反向索引

# 嵌套列表的下标索引
j = [[2, "wyq"], [5, "yjp"]]
print(j[0][1], j[1][1])

# 列表的常用操作和特点

# 列表的查询功能 "列表.index(元素)"告诉元素下标索引值(嵌套列表不能查)
index = i.index("yjp")
print(index)

# 修改特定位置的元素值："列表[下标]=值"，相当于对指定位置重新赋值
i[3] = 5
print(i)

# 在指定下标位置插入指定元素："列表.insert(下标, 元素)"
i.insert(1, "好好好")
print(i)

# 追加元素，将元素追加到列表的尾部："列表.append(元素)"
i.append("wyq")
print(i)
# 追加一批元素："列表.extend(其他数据容器)"

# 元素的删除："del 列表[下标]"或"列表.pop(下标)" (pop相当于取出元素,del是直接删除)
del i[0]
print(i)
q = i.pop(3)
print(i)
print(q)
# 删除指定的元素："列表.remove(元素)" 从前往后删除找到的第一个元素
i.remove(True)
print(i)
# 删除列表内容："列表.clear()"
j.clear()
print(j)

# 统计某元素在列表中的数量："列表count(元素)"
print(i.count("wyq"))

# 统计列表内有多少元素："len(列表)"
print(len(i))