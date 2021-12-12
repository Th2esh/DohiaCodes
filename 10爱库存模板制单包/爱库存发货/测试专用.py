import requests
import json
import hashlib
import time
from datetime import datetime
import pandas as pd
#commit测试

def hsmd(secert):
    str = secert
    m = hashlib.md5()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return str_md5
def rq(pg):
    # 时间参数
    rt = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    # 接口类型
    jk = 'order.list.get'
    # json数据
    dr = str(time.strftime("%Y-%m-%d", time.localtime()))
    js_data ='{"time_type":"5","order_status":"5","startModified":"'+str(dr)+' 00:00:00","endModified":"'+str(dr)+' 23:59:59","sd_code":"998","pageNo":"'+str(pg)+'"}'
    # js_data ='{"order_status":"5","startModified":"2021-11-30 00:00:00","endModified":"2021-11-30 23:59:59","sd_code":"998","pageNo":"'+str(pg)+'"}'
    # js_data = '{"deal_code":"210622-105245584311233"}'
    dqm_data = "key=test&requestTime="+rt+"&secret=1a2b3c4d5e6f7g8h9i10j11k12l&version=3.0&serviceType="+jk+"&data" \
                                                                                                            "="+js_data
    sign_data = hsmd(dqm_data)
    print(dr)


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

    st = datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "%Y-%m-%d %H:%M:%S")

    res = rq("1")
    print(res)



    et = datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "%Y-%m-%d %H:%M:%S")
    print('执行耗时：'+str((et-st).total_seconds())+' 秒')