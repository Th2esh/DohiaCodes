import pandas as pd
import pymysql
from pandas.core import apply
from sshtunnel import SSHTunnelForwarder
import os
import numpy as np
import time
import datetime
from dingding import dingmessage

def qushu(sql):
    server = SSHTunnelForwarder(ssh_address_or_host=('39.100.94.96',22),
                                ssh_username='efast',ssh_password='51ksCg7eZ!VUgNx',
                                remote_bind_address=('rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com' , 3306))
    server.start()
    db = pymysql.connect(host='127.0.0.1',port=server.local_bind_port,user='jusr2mmi49d8',
                        passwd='uEZBjc9tQwoN',db='e3',charset='utf8')

    cur = db.cursor()

    # old : 639459253449|wy642351881895
    #642351881895  7.15日

    cur.execute(sql)
    dt = cur.fetchall()
    return dt
# aaa  =  "select sum(a.goods_number) as 未发货数量 from order_goods a,order_info b where goods_sn in ('114021451820320','114021454080330','114021451850320','114021454110330','114021451830320','114021454090330','114021451840320','114021454100330') and a.order_sn = b.order_sn and b.order_status in (0,1) and FROM_UNIXTIME(b.pay_time,'%Y-%m-%d %H:%i:%s') BETWEEN '2021-07-15 00:00:00' and '2021-07-31 23:59:59' "
#
# bbb = "select sum(a.goods_number) as 未发货数量 from order_goods a,order_info b where goods_sn in ('114021451820320','114021454080330','114021451850320','114021454110330','114021451830320','114021454090330','114021451840320','114021454100330') and a.order_sn = b.order_sn and b.order_status in (0,1) and FROM_UNIXTIME(b.pay_time,'%Y-%m-%d %H:%i:%s') BETWEEN '2021-07-15 00:00:00' and '2021-07-31 23:59:59' and  b.fhck_id = 3"
#
# ccc = "select sum(a.goods_number) as 未发货数量 from order_goods a,order_info b where goods_sn in ('114021451820320','114021454080330','114021451850320','114021454110330','114021451830320','114021454090330','114021451840320','114021454100330') and a.order_sn = b.order_sn and b.order_status in (0,1) and FROM_UNIXTIME(b.pay_time,'%Y-%m-%d %H:%i:%s') BETWEEN '2021-07-15 00:00:00' and '2021-07-31 23:59:59' and b.fhck_id = 11"
#
# ddd = "select sum(a.goods_number) as 销售数量 from order_goods a,order_info b where goods_sn in ('114021451820320','114021454080330','114021451850320','114021454110330','114021451830320','114021454090330','114021451840320','114021454100330') and a.order_sn = b.order_sn and b.order_status != 3 and FROM_UNIXTIME(b.pay_time,'%Y-%m-%d %H:%i:%s') BETWEEN '2021-07-15 00:00:00' and '2021-07-31 23:59:59'  "
#
# eee = "select sum(a.goods_number) as 销售数量 from order_goods a,order_info b where goods_sn in ('114021451820320','114021454080330','114021451850320','114021454110330','114021451830320','114021454090330','114021451840320','114021454100330') and a.order_sn = b.order_sn and b.order_status != 3 and FROM_UNIXTIME(b.pay_time,'%Y-%m-%d %H:%i:%s') BETWEEN '2021-07-15 00:00:00' and '2021-07-31 23:59:59'  and b.fhck_id = 3"
#
# fff = "select sum(a.goods_number) as 销售数量 from order_goods a,order_info b where goods_sn in ('114021451820320','114021454080330','114021451850320','114021454110330','114021451830320','114021454090330','114021451840320','114021454100330') and a.order_sn = b.order_sn and b.order_status != 3 and FROM_UNIXTIME(b.pay_time,'%Y-%m-%d %H:%i:%s') BETWEEN '2021-07-15 00:00:00' and '2021-07-31 23:59:59'  and b.fhck_id = 11"

ggg ="select b.fhck_id, sum(a.goods_number) from order_goods a,order_info b where goods_sn in ('114021451820320','114021454080330','114021451850320','114021454110330','114021451830320','114021454090330','114021451840320','114021454100330') and a.order_sn = b.order_sn and b.order_status in (0,1) and FROM_UNIXTIME(b.pay_time,'%Y-%m-%d %H:%i:%s') BETWEEN '2021-07-15 00:00:00' and '2021-07-31 23:59:59'  GROUP BY b.fhck_id HAVING b.fhck_id in (0,3,11) ORDER BY b.fhck_id desc"

zongshu = qushu(ggg)

mm = zongshu[0][1]
nn = zongshu[1][1]
print(mm,nn)


# totale = qushu(aaa)[0][0]
#
# shanghai = qushu(bbb)[0][0]
#
# nantong = qushu(ccc)[0][0]
#
# totale1 = qushu(ddd)[0][0]
#
# shanghai1 = qushu(eee)[0][0]
#
# nantong1 = qushu(fff)[0][0]

# ct = [{'仓库':'总计','未发货':totale,'总单数':totale1},{'仓库':'上海仓','未发货':shanghai,'总单数':shanghai1},{'仓库':'南通仓','未发货':nantong,'总单数':nantong1}]
# df = pd.DataFrame(ct)
# text = str(df)
# print(text)
#
# def timeChanged(dt):
#     timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#     timeStamp = time.mktime(timeArray)
#     return timeStamp

# while time.time() < timeChanged("2021-07-17 23:59:59"):
#     print(datetime.datetime.now().strftime('%H:%M:%S'))
#     dingmessage()
#     time.sleep(600)



# if __name__=="__main__":
#     # mmm = tp_en
#     while 2 > 1:
#         dingmessage(qushu())
#         time.sleep(900)




















