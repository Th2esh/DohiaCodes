# coding=utf-8
import requests
import json

# 设置Server酱post地址 不需要可以删除
serverChan = "https://sc.ftqq.com/SCU38259Tdce55fedefed5a65374f74a41c6a7d375c233d11d819e.send"
# 状态地址
current_url = 'https://zhiyou.smzdm.com/user/info/jsonp_get_current'
# 签到地址
checkin_url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
# 用用户名和密码登录后获取Cookie
userCookie = "__ckguid=8JP4TU3p88Y3wgj7oVv5XI2; device_id=213070643316070759682991991b0ec3c93434ed62d0d0bff83dc20060; homepage_sug=c; r_sort_type=score; _ga=GA1.2.1477574111.1607075970; smzdm_user_view=72C98CD3057F487CCEBC314AAF3BCB8B; smzdm_user_source=4F55127EA4476FF4715CDD7AC12999F4; zdm_qd=%7B%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221762d313789259-0cde012c298a26-63112c72-2073600-1762d31378a15af%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2F%22%7D%2C%22%24device_id%22%3A%221762d313789259-0cde012c298a26-63112c72-2073600-1762d31378a15af%22%7D; shequ_pc_sug=b; s_his=%E7%89%B9%E6%96%AF%E6%8B%89; ss_ab=ss94; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1610938454,1611279712,1611387699,1611562133; wt3_sid=%3B999768690672041; wt3_eid=%3B999768690672041%7C2160732181300609094%232161156227700973757; _gid=GA1.2.223161085.1611710947; sess=MzU1YTZ8MTYxNjg5NDk1M3w3MDQ5MjkzNDc3fDYzNmRiN2ViYjcxNzYwZDUxMjUxM2VjOWYyOWQwN2Nj; user=user%3A7049293477%7C7049293477; smzdm_id=7049293477; _zdmA.uid=ZDMA.Nb6HiF9mt.1611710955.2419200; FROM_BD=1; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1611711348; _dc_gtm_UA-27058866-1=1"
headers = {
    'Referer': 'https://www.smzdm.com/',
    'Host': 'zhiyou.smzdm.com',
    'Cookie': userCookie,
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}


def req(url):
    url = url
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = json.loads(res.text)
        return data


data = req(current_url)
if data['checkin']['has_checkin']:
    info = '%s ：%s 你目前积分：%s，经验值：%s，金币：%s，碎银子：%s，威望：%s，等级：%s，已经签到：%s天' % (
    data['sys_date'], data['nickname'], data['point'], data['exp'], data['gold'], data['silver'], data['prestige'],
    data['level'], data['checkin']['daily_checkin_num'])
    print(info)
    # 通过Server酱发送状态 不需要可以删除
    requests.post(serverChan, data={'text': data['nickname'] + '已经签到过了', 'desp': info})
else:
    checkin = req(checkin_url)['data']
    # print(checkin)
    info = '%s 目前积分：%s，增加积分：%s，经验值：%s，金币：%s，威望：%s，等级：%s' % (
    data['nickname'], checkin['point'], checkin['add_point'], checkin['exp'], checkin['gold'], checkin['prestige'],
    checkin['rank'])
    print(info)
    # 通过Server酱发送状态 不需要可以删除
    requests.post(serverChan, data={'text': data['nickname'] + '签到信息', 'desp': info})
