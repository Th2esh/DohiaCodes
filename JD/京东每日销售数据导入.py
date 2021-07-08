import pandas as pd
import datetime
import pymysql
import logging
import os
import time

def timesinfo(days):
    import time
    return time.strftime("%Y-%m-%d",time.localtime(int(time.time()-int(days)*86400)))


st = timesinfo(1)


#连接数据库
db = pymysql.connect(host='192.168.20.12', user='ych', password='123456', database='qudao_sale', port=3306,
                     charset='utf8')
cur = db.cursor()


#读入数据表
df = pd.read_excel('jd.xlsx')
df = df[['商品编码','商品名称','区域','昨日销量']]
df_pan = pd.read_excel('京东自营盘货表.xlsx',sheet_name = '7月盘货表')
df_pan1 = df_pan[['sku','货号']]
pd.set_option('display.max_columns',10)

#修改字段名
df.rename(columns = {'商品编码':'bh','商品名称':'mc','区域':'qy','昨日销量':'sl'},inplace = True)
df_pan1.rename(columns = {'sku':'bh','货号':'hh'},inplace = True)

#填充缺失项
df = df.fillna(0)
df_pan1 = df_pan1.fillna(0)

#将bh,hh字段统一修改为字符串格式
df['bh'] = df['bh'].apply(lambda x: str(x))
df['sl'] = df['sl'].apply(lambda x: int(x))
df_pan1['bh'] = df_pan1['bh'].apply(lambda x: int(x))
df_pan1['hh'] = df_pan1['hh'].apply(lambda x: int(x))
df_pan1['bh'] = df_pan1['bh'].apply(lambda x: str(x))
df_pan1['hh'] = df_pan1['hh'].apply(lambda x: str(x))

 #连接两个表
df = pd.merge(df,df_pan1,how = 'left',on = 'bh')

#增加日期列和店铺列
df['rq'] = ""+st+""
df['dp'] = '京东自营'

#重排列的顺序
df = df.reindex(columns = ['dp','rq','bh','hh','mc','sl','qy'])

#除去不要的行以及垃圾数据
df = df[df['qy'].isin(['全国'])]

#删除多余字段
df.drop(df.columns[[6]],axis = 1,inplace = True)


df = df.astype(object).where(pd.notnull(df), None)
df.to_excel(r"\\192.168.20.66\fileshare\IT部\个人文件\燕江洪\※每日销售数据\京东自营\京东自营_"+st+".xlsx",index = False)

#将数据写入数据库
columns = ','.join(list(df.columns))
data_list = [tuple(i) for i in df.values]
s_count = len(data_list[0]) * "%s,"

with db.cursor() as cursor:
    try:
        sql = "insert into jdzy_sale("+columns+") value("+s_count[:-1]+")"
        cursor.executemany(sql,data_list)
        db.commit()
    except:
        logging.exception("exception")
        db.rollback()
db.close()
os._exit(0)



























