import pandas as pd
import pymysql
from pandas.core import apply
from sshtunnel import SSHTunnelForwarder
import os
import time
import datetime
from dingding import dingmessage

def qushu():
    server= SSHTunnelForwarder(ssh_address_or_host=('39.100.94.96',22),
                                ssh_username='efast',ssh_password='51ksCg7eZ!VUgNx',
                                remote_bind_address=('rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com' , 3306))
    server.start()
    db = pymysql.connect(host='127.0.0.1',port=server.local_bind_port,user='jusr2mmi49d8',
                        passwd='uEZBjc9tQwoN',db='e3',charset='utf8')

    cur = db.cursor()

    # old : 639459253449|wy642351881895
    #642351881895  7.15日

    cur.execute("SELECT taobao_refunds_trade_items.outer_id AS outsku, taobao_refunds_trade_items.sku AS ggms, "
                "sum( taobao_refunds_trade_items.num ) AS sl FROM taobao_refunds_trade, taobao_refunds_trade_items WHERE taobao_refunds_trade.trid = taobao_refunds_trade_items.trid AND taobao_refunds_trade_items.num_iid = 644828773154 GROUP BY outsku, ggms")

    # cur.execute("SELECT taobao_refunds_trade_items.outer_id AS outsku, taobao_refunds_trade_items.sku AS ggms, "
    #             "sum( taobao_refunds_trade_items.num ) AS sl FROM taobao_refunds_trade, taobao_refunds_trade_items WHERE taobao_refunds_trade.trid = taobao_refunds_trade_items.trid AND taobao_refunds_trade_items.num_iid = 648584312113 GROUP BY outsku, ggms")

    dt = cur.fetchall()

    row1 = []
    for row in dt:
        row1.append(list(row))


    colm = ['货号','商品属性','数量']
    df = pd.DataFrame(data = row1,columns = colm)

    df1 = df['商品属性']

    s = []
    for i in df1:
        # regex = '("适用床尺寸:").[a-zA-z0-9_]*'
        # regex = re.compile(r'\d+')
        # s.append(re.findall(regex, i))
        # s.append(i[20:24]+" | "+i[52:])
        # s.append(i.find(':',2))
        # s.append(i)

        s.append(i[20:24]+' '+i[36:43])

    new_hh = df['货号'].to_list()
    new_sl = df['数量'].to_list()
    tp_en = str(pd.DataFrame({'货号':new_hh,'属性':s,'数量':new_sl}))
    # print(datetime.datetime.now().strftime('%H-%M-%S'))
    # print(tp_en)
    # print('\n')
    # tp_en.to_excel('zhibo2_'+str(datetime.datetime.now().strftime('%H%M%S'))+'.xlsx', index=False)
    # print('###')
    # time.sleep(120)
    return tp_en


def timeChanged(dt):
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timeStamp = time.mktime(timeArray)
    return timeStamp

if __name__=="__main__":
    while time.time() < timeChanged("2021-07-27 09:30:00"):
        dingmessage(qushu())
        print(datetime.datetime.now().strftime('%H:%M:%S'))
        time.sleep(900)





















