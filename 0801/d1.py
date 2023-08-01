import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test1():
    print(2)
    data = np.array
    
# test1()

def test1a():
    
    data = np.array([3,8,2,15,11])
    print(type(data), data.shape)

    plt.plot(data, 'r')
    plt.show()
    
# test1a()

# 1 차원 데이터 산포도
def test2():
    print("a")
    data = np.random.randint(0,100,50) # 0~100 50개
    print(data)
    
    # plt.plot(data, 'y') # 색상 'y' = 노랑
    #plt.plot(data, 'yo') # 산포도 o : 1차원그래프는 산포도로 보는경우가 적고 2차원 할때는 봄

    plt.plot(data, 'bx') # 산포도 x  : bx yx .. '(색상)(표시)
    
    plt.show()
    
# test2()

def test2a():
    
    data = np.random.randint(0,500,20)
    print(data)
    plt.plot(data, 'r')
    plt.show()
    
# test2a()

# 2차원 데이터 
def test3():
    data = np.random.randint(0,10, (20,2)) # 0~10개 (데이터 20개, 2차원)
    print(data, data.shape)

    plt.plot(data[:,0],data[:,1],'rx') # y 전부, 
    plt.show()
    
# test3()

def test3a():
    data = np.random.randint(0,10, (12,2))
    print(data, data.shape)
    x = np.array([1,2,3,4])
    y = np.array([10,20,30,50])
    plt.plot(x,y,'gx')
    plt.show()
    
# test3a()

def test4():
    data = np.random.randint(0,100,(30,5))
    print(data, data.shape)
    
    data1 = np.array([1,2,43,5,6,6,7,8,42,10])
    
    plt.plot(data1,data[:,0],'rx')
    plt.plot(data1, data[:,1],'go')
    plt.show()
    
    
# test4()
def test5():
    data = np.random.randint(0,10,50)
    data[0] = 50
    data[10] = -10
    print(data, data.shape)


    plt.boxplot(data)
    plt.show()

# test5()

def test6():
    data = np.random.randint(0,10,30) 
    print(data, data.shape)

    plt.hist(data,bins=4, color = 'r') # histogram 
    # bins=4로 설정하여 4개의 구간으로 데이터를 나눔
    plt.show()
    
# test6()

def test7():
    data =np.random.randint(0,100,(50,5))
    
    plt.plot(data[:,0], data[:,1],'rx')
    plt.xlabel("kor")
    plt.ylabel("eng")
    plt.title("scores")
    plt.show()

# test7()

def test7a():
    data = np.random.randint(0,400,(10,5)) # (70, 5)의 형태는 2차원 배열이고, 해당 배열은 70개의 행(row)과 5개의 열(column)
    print(data,data.shape)
    
    plt.plot(data[:,0], 'r')
    plt.plot(data[:,1], 'b')
    plt.legend(['kor','eng'])   # plot한 순서대로 범례   
    plt.show()

# test7a()

def test8():
    data = np.random.randint(0,100,(30,5))
    print(data, data.shape)
    
    plt.plot(data[:, 0], data[:, 1], 'r')
    plt.plot(data[:,0], data[:,2], 'y')
    plt.grid() # 그래프 격자(grid)
    plt.legend(["kor","eng"])
    plt.show()
    
# test8()

def test9():
    pdata = pd.read_csv('data_org/iris.csv')
    print(pdata.info())
    print(pdata.describe())
    
    data = pdata.values
    print(type(data),data.shape)
    
    plt.plot(data[:,0],'r')
    plt.show()
    
    plt.boxplot(data[:,0], 'y')
    plt.show()
# test9()

def test10():
    df = pd.read_csv('data_org/iris.csv')
    print(df.shape)
    
    print(df['variety'].value_counts())
    print(df)
    data = df.values #그래프화 하기위해 배열안에 넣음
    print(data)
    x = np.arange(150)
    
    plt.plot(x, data[:,4], 'ro')
    plt.show()
# test10()

def test12():
    df = pd.read_csv('data_org/iris.csv')
    print(df.info())
    
    data = df.values
    
    plt.plot(data[:,0],'r')
    plt.plot(data[:,1], 'g')
    plt.savefig('data_org/t1.png') #t1.png로 파일 저장
    # plt.show()

# test12()

# def test12a():
#     tdf = pd.read_csv('data_org/cancer.csv')
#     print(tdf.info())
    
#     data =tdf.values
#     print(data)
    
#     plt.plot(data[:,0],'r') # id
#     plt.plot(data[:,1],'b') # 진단 B = 양성, M = 악성
#     plt.plot(data[:,2],'y') # radius_mean
#     plt.plot(data[:,10],'g') # symmetry_mean 
#     plt.legend(["id","diagnosis","radius_mean","symmetry_mean"])
#     plt.show()
# test12a()

def demo1():
    tdf = pd.read_csv('data_org/iris.csv')
    print(tdf.info())
    
    data =tdf.values
    print(data)
    
    # plt.plot(data[:,1],'r') # id
    # plt.plot(data[:,3],'b') # 진단 B = 양성, M = 악성
    # plt.legend(["id","diagnosis"])
    # plt.xlabel("id")
    # plt.ylabel("widths_values")
    # plt.grid()
    # plt.show()
    plt.plot(data[:,1],'r') # id
    plt.plot(data[:,2],'b') # petal.length   
    plt.legend(["id",'petal.length']) 
    plt.xlabel("id")
    plt.ylabel("petal.length")
    plt.grid()
    plt.show()
# demo1()

def demo2():
    Wdf = pd.read_csv("data_org/wine.csv")
    print(Wdf.info())
    
    data = Wdf.values 
    
    plt.plot(Wdf[:,0], Wdf[:,1], 'yo') # (x,y,타입)
    plt.show()
    
    
# demo2()

def demo3():
    df = pd.read_csv('data_org/wine.csv')
    print(df.info())

    data = df.values   
    plt.plot(data[:,0], data[:,1], 'rx')   
    plt.show()   

demo3()