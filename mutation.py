import numpy as np
from decis import data_length

# 变异函数
# 变异操作定义为一个染色体的两个基因交换位置

#变异概率
mutation_prob=0.8  

def mutation(decisDatas):
    for i in range(len(decisDatas)): #对每一条染色体
        decis=decisDatas[i]
        if np.random.rand() <= mutation_prob:
            # 生成r1,r2两个变异位置
            r1 = np.random.randint(data_length)
            r2 = np.random.randint(data_length)
            while r2 == r1:#如果相同
                r2 = np.random.randint(data_length)#r2再生成一次
            
            # 交换
            temp=decis.data[r1]
            decis.data[r1]=decis.data[r2]
            decis.data[r2]=temp
        decisDatas[i]=decis

    return decisDatas


