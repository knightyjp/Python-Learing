money = 50
print("钱包还有：", money)
money = money - 10
print("买了冰淇淋钱包还有", money, "元")
# 运算符
print("2+1=", 2+1)

# 单引号内包含双引号
name = '"yjp"'
print(name)

# 双引号内包含单引号
name2 = "'yjpp'"
print(name2)

# 变量拼接
name = "爱"
print("我" + name + "你")

# 全局变量
num = 200


def test():
    global num
    num = 500


test()
print(num)
# 通过global让外部的num和内部的num变成同一个，这就是全局变量