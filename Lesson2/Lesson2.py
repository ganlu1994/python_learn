# Lesson2# listangiosperm = ["Amborellales", "Nymphaeales", "Austrobaileyales",              "Chloranthales", "Magnoliids", "Monocots",              "Ceratophyllales"]# 访问列表元素angiosperm[0]angiosperm[1:]angiosperm[:3]# 列表复制test_list = angiosperm[:]test_list = angiosperm.copy()test_list = angiosperm# 列表合并test_list += test_listtest_list.extend(test_list)# 列表常用方法angiosperm.pop(0)angiosperm.append("Eudicots")angiosperm.index("Eudicots")# 循环-遍历列表元素for i in angiosperm:    print(i)print("all angiosperms here".title())# 循环-range函数for i in range(0, 9):    print(str(i ** 2))for i in range(9, 0, -2):    print(str(i ** 2))# 循环-字符串迭代for i in angiosperm[0]:    print(i)"A" in angiosperm[0]# 条件判断age = 14if age < 5:    print("Kids")elif age < 18:    print("juvenile")else:    print("Adult")# 循环中途控制-continuefor i in range(0, 9):    if i % 2 == 0:        print(str(i ** 2))        continue    print(str(i))# 循环中途控制-breakfor i in angiosperm:    if i == "Magnoliids":        break    print(i)for i in angiosperm:    print(i)    if i == "Magnoliids":        break# 文件读with open("file") as fh:    for line in fh:        print(line)# 文件写with open("file", mode="w") as fh:    fh.write()# 文件同时读写with open("lesson2.fasta") as file_1, \        open("output.txt", "w") as file_2:    file_2.write(file_1.read())