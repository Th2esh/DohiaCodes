import time
import datetime
now = time.time()
a = int(now)
print(a)
b = 1626358140
while a < b:
    print(datetime.datetime.now().strftime('%H:%M:%S'))
    time.sleep(10)
    # # now = time.time()
    #
    # # if time
    # print(type(now))
# a = 1626356894
# b = 1626356939
# while a > b:
#     print("1")

