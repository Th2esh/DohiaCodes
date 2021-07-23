import pandas as pd
import pymysql
import logging
import os
#这是一个测试Git是否生效的语句
st = '2021-07-22'

#连接数据库
db = pymysql.connect(host='192.168.20.12', user='ych', password='123456', database='qudao_sale', port=3306,
                     charset='utf8')
cur = db.cursor()

#导入数据表
df = pd.read_excel('123.xlsx')
df = df[['商品编码','商品名称','区域','可用库存','采购未到货']]
pd.set_option('display.max_columns',20)

#修改所需数据格式
df['商品编码'] = df['商品编码'].apply(lambda x: str(x))
df['可用库存'] = df['可用库存'].apply(lambda x: int(x))
df['采购未到货'] = df['采购未到货'].apply(lambda x: int(x))

#计算总库存
df['qgzkc'] = df['可用库存'] + df['采购未到货']

#删除多余字段
df.drop(df.columns[[3,4]],axis = 1,inplace = True)

#将区域字段进行透视
df = df.groupby(['商品编码', '商品名称','区域'], as_index = False)['qgzkc'].sum().pivot(['商品编码', '商品名称'], '区域', 'qgzkc')

#填充空缺项
df = df.fillna(0)

#更改数据格式
df= df.applymap(lambda x: int(x))

#将索引还原为字段
df = df.reset_index()

#修改字段名
df.rename(columns = {'商品编码':'bh','商品名称':'mc','全国':'qgzkc','北京':'bjkc','德州':'dzkc','上海':'shkc','广州':'gzkc','成都':'cdkc','武汉':'whkc','沈阳':'sykc','西安':'xakc'},inplace=True)

#新增一个日期列
df['rq'] = ""+st+""

#调整字段顺序
df = df.reindex(columns = ['rq','bh','mc','qgzkc','bjkc','dzkc','shkc','gzkc','cdkc','whkc','sykc','xakc'])

#除去不要的行
df = df[~df['qgzkc'].isin([0])]

#将数据保存到特定文件夹
df.to_excel(r"\\192.168.20.66\fileshare\IT部\个人文件\燕江洪\※每日销售数据\京东自营库存\库存导入_"+st+".xlsx",index = False)


#将数据写入数据库
columns = ','.join(list(df.columns))
data_list = [tuple(i) for i in df.values]
s_count = len(data_list[0]) * "%s,"

with db.cursor() as cursor:
    try:
        sql = "insert into jdzy_kc("+columns+") value("+s_count[:-1]+")"
        cursor.executemany(sql,data_list)
        db.commit()

    except:
        logging.exception("exception")
        db.rollback()

db.close()
os._exit(0)
























