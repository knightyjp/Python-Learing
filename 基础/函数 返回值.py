# 返回值是程序中函数完成事情后，最后给调用者的结果
def add(x, y):
    result = x * y
    print("111")
    return result


r = add(4, 5)
print(r)
# return 相当于是一个函数的终止符，return后面的代码函数都不会执行
# 在if判断中none等同于false