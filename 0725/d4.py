import pandas as pd
import numpy as np

def test1():
    print(10,20,130)
    df  = pd.read_csv("invedata.csv")
    print(df.info()) # 데이터 정보
    print("-----------")
    print(df.head(3)) #위에서 3개
    print("-----------")
    print(df.describe())
#       Volume
#       count  2.516000e+04
#       mean   5.131764e+07
#       std    6.399143e+07
        # min    1.143952e+06
        # 25%    1.200394e+07
        # 50%    2.672083e+07
        # 75%    6.857269e+07
        # max    1.065209e+09
    print("-----------")
    print(df["Volume"].value_counts)
    print("-----------")
    data=df.values
    print(data.shape) #(25160, 7)
    print("-----------")
    x=data[:,[0,1]]
    print(x,x.shape)
#     [['AAPL' '07/17/2023']
#  ['AAPL' '07/14/2023']
#  ['AAPL' '07/13/2023']
#  ...
#  ['NFLX' '07/22/2013']
#  ['NFLX' '07/19/2013']
#  ['NFLX' '07/18/2013']] (25160, 2)
    
test1()