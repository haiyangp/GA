from decis import decisDatas,select_Number,countLowest
from selection import *
from mutation import *
from reverse import *
from merge import *

# 解决二次分配问题的简单遗传算法实现
# decis.py————————问题描述及初始数据，类decis实例表示一条决策变量
# selection———————定义选择操作
# mutation.py—————定义突变操作
# reverse.py——————定义翻转操作
# merge.py————————定义合并操作

# 迭代次数
iteration_time=1000

def Main():
    # 表示当前种群中的最优解
    lowestcost=2000

    # 记录每次迭代的最优解
    iteration_data=[]

    # 初始种群数据
    dD=decisDatas
    for i in range(iteration_time):
        # 选择
        sub_DecisData=selection(decisDatas=dD,select_num=select_Number)
        # 突变
        sub_DecisData=mutation(sub_DecisData)
        # 翻转
        sub_DecisData=reverse(sub_DecisData)
        # 合并
        dD=merge(decisDatas=dD,sub_decisDatas=sub_DecisData)

        # 当前最优解
        lowestcost=countLowest(decisDatas=dD)

        # 添加当次迭代最优解
        iteration_data.append(lowestcost)

    print(iteration_data)


if __name__=="__main__":
    Main()