import pandas as pd
from sshtunnel import SSHTunnelForwarder
import pymysql

# excel表格导入
def read_file(file,shname):
    df = pd.read_excel(file,sheet_name=shname,header=1)
    return df

def read_file_basic(file,shname):
    df = pd.read_excel(file,sheet_name=shname)
    return df

# 数据库读写
def mysql_query(sql):
    server = SSHTunnelForwarder(ssh_address_or_host=('39.100.94.96', 22), ssh_username='root',
                                ssh_password='zmPissCMsOWF',
                                remote_bind_address=('rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com', 3306))
    server.start()
    db = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user='jusr2mmi49d8', passwd='uEZBjc9tQwoN',
                         db='e3', charset='utf8')
    cur = db.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    db.commit()
    return results


def mysql_query_kd(sql,zh,mm):
    server = SSHTunnelForwarder(ssh_address_or_host=('39.100.94.96', 22), ssh_username=zh,
                                ssh_password=mm,
                                remote_bind_address=('rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com', 3306))
    server.start()
    db = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user='jusr2mmi49d8', passwd='uEZBjc9tQwoN',
                         db='e3', charset='utf8')
    cur = db.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    db.commit()
    return results


# 日志文件，流文件  a 追加模式
def w_file(files,contents):
    with open(files,'a') as fwr:
        fwr.write(contents)