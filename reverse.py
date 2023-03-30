import numpy as np
from decis import data_length

# 翻转函数
# 翻转操作定义为一个染色体的r1到r2基因段做翻转操作

def reverse(decisDatas):
    for i in range(data_length): #对每一条染色体
        decis=decisDatas[i]
        decis_2=decisDatas[i].copyInstance()

        # 生成翻转的始末位置r1,r2
        r1 = np.random.randint(data_length)
        r2 = np.random.randint(data_length)
        while r2 == r1:#如果相同
            r2 = np.random.randint(data_length)#r2再生成一次

        left,right=min(r1,r2),max(r1,r2)

        # 进行翻转
        decis_2.data[left:right+1] = decis_2.data[left:right + 1][::-1]

        # 翻转得到了cost更小的染色体则更新，否则撤销当次翻转操作
        if decis.cost<decis_2.cost:
            decisDatas[i]=decis
        else:
            decisDatas[i]=decis_2
        

        return decisDatas

