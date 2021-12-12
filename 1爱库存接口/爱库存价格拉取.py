import requests
import json
import hashlib
import time
import random
import pandas as pd



def hsmd(secert):
    str = secert
    m = hashlib.sha1()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_sha1 = m.hexdigest()
    return str_sha1

def akc_jg(contents):
    # 随机码获取区域
    s = "0123456789abcdefghijklmnopqrstuvwxyz"

    # 时间戳 取整数
    rt = int(time.time())


    # 8位随机码
    nc = ''.join(random.choices(s, k=8))

    # 接口名
    ifn = "aikucun.delivery.trade.order.detail"

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




if __name__ == '__main__':
    df = pd.read_excel("ddd.xlsx", sheet_name="Sheet1")
    # print(df['dd'][0])
    # print(len(df['dd']))
    for i in range (len(df)):
        print(str(df['dd'][i])+"\t"+str(akc_jg('{"adOrderId":"'+df['dd'][i]+'"}')['data']['realPayAmount']))



