# 综合引入
import os
import time
import pandas as pd



# 函数
def mysql_query_results(sql,zh,mm):
    import pandas as pd
    from sshtunnel import SSHTunnelForwarder
    import pymysql

    server = SSHTunnelForwarder(ssh_address_or_host=('39.100.94.96', 22), ssh_username= zh,
                                ssh_password= mm,
                                remote_bind_address=('rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com', 3306))
    server.start()
    db = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user='jusr2mmi49d8', passwd='uEZBjc9tQwoN',
                         db='e3', charset='utf8')
    cur = db.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    db.commit()
    # return results
    df = pd.DataFrame(results)
    return df

def load_goods_sn():
    df = pd.read_excel('wu_tg_sku.xlsx',sheet_name='Sheet1')
    return df

def read_key():
    df = pd.read_excel('key.xlsx',sheet_name='Sheet1')
    return df



# 主程序部分
if __name__ == "__main__":

####################################
# 生产工具
####################################

    # 载入账号密码
    zh = read_key()['user'][0]
    mm = read_key()['password'][0]

    input('回车开始程序...')

    # 基础表
    gdn_basic = load_goods_sn()
    gdn = gdn_basic['SKU'].to_list()
    t_tempx = []
    for i in gdn:
        t_tempx.append(str(i))
    gdn_basic['SKU']=t_tempx

    str = ",".join(str(i) for i in gdn)

    # 产出全仓结果df
    sql = "select goods_barcode.barcode,goods.goods_sn,goods.goods_name,spkcb.ck_id_name,if(spkcb.sl=0,0," \
          "spkcb.sl-spkcb.sl2) as sl from spkcb,goods,goods_barcode where spkcb.goods_sn = goods.goods_sn and " \
          "spkcb.goods_sn = goods_barcode.sku and spkcb.ck_id in (3,10,11) and goods_barcode.barcode in ("+str+")"
    dfc_all = mysql_query_results(sql,zh,mm)
    dfc_all.columns = ['SKU','货号','名称','仓库','库存']
    dfc_all = dfc_all.drop(dfc_all[dfc_all.库存 == 0].index)

    # 产出上海仓结果df
    sql = "select goods_barcode.barcode,goods.goods_sn,goods.goods_name,spkcb.ck_id_name,if(spkcb.sl=0,0," \
          "spkcb.sl-spkcb.sl2) as sl from spkcb,goods,goods_barcode where spkcb.goods_sn = goods.goods_sn and " \
          "spkcb.goods_sn = goods_barcode.sku and spkcb.ck_id = 3 and goods_barcode.barcode in ("+str+")"
    dfc_sh = mysql_query_results(sql,zh,mm)
    dfc_sh.columns = ['SKU','货号','名称','仓库','上海库存']
    dfc_sh = dfc_sh.drop(dfc_sh[dfc_sh.上海库存 == 0].index)

    # 产出南通仓结果df
    sql = "select goods_barcode.barcode,goods.goods_sn,goods.goods_name,spkcb.ck_id_name,if(spkcb.sl=0,0," \
          "spkcb.sl-spkcb.sl2) as sl from spkcb,goods,goods_barcode where spkcb.goods_sn = goods.goods_sn and " \
          "spkcb.goods_sn = goods_barcode.sku and spkcb.ck_id = 11 and goods_barcode.barcode in (" + str + ")"
    dfc_nt = mysql_query_results(sql,zh,mm)
    try:
        dfc_nt.columns = ['SKU', '货号', '名称', '仓库', '南通库存']
        dfc_nt = dfc_nt.drop(dfc_nt[dfc_nt.南通库存 == 0].index)
    except:
        pass

    # 产出长沙仓结果df
    sql = "select goods_barcode.barcode,goods.goods_sn,goods.goods_name,spkcb.ck_id_name,if(spkcb.sl=0,0," \
          "spkcb.sl-spkcb.sl2) as sl from spkcb,goods,goods_barcode where spkcb.goods_sn = goods.goods_sn and " \
          "spkcb.goods_sn = goods_barcode.sku and spkcb.ck_id = 10 and goods_barcode.barcode in (" + str + ")"
    dfc_cs = mysql_query_results(sql,zh,mm)
    try:
        dfc_cs.columns = ['SKU', '货号', '名称', '仓库', '长沙库存']
        dfc_cs = dfc_cs.drop(dfc_cs[dfc_cs.长沙库存 == 0].index)
    except:
        pass

    tempx01 = pd.merge(gdn_basic,dfc_all,how='left',on='SKU')
    del tempx01['仓库']
    del tempx01['库存']
    tempx02 = pd.merge(gdn_basic, dfc_sh, how='left', on='SKU')
    del tempx02['仓库']
    tempx03 = pd.merge(tempx02, dfc_nt, how='left', on='SKU')
    del tempx03['仓库']
    # del tempx03['货号_y']
    # del tempx03['名称_x']
    # del tempx03['货号_x']
    # del tempx03['名称_y']
    tempx03.to_excel("Results.xls",index=False)

    try:
        tempx04 = pd.merge(tempx03, dfc_cs, how='left', on='SKU')
        # del tempx04['仓库']
        # del tempx04['货号_y']
        # del tempx04['名称_x']
        # del tempx04['货号']
        # del tempx04['名称_y']
        tempx04.to_excel("Results.xls",index=False)
    except:
        pass

    # 增加库存表的商品名称和货号！
    print('数据结转完成，请到根目录查找Results文件')
    os._exit(0)




#######################################
# 根据值查索引
#######################################
    # possion = []
    # dfc = dfc_df[4].to_list()
    # for index,value in enumerate(dfc):
    #     if value == 0:
    #         possion.append(index)
    #     else:
    #         pass
    # print(possion)

    # df = dfc_df.drop(dfc_df[dfc_df.])

#########################################
# ssh密码载入测试
#########################################

    # zh = read_key()['user'][0]
    # mm = read_key()['password'][0]
