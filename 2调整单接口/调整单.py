import requests
import json
import hashlib
import time
import pandas as pd





def hsmd(secert):
    str = secert
    m = hashlib.md5()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return str_md5


def rq(contents):
    # 单据编号的变量值
    dj_random = str(time.strftime("%Y%m%d%H%M", time.localtime()))
    # 时间参数
    rt = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    # 接口类型
    jk = 'kctzd.add'
    # json数据
    js_data = '{"djbh": "wphhztz'+str(dj_random)+'","ckCode": "310201","sku": '+str(contents)+'}'

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



if __name__ == '__main__':

    # time.sleep(10800)

    df = pd.read_excel("wph.xlsx",sheet_name="Sheet1")
    sku_list = df['内部货号'].to_list()
    sl_list = df['虚加数量'].to_list()
    sl_list_x = []
    for i in sl_list:
        sl_list_x.append(int(i))

    d_dict = []
    for i in range(len(sku_list)):
        d_dict.append({"sku": str(sku_list[i]), "number": str(sl_list_x[i])})
    str_dict = str(d_dict).replace("'",'"')


    print(rq(str_dict))


