# 字符串是字符的容器，一个字符串可以存放任意数量的字符
name = "my chemistry is good"
# 这就相当于是一个字符串，其中每个字母都是一个字符，也能用下标来表示，只读 并不能修改

# 字符串的替换，将字符串1，替换为字符串2："字符串.replace(字符串1， 字符串2)"
"""
替换后是给的返回值，需要用一个变量去接收它
"""
new = name.replace("good", "bad")
print(new)

# 字符串的分割："字符串.split(分隔符字符串)"  将字符串中的元素通过空格划分为多个字符串并存入列表对象中
change = name.split("is")
# 分隔符不会显示在结果中
print(change)

# 字符串的规整操作："字符串.strip()"。 括号中不写则去掉前后空格，写了则去掉前后相应指定内容（与中间内容无关）
kick = name.strip("od")
print(kick)
"""
strip去掉的是字符，不是单词，od是单独分别去除的，效果与写do是相同的
"""

# 字符串.count(字符串)与len(字符串)都是可以正常使用的。前者计算出现次数 后者计算字符串长度