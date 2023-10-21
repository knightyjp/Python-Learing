name = "switch switch switch"
num = 0
for x in name:
    if x == "i":
        num += 1
print("句子中有%s个i" % num)

for j in range(2):
    print("送")
# range规定的是for循环的次数
# 可在for循环中加入”continue“来中止当此循环并继续下一次循环（类似反复循环同一个语句）
# 使用”break“语句可直接中止整个for循环，直接进行下一步
