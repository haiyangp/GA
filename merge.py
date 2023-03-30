from decis import Init_Number,select_Number
import numpy as np

# 合并函数
# 合并操作定义为将经过变异翻转的子代个体替换掉父代种群中等数量的cost较高的个体

def merge(decisDatas,sub_decisDatas):
    # decisDatas表示原始种群，sub_decisDatas表示经过变异的子代种群
    costs=[]
    for i in range(Init_Number):
        costs.append(decisDatas[i].cost)
    costs=np.array(costs)
    
    # 计算按cost值大小排序的索引，index前N条，表示cost前N大的染色体在种群中的索引
    index=np.argsort(costs)[::-1]
    for i in range(select_Number):
        ind=index[i]
        decisDatas[ind]=sub_decisDatas[i] #对原始种群中的cost较大值进行替换
    
    return decisDatas
