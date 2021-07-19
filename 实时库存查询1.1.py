import xlwt
import os
def Query_inventory(file_excel):


    from sshtunnel import SSHTunnelForwarder
    import pymysql

    server = SSHTunnelForwarder(ssh_address_or_host=('39.100.94.96', 22), ssh_username='efast',
                                ssh_password='51ksCg7eZ!VUgNx',
                                remote_bind_address=('rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com', 3306))
    server.start()
    db = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user='jusr2mmi49d8', passwd='uEZBjc9tQwoN',
                         db='e3', charset='utf8')
    cur = db.cursor()
    # cur.execute("SELECT goods_barcode.barcode,goods.goods_sn,goods.goods_name,sum(spkcb.sl-spkcb.sl2) AS sl FROM spkcb,goods,goods_barcode WHERE spkcb.goods_sn=goods.goods_sn AND spkcb.goods_sn=goods_barcode.sku AND spkcb.ck_id IN (11,10,3) GROUP BY goods.goods_sn")#查询库存sql语句
    cur.execute(sql)
    res = cur.fetchall()
    # print(results[1][3])
    w_excel(res)

    db.commit()
def w_excel(res):
    book = xlwt.Workbook() #新建一个excel
    sheet = book.add_sheet('实时库存查询') #新建一个sheet页
    title = ['barcode','goods_sn','goods_name','sl','仓库']
    #写表头
    i = 0
    for header in title:
        sheet.write(0,i,header)
        i+=1


    #写入数据
    for row in range(1,len(res)):
        for col in range(0,len(res[row])):
            sheet.write(row,col,res[row][col])
        row+=1
    col+=1
    book.save('实时库存.xls')
    print("导出成功！")


if __name__ == "__main__":
    print(
        "####唯品会实时查询工具\n"
        "\n"
        "1.总量查询\n"
        "2.分仓查询\n"
    )
    number = input("请输入代码:")
    if number == str(1):
        sql = "SELECT goods_barcode.barcode,goods.goods_sn,goods.goods_name,sum(spkcb.sl-spkcb.sl2) AS 实时库存 FROM spkcb,goods,goods_barcode WHERE spkcb.goods_sn=goods.goods_sn AND spkcb.goods_sn=goods_barcode.sku AND spkcb.ck_id IN (11,10,3) GROUP BY goods.goods_sn"
    elif number == str(2):
        sql = "select goods_barcode.barcode,goods.goods_sn,goods.goods_name,spkcb.sl - spkcb.sl2 as 实时库存 ,spkcb.ck_id_name as 仓库 from spkcb,goods,goods_barcode  where spkcb.goods_sn = goods.goods_sn and spkcb.goods_sn = goods_barcode.sku and spkcb.ck_id in (11,10,3) "
    else:
        print("输入数字错误，请重新运行程序")
        os._exit(0)

    file_excel = r"2222.xls"
    Query_inventory(file_excel)

