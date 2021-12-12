import requests
import json



    # 文本类型消息
def send_wx(title,content):
    sckey = "SCT82809TLRqNECzzPtmuDwF5L8oE30sL"
    url = 'https://sctapi.ftqq.com/' +sckey +'.send'
    data = {'text':title,'desp':content}
    result = requests.post(url,data)
    return(result)
title = '唯品会克隆库存机器人'
content ='计划任务已改为10分钟'
send_wx(title,content)
