from work import connect
import requests
import json

header = {'content-type': 'application/json;charset=UTF-8'}
cursor = connect.startMysql().cursor()
sql = "SELECT F_MOBILE FROM t_user "
try:
    counts = 0
    cursor.execute(sql)
    results = cursor.fetchall()
    result=list(results)
    print('共有项：', len(result))
    for i in result:
        username = i[0]
        jsons = json.dumps({"loginName": username, "password": 123456})
        r = requests.post('http://192.168.1.250/api/login/login', data=jsons, headers=header)
        if r.json()['data']['detail'] == None:
            print('数据不完整')
            continue
        r = r.json()['data']['detail']['USER']
        sex = '男'
        if r['GENDER'] == 2:
            sex = '女'
        print('-----登陆的用户信息------')
        print('姓名：', r['USERNAME'])
        print('性别：', sex)
        print('I D ：', r['USER_ID'])
        print('电话：', r['MOBILE'])
        print('职位：', r['POSITION'])
        counts += 1
except Exception as e:
    raise e
finally:
    print('通过次数', counts)
    connect.startMysql().close()
