def wph_xnkc():
    beijing_sku = ['11','22']
    beijing_number = ['50', '20']
    suoku_number = ['30','60']
    new_beijing_number = []
    for i in range (len(beijing_number)):
        if beijing_number[i] > suoku_number[i]:
            new_beijing_number.append(suoku_number[i])
        else:
            new_beijing_number.append(beijing_number[i])
    return new_beijing_number
def wph_yqdh():
    huazhong_number = ['50','20']
    sancang_nmuber = ['100','10']
    new_huazhong_number = []
    for j in range (len(huazhong_number)):
        # if huazhong_number[j] < sancang_nmuber[j]:
        #     new_huazhong_number.append(-int(huazhong_number[j]))
        # else:
        #     new_huazhong_number.append(0)
       print(huazhong_number[j] ,sancang_nmuber[j])
     return new_huazhong_number


print(wph_yqdh())




