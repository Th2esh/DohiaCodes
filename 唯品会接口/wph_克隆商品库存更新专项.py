# -*- coding:utf-8 -*-

import hmac
import datetime
import requests
import json
import hashlib
import time
import pandas as pd
def dingmessage(xiaoxi):
# 请求的URL，WebHook地址
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=88578f695c2d361e07441f3bfc4de9af9536c2cfd436768e925899c679a43b31"
#构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
}
#构建请求数据
    tex = xiaoxi +"\n唯品会库存同步\n"+datetime.datetime.now().strftime('%H:%M:%S')
    message ={

        "msgtype": "text",
        "text": {
            "content": tex
        },
        "at": {

            "isAtAll": True
        }

    }
#对请求的数据进行json封装
    message_json = json.dumps(message)
#发送请求
    info = requests.post(url=webhook,data=message_json,headers=header)
#打印返回的结果
    print(info.text)
# 此函数在本接口中无效 系MD5加密 用于百胜接口
def hsmd(secert):
    str = secert
    m = hashlib.md5()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return str_md5

# 此函数为HMAC-MD5加密方式
def hmac_md5(key, value):
    message = value.encode('utf-8')
    return hmac.new(key.encode('utf-8'), message, digestmod=hashlib.md5).hexdigest()

def wph_kccx(contents):
    # 服务名
    service = 'vipapis.inventory.InventoryService'
    # 方法名
    method = 'getSkuStock'
    # 版本
    version = '1.0.0'
    # 时间参数
    # timestamp = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    timestamp = int(time.time())
    # timestamp = '1633941962'
    # 类型
    format = 'json'
    # key
    appKey = 'e79ed1c1'
    # secret
    appSecret = '42980F87296326370A34563DA67B28AA'
    accessToken = 'B569E6BE58AEC06CEB248B836DACAECDAF3D025F'
    # 请求变量 从形参传入 ...



    # dqm_data = "appKey"+str(appKey)+"format"+str(format)+"method"+str(method)+"service"+str(service)+"timestamp"+str(
    #     timestamp)+"version"+str(version)+str(contents)

    dqm_data = "accessToken"+str(accessToken)+"appKey"+str(appKey)+"format"+str(format)+"method"+str(method)+"service"+str(
        service)+"timestamp"+str(
        timestamp)+"version"+str(version)+str(contents)

    sign_data = hmac_md5(appSecret, dqm_data).upper()
    # return sign_data

    # url = "https://vop.vipapis.com/?service="+str(service)+"&method="+str(method)+"&version="+str(version)+"" \
    #       "&timestamp="+str(timestamp)+"&format="+str(format)+"&appKey="+str(appKey)+"&sign="+str(sign_data)

    url = "https://vop.vipapis.com/?service="+str(service)+"&method="+str(method)+"&version="+str(version)+"" \
          "&timestamp="+str(timestamp)+"&format="+str(format)+"&appKey="+str(appKey)+"&sign="+str(
        sign_data)+"&accessToken="+str(accessToken)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
    }

    # POST用法，url直接传str_query所以前面的url有用?&直接增加url传参，data传递post表格信息即应用请求

    response = requests.post(url=url, data=contents, headers=headers)
    data_re = json.loads(response.text)
    return data_re

