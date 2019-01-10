str = input('输入学生信息')
str = str.strip().split(';')
for stu in str:
    if len(stu) == 0 or ',' not in stu :
        continue
    str1 = stu.split(',')
    name = str1[0].strip()
    age = str1[1].strip()
    print('{:<20}{:>02};'.format(name, age))
