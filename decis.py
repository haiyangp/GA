import random
import numpy as np

# 二次分配问题
# 共有m=0,1,2,3,4,5,6,7,8,9,10,11(12个地方)
# 以及n=0,1,2,3,4,5,6,7,8,9,10,11(12个工厂)

# d为距离矩阵,d(mi,mj)表示i,j两地的距离
d = [[0, 1, 2, 2, 3, 4, 4, 5, 3, 5, 6, 7],
      [1,  0, 1, 1, 2, 3, 3, 4, 2, 4, 5, 6],
      [2, 1, 0, 2, 1, 2, 2, 3, 1, 3, 4, 5],
      [2, 1, 2, 0, 1, 2, 2, 3, 3, 3, 4, 5],
      [3, 2, 1, 1, 0, 1, 1, 2, 2, 2, 3, 4],
      [4, 3, 2, 2, 1, 0, 2, 3, 3, 1, 2, 3],
      [4, 3, 2, 2, 1, 2, 0, 1, 3, 1, 2, 3],
      [5, 4, 3, 3, 2, 3, 1, 0,  4, 2, 1, 2],
      [3, 2,  1, 3, 2, 3, 3, 4, 0, 4, 5, 6],
      [5, 4, 3, 3, 2, 1, 1, 2, 4, 0, 1, 2],
      [6, 5, 4, 4, 3, 2, 2, 1, 5, 1, 0, 1],
      [7, 6, 5, 5, 4, 3, 3, 2, 6, 2, 1, 0]]

# h为距离矩阵,h(ni,nj)表示i,j两个工厂之间需要运输的货物
h = [[0, 3, 4, 6, 8, 5, 6, 6, 5, 1, 4, 6],
      [3, 0, 6, 3, 7, 9, 9, 2, 2, 7, 4, 7],
      [4, 6, 0, 2, 6, 4, 4, 4, 2, 6, 3, 6],
      [6, 3, 2, 0, 5, 5, 3, 3, 9, 4, 3, 6],
      [8, 7, 6, 5, 0, 4, 3, 4, 5, 7, 6, 7],
      [5, 9, 4, 5, 4, 0, 8, 5, 5, 5, 7, 5],
      [6, 9, 4, 3, 3, 8, 0, 6, 8, 4, 6, 7],
      [6, 2, 4, 3, 4, 5, 6, 0, 1, 5, 5, 3],
      [5, 2, 2, 9, 5, 5, 8, 1, 0, 4, 5, 2],
      [1, 7, 6, 4, 7, 5, 4, 5, 4, 0, 7, 7],
      [4, 4, 3, 3, 6, 7, 6, 5, 5, 7, 0, 9],
      [6, 7, 6, 6, 7, 5, 7, 3, 2, 7, 9, 0]]

# 决策变量为一个长度为12的数组arr[12],其中arr[i]表示第i家工厂在第arr[i]个地方
# eg.[0,2,3,5,7,1,9,11,10,8,6,4]

# 初始种群数量
Init_Number = 200
# 选择的种群数量
select_Number = 160
# 决策变量长度
data_length = 12
# 初始化决策变量
decisDatas = []

# 表示决策变量 或者说种群中的一个个体
# 其中主要包括属性成员
#     data————长度为12的一维数组，也就是决策变量
#     cost————该决策变量的cost

class decis():
    # 指定染色体长度，初始化一个随机染色体
    def __init__(self,data_length) -> None:
        self.data_length=data_length # 设置数据长度
        self.init() #初始化data
        self.costCompute(d,h) #初始化cost
        
    # 初始化函数
    def init(self):
        data=[]
        records=list(range(self.data_length))
        for i in range(self.data_length):
            index=random.randint(0,len(records)-1)  #随机初始化个体
            data.append(records.pop(index))

        if self.check(data=data):
            self.data=np.array(data)

    # 检查是否满足等式约束(一个工厂独占一个地方)
    def check(self,data):
        decis_data=data
        if len(decis_data) !=self.data_length:
            return False
        
        for i in range(self.data_length):
            if i not in decis_data:
                return False
        return True
    

    # 打印当前染色体
    def print(self):
        print(self.data)

    # 复制函数，将参数染色体中的内容拷贝到当前对象当中（深拷贝）
    def copy(self,decis_data) -> None:
        self.data_length=decis_data.data_length
        data=[]
        for i in range(self.data_length):
            data.append(decis_data.data[i])
        if self.check(data=data):
            self.data=np.array(data)
            self.costCompute(d,h)

        
    # 复制实例，返回一个跟当前对象具有相同内容的染色体
    def copyInstance(self):
        res=decis(self.data_length)
        res.copy(self)
        return res


    # cost function
    def costCompute(self,d,h) -> None:
        # 检查数据维度是否一致
        if len(d) !=self.data_length or len(d[0])!=self.data_length or len(h) !=self.data_length or len(h[0])!=self.data_length:
            print("数据维度不一致")
            return
        data=self.data
        cost_data=0
        for i in range(self.data_length):
            i_data=0
            pos_a=data[i]
            
            for j in range(self.data_length):
                if i==j:
                    continue
                
                pos_b=data[j]
                d_data=d[pos_a][pos_b]
                h_data=h[i][j]

                j_data=h_data*d_data

                i_data=i_data+j_data

            cost_data=cost_data+i_data    

        self.cost=cost_data

# 初始化种群函数
for i in range(Init_Number):
    decisDatas.append(decis(data_length))


# 计算当前种群中的最优染色体的cost
def countLowest(decisDatas):
      lc = 20000
      for i in range(Init_Number):
            if decisDatas[i].cost < lc:
                  lc = decisDatas[i].cost
      return lc