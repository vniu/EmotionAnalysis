# -*- coding: utf-8 -*-
# 时间    : 2018/10/18 17:54
# 作者    : xcl

import pandas as pd

inputfile = 'C:\\Users\\Administrator\\Desktop\\EmotionAnalysis\\data\\huizong.csv' #评论汇总文件
outputfile = 'C:\\Users\\Administrator\\Desktop\\meidi_jd.txt' #评论提取后保存路径
data = pd.read_csv(inputfile, encoding = 'utf-8')
data = data[['评论']][data['品牌'] == '美的']
data.to_csv(outputfile, index = False, header = False, encoding = 'utf-8')