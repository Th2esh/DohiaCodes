import requests
import json
import pymysql
import datetime




def dingmessage():
# 请求的URL，WebHook地址
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=b8f8d6097b1a00289056907fec8694e5aab89d545038deb06958d04ccdc6631e"
#构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
}
#构建请求数据
    tex = xiaoxi +"\n715直播销售退货\n"+datetime.datetime.now().strftime('%H:%M:%S')
    message ={

        "msgtype": "text",
        "text": {
            "content": tex
        },
        "at": {

            "isAtAll": True
        
    }
#对请求的数据进行json封装
    message_json = json.dumps(message)
#发送请求
    info = requests.post(url=webhook,data=message_json,headers=header)
#打印返回的结果
    print(info.text)

if __name__=="__main__":
    dingmessage()



    ]



    