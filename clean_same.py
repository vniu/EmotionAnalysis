# -*- coding: utf-8 -*-
# 时间    : 2018/10/18 17:58
# 作者    : xcl

import pandas as pd

inputfile = 'C:\\Users\\Administrator\\Desktop\\meidi_jd.txt' #评论文件
outputfile = 'C:\\Users\\Administrator\\Desktop\\meidi_jd_process_1.txt' #评论处理后保存路径
data = pd.read_csv(inputfile, encoding = 'utf-8', header = None)
l1 = len(data)
data = pd.DataFrame(data[0].unique())
l2 = len(data)
data.to_csv(outputfile, index = False, header = False, encoding = 'utf-8')
print('删除了%s条评论。' %(l1 - l2))