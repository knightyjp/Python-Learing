# 函数：是组织好的，可重复使用的，用来实现特定功能的代码段
i = "i love you"
count = 0
for j in i:
    count += 1
print(f"字符串{i}的长度为{count}")

# 定义一个函数 并输出相关信息


def say_hi():
    print("你好")
# 空格内为传入参数，say_hi 为函数名，print为函数体，print下一行为return(返回值)可省略
# 使用函数需要调用函数


say_hi()