def wph_kcgx(contents):
    # 服务名
    service = 'vipapis.inventory.InventoryService'
    # 方法名
    method = 'updateInventory'
    # 版本
    version = '1.0.0'
    # 时间参数
    # timestamp = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    timestamp = int(time.time())
    # timestamp = '1633941962'
    # 类型
    format = 'json'
    # key
    appKey = 'e79ed1c1'
    # secret
    appSecret = '42980F87296326370A34563DA67B28AA'
    accessToken = 'B569E6BE58AEC06CEB248B836DACAECDAF3D025F'
    # 请求变量 从形参传入 ...



    # dqm_data = "appKey"+str(appKey)+"format"+str(format)+"method"+str(method)+"service"+str(service)+"timestamp"+str(
    #     timestamp)+"version"+str(version)+str(contents)

    dqm_data = "accessToken"+str(accessToken)+"appKey"+str(appKey)+"format"+str(format)+"method"+str(method)+"service"+str(
        service)+"timestamp"+str(
        timestamp)+"version"+str(version)+str(contents)

    sign_data = hmac_md5(appSecret, dqm_data).upper()
    # return sign_data

    # url = "https://vop.vipapis.com/?service="+str(service)+"&method="+str(method)+"&version="+str(version)+"" \
    #       "&timestamp="+str(timestamp)+"&format="+str(format)+"&appKey="+str(appKey)+"&sign="+str(sign_data)

    url = "https://vop.vipapis.com/?service="+str(service)+"&method="+str(method)+"&version="+str(version)+"" \
          "&timestamp="+str(timestamp)+"&format="+str(format)+"&appKey="+str(appKey)+"&sign="+str(
        sign_data)+"&accessToken="+str(accessToken)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
    }

    # POST用法，url直接传str_query所以前面的url有用?&直接增加url传参，data传递post表格信息即应用请求

    response = requests.post(url=url, data=contents, headers=headers)
    data_re = json.loads(response.text)
    return data_re

def myinterface06(contents):
    url = "http://39.100.94.96/e3/dohia/interfaces/get_spkc_info.php?"
    params = {
        'splist' : contents,
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
    }
    response = requests.get(url=url, params=params, headers=headers)
    # data = json.loads(response.text,encoding='utf-8')
    return response.text

###########
# 1.读文件获取四列有效数据
df = pd.read_excel("clone_goods_10301.xlsx")
df = df[['克隆产品货号','克隆产品69码','产品货号','产品名称']]
# 2.根据产品货号获取E3库存
hh_string = ",".join(str(i) for i in df['产品货号'].to_list())
# 3.通过自编接口获取E3当前库存列表
goods_sn = []
zsl = []
for i in eval(myinterface06(hh_string)[0:-1]+"]"):
    goods_sn.append(i['goods_sn'])
    zsl.append(i['zsl'])
etkclist = pd.DataFrame({'goods_sn':goods_sn,'zsl':zsl})['zsl'].to_list()
# 4.将列表附加到df中
df['e3kc'] = etkclist

# 5.循环调用接口更新数据
# 同步原则：大于50上全量，低于50上50%，小于5个同步0
print("Start Update ... ... Please wait for a moment ... ... ")

for i in range(len(etkclist)):
    if int(etkclist[i]) > 50:
        wph_kcgx('{"request":{"vendor_id":"8394","cooperation_no":"30008042","barcode":"' + str(df['克隆产品69码'].to_list()[i]) + '","quantity":"'+str(df['e3kc'].to_list()[i])+'",'
                '"batch_no":"' + str(int(time.time())) + '"}}')
        time.sleep(3)
    elif int(etkclist[i]) <5:
        wph_kcgx('{"request":{"vendor_id":"8394","cooperation_no":"30008042","barcode":"' + str(
            df['克隆产品69码'].to_list()[i]) + '","quantity":"0","batch_no":"' + str(int(time.time())) + '"}}')
        time.sleep(3)
    else:
        wph_kcgx('{"request":{"vendor_id":"8394","cooperation_no":"30008042","barcode":"' + str(df['克隆产品69码'].to_list()[i]) + '","quantity":"'+str(int(float(df['e3kc'].to_list()[i])*0.5))+'",'
                '"batch_no":"' + str(int(time.time())) + '"}}')
        time.sleep(3)


print("Show Results:")

def timeChanged(dt):
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timeStamp = time.mktime(timeArray)
    return timeStamp
res = []
while time.time() < timeChanged("2022-10-10 23:59:59"):
    print(datetime.datetime.now().strftime('%H:%M:%S'))
    time.sleep(7200)
    for i in range(len(etkclist)):
        m = str(df['产品名称'].to_list()[i]) + "\t" + str(df['产品货号'].to_list()[i]) + "\t" + str(df['克隆产品69码'].to_list()[i]) + "\t线上当前库存：\t" + str(wph_kccx('{"vendor_id":"8394","barcode":"' + str(df['克隆产品69码'].to_list()[i]) + '","cooperation_no":"30008042"}')['result'][0][
                'leaving_stock'])
    res.append(m)

    dingmessage("\n".join(str(i) for i in res))

