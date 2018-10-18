# -*- coding: utf-8 -*-
# 时间    : 2018/10/18 22:05
# 作者    : xcl

#短句删除
#需要提前处理txt的空行
#输出的结果均为长句
inputfile = 'C:\\Users\\Administrator\\Desktop\\meidi_jd.txt' #评论提取后保存路径
outputfile = 'C:\\Users\\Administrator\\Desktop\\meidi_jd233.txt' #评论提取后保存路径
import pandas as pd

data=pd.read_csv(inputfile,encoding="utf-8")


#print(len(data))
out=open(outputfile,"a+")
print(data.loc[0].map(len)[0])
print(data.loc[0][0])

for i in range(0,len(data),1):
    if data.loc[i].map(len)[0] >= 35.0:
        out.write(data.loc[i][0]+'\n')
    else:
        pass

out.close()