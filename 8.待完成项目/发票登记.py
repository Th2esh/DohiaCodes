import pandas as pd
import pymysql
from sshtunnel import SSHTunnelForwarder
import os
import time
import datetime

def fapiao(sql):
    server = SSHTunnelForwarder(ssh_address_or_host=('39.100.94.96', 22),
                                ssh_username='efast', ssh_password='51ksCg7eZ!VUgNx',
                                remote_bind_address=('rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com', 3306))
    server.start()
    db = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user='jusr2mmi49d8',
                         passwd='uEZBjc9tQwoN', db='e3', charset='utf8')
    cur = db.cursor()
    cur.execute(sql)
    restult = cur.fetchall()
    return restult



df_list = pd.DataFrame()
s0 = "select deal_code from order_invoice where sd_id in (5,7,8,27,59,34,23,64) and DATE_FORMAT(lastchanged," \
     "'%Y-%m-%d') = " \
     "DATE_SUB(CURDATE(),INTERVAL 1 DAY)"
res0 = fapiao(s0)
print('len = '+str(len(res0)))

for i in res0:
    s1 ="select order_invoice.deal_code , kehu.khmc ,order_invoice.invoice_title  ,order_invoice.invoice_amount ," \
        "order_invoice.invoice_tax_no , " \
        "order_invoice.invoice_content , " \
        "order_invoice.invoice_type from " \
        "order_invoice,kehu where order_invoice.sd_id = kehu.id and order_invoice.deal_code = "+str(i[0])
    res1 = pd.DataFrame(fapiao(s1))
# # #
    s2 = "select '',goods_name,goods_number,share_price ,'','' from order_goods where deal_code = '"+str(i[0])+"'"
    res2 = pd.DataFrame(fapiao(s2))
    df = res1.append(res2)
    df_list = df_list.append(df)

df_list.to_excel('res.xlsx',index=False)
os._exit(0)


