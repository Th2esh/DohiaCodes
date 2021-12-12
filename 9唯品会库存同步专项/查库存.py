import requests
import schedule
import os
import requests
from sshtunnel import   SSHTunnelForwarder
import pymysql
import pandas as pd
def myinterface06(sql,fields):
    url = "http://39.100.94.96/e3/dohia/interfaces/default_sql.php"
    data = {
        'sql_code': sql,
        'show_info': fields
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
    }
    response = requests.post(url=url, data=data, headers=headers)
    return response.text
a = "SELECT a.goods_name AS 商品名称,b.sku AS 货号,b.sl AS 冻结数量,b.ck_id_name AS 仓库名称 FROM goods a,spkcb b WHERE a.goods_sn=b.sku AND b.ck_id IN (7,41) AND sl > 0 AND b.sku IN (SELECT sku FROM spkcb WHERE ck_id=23 AND sl> 0)"
print(myinterface06(a,"商品名称,冻结数量,仓库名称,"))
# def mysql_query_results(sql):
#     import pandas as pd
#     from sshtunnel import SSHTunnelForwarder
#     import pymysql
#
#     server = SSHTunnelForwarder(ssh_address_or_host=('39.100.94.96', 22), ssh_username='efast',
#                                 ssh_password='51ksCg7eZ!VUgNx',
#                                 remote_bind_address=('rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com', 3306))
#     server.start()
#     db = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user='jusr2mmi49d8', passwd='uEZBjc9tQwoN',
#                          db='e3', charset='utf8')
#     cur = db.cursor()
#     cur.execute(sql)
#     results = cur.fetchall()
#     db.commit()
#     return results
# a  = "SELECT a.goods_name AS 商品名称,b.sku AS 货号,b.sl AS 冻结数量,b.ck_id_name AS 仓库名称 FROM goods a,spkcb b WHERE a.goods_sn=b.sku AND b.ck_id IN (7,41) AND sl > 0 AND b.sku IN (SELECT sku FROM spkcb WHERE ck_id=23 AND sl> 0)"
# print(mysql_query_results(a))