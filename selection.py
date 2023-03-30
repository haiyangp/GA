import numpy as np

# 选择函数
# 选择操作是指从原始种群中选择N个个体做变异、翻转等操作
# 选择操作有多种选择策略，这里选择随机遍历选择

def selection(decisDatas,select_num):
    # 计算每个个体的损失函数
    costs=[]
    for i in range(len(decisDatas)):
        costs.append(decisDatas[i].cost)
    costs=np.array(costs)
    
    # 根据损失函数确定每一个染色体被选择的概率
    possbility=1./costs
    
    # 随机遍历选择
    pos_cumsum=np.cumsum(possbility)
    pick = pos_cumsum[-1] /select_num  * (np.random.rand() + np.array(range(select_num)))

    i,j=0,0
    index=[]
    while i<len(pos_cumsum) and j<select_num:
        if pos_cumsum[i]>=pick[j]:
            index.append(i)
            j=j+1
        else:
            i=i+1
    
    data=[]
    for i in index:
        data.append(decisDatas[i].copyInstance())  #复制原始种群中被选择的个体，生成子种群
    return data



