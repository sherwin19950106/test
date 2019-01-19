str = input('输入学生信息')
if ';' not in str:
    print('没有分号')
else:
    str = str.strip().split(';')
    for stu in str:
        if len(stu) == 0 or ',' not in stu :
            print('没有逗号或者没有值')
            continue
        str1 = stu.split(',')
        name = str1[0].strip()
        age = str1[1].strip()
        print('{:<20}:{:>02};'.format(name, age))
