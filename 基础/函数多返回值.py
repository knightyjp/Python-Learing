# 用语法接收函数的多个返回值, 类型不受限
def test():
    return 2, "hello", True


x, y, z = test()
print(x)
print(y)
print(z)