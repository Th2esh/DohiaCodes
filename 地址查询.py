import requests
import json
import hashlib
import time
from datetime import datetime
import pandas as pd


from sshtunnel import SSHTunnelForwarder
import pymysql




new_order = []
st = datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "%Y-%m-%d %H:%M:%S")
df = pd.read_excel('客户地址查询.xlsx', sheet_name='Sheet1', header=0)
order = df['订单号'].to_list()
for j in order:
    new_order.append(str(j))


server = SSHTunnelForwarder(ssh_address_or_host=('39.100.94.96', 22), ssh_username='efast',
                            ssh_password='51ksCg7eZ!VUgNx',
                            remote_bind_address=('rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com', 3306))
server.start()
db = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user='jusr2mmi49d8', passwd='uEZBjc9tQwoN',
                     db='e3', charset='utf8')
dizhi = []
for i in order:
    cur = db.cursor()
    cur.execute("select user_name from order_info where order_sn  ='" + str(i) + "'")
    results = cur.fetchall()
    # res = results[0][0][0].replace(" ", "")
    res = results[0][0]
    # print(res)
    db.commit()
    dizhi.append(res)
    # dizhi = nicheng[0][0][0].replace(" ", "")


df = pd.DataFrame({"订单号":new_order,"顾客地址":dizhi})



df.to_excel('查询结果.xls', encoding='utf-8',index=False,sheet_name="顾客地址")


et = datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "%Y-%m-%d %H:%M:%S")
print('执行耗时：'+str((et-st).total_seconds())+' 秒')

