from work import connect

cursor = connect.startMysql().cursor()
sql = "SELECT F_NAME FROM t_task "
cursor.execute(sql)
results = cursor.fetchall()
for task in results:
    print(list(task)[0])

