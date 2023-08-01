import pandas as pd
def test1():
    print("haha")
    df = pd.read_csv("data.csv")
    print(type(df))
    print("---------")    
    
    
    print(df.info())
    print(df.head()) # 위부터 5개
    print(df.tail()) # 밑에서 5개
    
#test1()

def test2():
    df = pd.read_csv("data1.csv")
    
    print(df.info())
    print(df.head())
    
    print(df.describe()) # 묘사하다
    
    print(df['grade'].value_counts)
test2()


#데이터가 자동차로 치면 연료인데 엉터리 기름을 넣으면 차가 고장나듯
# 데이터의 품질을 높여주는 것이 실력
# 많은 데이터가 30, 50인데 하나만 10000같이 엄청 클 경우 빼주거나 처리를 해줘야지 그렇지 않으면 망가짐

