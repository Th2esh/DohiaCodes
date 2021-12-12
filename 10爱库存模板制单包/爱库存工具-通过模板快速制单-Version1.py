# -*- coding:utf-8 -*-
import requests
import json
import hashlib
import time
import pandas as pd
import cpca

# 测试模型核心部件
# dongwu = ['dog','dog','cat','zera','lion','lion']
# wps = ['zoo','2','3','zoo','4','zoo']
# df = pd.DataFrame({'dongwu':dongwu,"weizhi":wps})
# print(df)

## 导入
df = pd.read_excel('2145-2205.xlsx')

####   处理basic表中货号转换和价格附加
df_b = pd.read_excel('货号对照表.xlsx')

new_goods_sn = []
new_jiage = []
for m in df['商品条码'].to_list():
    if m in df_b['商品条码'].to_list():
        p = df_b['商品条码'].to_list().index(m)
        new_goods_sn.append(df_b['商品货号'][p])
        new_jiage.append(df_b['商品供货价'][p])

###########更新DF
df['hh'] = new_goods_sn
df['ghj'] = new_jiage

# 通过遍历去重 找到唯一的订单好
order_list_new = []
for i in df['订单号'].to_list():
    if not i  in order_list_new:
        order_list_new.append(i)

# 通过遍历动物找每个动物需要对应的WPS
nx = []
nxgoods = []
for i in order_list_new:
    goodslist = []
    hpxx = []
    for j in range(len(df)):
        if i == df['订单号'][j]:
            hpxx.append({"收货人":df['收货人'][j],"收货地址":df['收货地址'][j],"联系电话":df['联系电话'][j],"商品条码":df['商品条码'][j],
                         "商品名称":df['商品名称'][j],"商品数量":df['数量'][j]})
            goodslist.append({"sku_sn":""+str(df['hh'][j])+"","goods_price":""+str(df['ghj'][j])+"",
                              "transaction_price": ""+str(df['ghj'][j])+"","goods_number": ""+str(df['数量'][j])+""})
        else:
            pass
    nx.append(hpxx)
    nxgoods.append(goodslist)

#########################
#########################
dts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

def jiage(tmp):
    pia = []
    for i in range(len(tmp)):
        pia.append(float(tmp[i]['goods_price'])*(float(tmp[i]['goods_number'])))
    return sum(pia)
def hsmd(secert):
    str = secert
    m = hashlib.md5()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return str_md5
def rq(input_data):
    # 单据编号的变量值
    dj_random = str(time.strftime("%Y%m%d%H%M", time.localtime()))
    # 时间参数
    rt = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    # 接口类型
    jk = 'order.detail.add'
    # json数据
    js_data = input_data

    dqm_data = "key=test&requestTime="+rt+"&secret=1a2b3c4d5e6f7g8h9i10j11k12l&version=3.0&serviceType="+jk+"&data" \
                                                                                                            "="+js_data
    sign_data = hsmd(dqm_data)
    # return js_data


    url = "http://39.100.94.96/e3/webopm/web/?app_act=api/ec&app_mode=func"

    params = {
        'key' : 'test',
        'sign' : sign_data,
        'requestTime' : rt,
        'version' : '3.0',
        'serviceType' : jk,
        'data' : js_data
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
    }
    response = requests.get(url=url, params=params, headers=headers)
    data = json.loads(response.text)
    return data

#### 正式执行 #####
print('本地执行一共'+str(len(order_list_new))+'单，执行开始... ...注意查看返回值... ...')
print('\n')

for i in range(len(order_list_new)):
    z_list =[]
    z_list.append(nx[i][0]['收货地址'])

    print(rq( '{"add_time": "'+str(dts)+'","order_sn": "'+str(order_list_new[i])+'","sd_code": "998","order_status":"1","consignee":"'+str(nx[i][0]['收货人'])+'","province_name": "'+str(cpca.transform(z_list).iat[0, 0])+'","city_name":"'+str(cpca.transform(z_list).iat[0,1])+'","district_name":"'+str(cpca.transform(z_list).iat[0, 2])+'","address":"'+str(cpca.transform(z_list).iat[0, 3])+'","pos_code":"1","pay_code": "alipay","vip_no": "1","shipping_code":"shunfeng","shipping_fee":"0.00","order_amount": "'+str(jiage(nxgoods[i]))+'","payment": "'+str(jiage(nxgoods[i]))+'","mobile":"'+str(nx[i][0]['联系电话'])+'","receiver_zip":"'+str(cpca.transform(z_list).iat[0, 4])+'","os_user_id": "1","items": '+str(nxgoods[i]).replace("'",'"')+'}'))