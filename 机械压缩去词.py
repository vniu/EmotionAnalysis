# -*- coding: utf-8 -*-
# 时间    : 2018/10/18 18:10
# 作者    : xcl

# https://www.cnblogs.com/a1397240667/p/7571407.html

import codecs
inputfile = 'C:\\Users\\Administrator\\Desktop\\meidi_jd_process_1.txt' #评论文件
outputfile = 'C:\\Users\\Administrator\\Desktop\\meidi_jd_process_2.txt' #评论处理后保存路径
f = codecs.open(inputfile ,'r','utf-8')
f1=codecs.open(outputfile,'w','utf-8')
fileList = f.readlines()
f.close()
for A_string in fileList:
    temp1= A_string.strip('\n')       #去掉每行最后的换行符'\n'
    temp2 = temp1.lstrip('\ufeff') #去掉Unicode编码产生的feff字母
    temp3= temp2.strip('\r') #“\r”相当于回车，删除换行符
    char_list=list(temp3)
    list1=['']
    list2=['']
    del1=[]
    flag=['']
    i=0
    while(i<len(char_list)):
        if (char_list[i]==list1[0]):
            if (list2==['']):
                list2[0]=char_list[i]
            else:
                if (list1==list2):
                    t=len(list1)
                    m=0
                    while(m<t):
                        del1.append( i-m-1)
                        m=m+1
                    list2=['']
                    list2[0]=char_list[i]
                else:
                    list1=['']
                    list2=['']
                    flag=['']
                    list1[0]=char_list[i]
                    flag[0]=i
        else:
            if (list1==list2)and(list1!=[''])and(list2!=['']):
                if len(list1)>=2:
                    t=len(list1)
                    m=0
                    while(m<t):
                        del1.append( i-m-1)
                        m=m+1
                    list1=['']
                    list2=['']
                    list1[0]=char_list[i]
                    flag[0]=i
            else:
                if(list2==['']):
                    if(list1==['']):
                        list1[0]=char_list[i]
                        flag[0]=i
                    else:
                       list1.append(char_list[i])
                       flag.append(i)
                else:
                    list2.append(char_list[i])
        i=i+1
        if(i==len(char_list)):
           if(list1==list2):
                    t=len(list1)
                    m=0
                    while(m<t):
                        del1.append( i-m-1)
                        m=m+1
                    m=0
                    while(m<t):
                        del1.append(flag[m])
                        m=m+1
    a=sorted(del1)
    t=len(a)-1
    while (t>=0):
        #print(char_list[a[t]])
        del char_list[a[t]]
        t=t-1
    str1 = "".join(char_list)
    str2=str1.strip() #删除两边空格
    f1.writelines(str2+'\r\n')
f1.close()