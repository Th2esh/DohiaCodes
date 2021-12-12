from xpinyin import Pinyin
import pypinyin
import pandas as pd
from snownlp import SnowNLP
s = SnowNLP('测试')
p = s.pinyin

df = pd.read_excel('员工表.xlsx')
df.head()
pinyin_name = []
first_pinyin = []
for i in df['真实姓名']:
    result = pypinyin.pinyin(i, style=pypinyin.NORMAL)
    result_ = [i[0] for i in result]
    result2 = result_[0].capitalize() + ' ' + ''.join(result_[1:]).capitalize()

    result3 = ''.join([i[0].upper() for i in result])
    print(result2)



