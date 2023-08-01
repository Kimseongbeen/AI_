import numpy as mp
import pandas as pd

def test1():
    print('---')
    df  = pd.read_csv("iris.csv")
    
    print(df.info())
    
    print(df.describe())
    print("--------------")
    
    print(df["variety"].value_counts)
    
    cname = df.columns.values
    print(cname)
    print("--------------")
    
    data = df.values
    print(type(data),data.shape) # result : <class 'numpy.ndarray'> (150, 5)
    
    x = data[:,[0,1,2,3]] # [6.4 3.1 5.5 1.8]
                          # [6.0 3.0 4.8 1.8]
                          # [6.9 3.1 5.4 2.1]
                          # [6.7 3.1 5.6 2.4]
                          # [6.9 3.1 5.1 2.3]
                          # [5.8 2.7 5.1 1.9]
    # x = data[:,4]
    print(x,x.shape)    # shape (150, 4) 4개 데이터 150개
    
    # y = data[:,4]
    # print(y,y.shape)  # shape (150, 4) [[5.1 3.5 1.4 0.2][4.9 3.0 1.4 0.2]...[4.9 3.0 1.4 0.2]] 4개 데이터 15개
    
    y1 = data[:,[4]] 
    print(y1,y1.shape)  # (150, 1)[['Setosa']['Setosa']...['Versicolor']...['Virginica']...]
    
test1()