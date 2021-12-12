a = "app_key23036663item_list{'brand_name': '多喜爱旗舰店', 'channel': 'OFFLINE_SHOP', 'channel_publish_time': '2021-10-20 00:00:00', 'tmall_same': 'true', 'item_id': '657089889925', 'item_name': '福克斯', 'brand_id': '80884', 'channel_publish_area': 'ALL'}methodtmall.brand.item.uploadsession6100702294147e841d7715eb8a2b55033caa6e780b31a34114141735sign_methodmd5timestamp2021-10-20 23:21:38v2.0"


b = "app_key23036663item_list{'brand_name': '多喜爱旗舰店', 'channel': 'OFFLINE_SHOP', 'channel_publish_time': '2021-10-20 00:00:00', 'tmall_same': 'true', 'item_id': '657856679754', 'item_name': '艾兰达', 'brand_id': '80884', 'channel_publish_area': 'ALL'}methodtmall.brand.item.uploadsession6100702294147e841d7715eb8a2b55033caa6e780b31a34114141735sign_methodmd5timestamp2021-10-20 23:19:57v2.0"


for i in range(len(a)):
    if a[i] != b[i]:
        print(a[i] + b[i])

