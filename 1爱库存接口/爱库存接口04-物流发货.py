import requests
import json
import hashlib
import time
import random
import pandas as pd
from 测试专用 import rq


def hsmd(secert):
    str = secert
    m = hashlib.sha1()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_sha1 = m.hexdigest()
    return str_sha1

def akc_wlhc(contents):
    # 随机码获取区域
    s = "0123456789abcdefghijklmnopqrstuvwxyz"

    # 时间戳 取整数
    rt = int(time.time())
    # rt = '1622209257'

    # 8位随机码
    nc = ''.join(random.choices(s, k=8))
    # nc = '12341234'

    # 接口名
    ifn = "aikucun.delivery.order.logistics.send"

    # json数据
    js_data = contents

    dqm_data = "appid=2c9089947329762e01732c5b13105acd&appsecret=2c908c337329774b01732c5b14d2058c&body="+str(js_data)+"&format=json&interfaceName="+str(ifn)+"&noncestr="+str(nc)+"&timestamp="+str(rt)+"&version=1.0"


    sign_data = hsmd(dqm_data)
    # return sign_data


    url = "https://openapi.aikucun.com/route/rest?appid=2c9089947329762e01732c5b13105acd&sign="+str(
        sign_data)+"&format=json&interfaceName="+str(ifn)+"&version=1.0&noncestr="+str(nc)+"&timestamp="+str(rt)


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
        'Content-Type': 'application/json;charset=utf-8'
    }

    response = requests.post(url=url, data=js_data, headers=headers)
    data_rx = json.loads(response.text)
    return data_rx

def read_input_data():
    df  = pd.read_excel("6.xlsx")
    return df



if __name__ == '__main__':
    res = rq()
    order_code = []
    shipping_code = []
    shipping_sn = []
    #遍历获取到的值并写入到列表
    jj = res['data']['page']['pageTotal']
    for i in range(1, int(jj)+1, 1):
        for j in range(100):
            try:
                order_code.append(res['data']['orderListGets'][j]['deal_code'])
            except:
                pass

            try:
                shipping_sn.append(res['data']['orderListGets'][j]['shipping_sn'])
            except:
                pass

            try:
                shipping_code.append(res['data']['orderListGets'][j]['shipping_code'])
            except:
                pass
    # print(shipping_sn,shipping_code)

    new_shipping_code = []



    for x in shipping_code:
        if x == 'zto':
            new_shipping_code.append('zhongtong')
        elif x == 'sfsy':
            new_shipping_code.append('shunfeng')
        elif x == 'yto':
            new_shipping_code.append('yuantong')
        elif x == 'htky':
            new_shipping_code.append('huitongkuaidi')
        else:
            new_shipping_code.append('yunda')




    for y in range(len(new_shipping_code)):
        # time.sleep(1)
        try:
            print(order_code[y]+' '+str(y+1)+' '+akc_wlhc('{"adOrderId":"'+str(order_code[y])+'","isSplit":"0",'
                                                                              '"logisticsCode":"'+str(
                new_shipping_code[y])+'",'
                           '"logisticsNo":"'+str(shipping_sn[y])+'"}')['message'])
        except:
            pass




