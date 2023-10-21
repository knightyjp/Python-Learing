# 函数参数的种类
# 位置参数：调用时根据函数定义的参数位置来传递函数
def user(name, age, gender):
    print(f"您的名字是{name}，年龄为{age}，性别为{gender}")


user("Sam", 19, "男")


# 关键字参数：传参时不需要固定位置(可以和位置参数混用，但是位置参数必须在关键字参数前面)
def user2(name, age, gender):
    print(f"您的名字是{name}，年龄为{age}，性别为{gender}")


user2(gender="女", age=19, name="wyq")


# 缺省参数：可以在函数中设定默认值，当不传入指定参数时就为默认值
def user3(name, age, gender="男"):
    print(f"您的名字是{name}，年龄为{age}，性别为{gender}")


user3("hza", 19)