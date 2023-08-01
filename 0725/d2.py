import pandas as pd

def test1():
    print('____')
    df = pd.read_csv("iris.csv")
    print(df.info())
    
    print(df.head())
    print(df.describe())
    
    print(df["variety"].value_counts())
#test1()

def test1a():
    print('heelo')
    df = pd.read_csv("iris.csv")
    print(df.head)
    
#test1a()

def test2():
    print("---")
    df = pd.read_csv("wine.csv")


    print(df.info())
    print(df.head(3))


    print(df.describe())
    print("____________________________________")


    print(df["Wine"].value_counts())


# test2()

def test3():
    print("-----")
    df = pd.read_csv("titanic.csv")
    
    print(df.info())
    print(df.head())
    
    print(df.describe())
    print(df["Cabin"].value_counts)
    print("-----------------")
    print(df["Cabin"].unique)
    
    fname = df.columns.values # 필드네임만 꺼내서 씀, 나이, 성멸 이름 위치 등등..
    print(fname)
    
# test3()

def test4():
    print("-----")
    df = pd.read_csv("iris.csv")
    
    print(df.info())
    
    data = df.values
    print(type(data),data.shape)
    
    x = data[:,0] # 2차원
    #x = data[:,[0]] # 1차원
    print(x,x.shape)
test4()

