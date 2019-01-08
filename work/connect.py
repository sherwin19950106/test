import pymysql.cursors
def startMysql():
    connect = pymysql.Connect(
        host='192.168.1.251',
        port=3306,
        user='root',
        passwd='zhongguankj123',
        db='xhcasenew',
        charset='utf8'
    )
    return connect



