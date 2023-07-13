import numpy as np

# #, 없음
# def test1():
#     data = np.array([1,2,4,5])
#     print(data)
#     print(type(data))
    
# test1()

def test1A():
    data = np.array([5,6,78,8])
    print(data)
    print(type(data))
    print(len(data))

# test1A()

def test2():
    data = np.random.randint(0,100,10) # 0~100,10개
    print(data)
    print(type(data),data.shape) # 1차원 데이터 10개 (y,x) || y : len(data)
    print(len(data))


# test2()

def test2a():
    data = np.random.randint(0,10,10) #정수 0~10,10개
    print(data)
    print(type(data),data.shape)

# test2a()

def test3():
    data = np.random.rand(20) # 소수
    print(data)
    print(type(data),data.shape)
    
    print(data[0],data[-1])
    #슬라이싱
    data1 = data[:5] # (0):5 , 0 생략가능, 0~4까지 5개의 데이터
    print(data1)
    print(type(data1),data1.shape)
    
# test3()

def dest3a():
    data = np.random.rand(10)
    print(data)
    print(type(data),data.shape)
    
    data1 = data[:5]
    print(data1)

# dest3a()

def test4():
    data = np.random.randint(0,100,10)
    print(data)
    
    data1 = data[0:3]
    print(data1)
    print(type(data1),data1.shape)
    
    # data2 = data[4:] # [-5:]
    data2 = data[-5:] # [-5:] 5번째 부터
    print(data2)
    
# test4()

# 2차원 데이터
# shape (R,C) (3,4) 
def test5():
    data = np.random.randint(0,100,(5,3))
    print(data)
    print(type(data),data.shape)
    # d[y][x] / d[y,x]
#  [[96  9 46]
#  [15 23 16]
#  [92 23 68]
#  [28 74 70]
#  [71 46 43]]
# test5()

def test5a():
    data = np.random.randint(0,100,(10,5))
    print(data)
    print(type(data),data.shape)

# test5a()

#특정위치 값 변경하기
def test6():
    data = np.random.randint(0,10,(5,3))
    print(data)
    
    print(data[0][1],data[0,1])
    
    data[4,2] = 99
    print(data)
    
# test6()

def test6a():
    data = np.random.randint(0,100,(10,4))
    print(data)
    
    print(data[4,2])
    data[9,3] = 88
    print(data)
    
# test6a()

#데이터 자르기
# r 자르기, c 자르기
def test7():
    data = np.random.randint(0,100,(10,3))
    print(data)
    
    
    # 처음부터 3명분의 데이터를 추출
    data1 = data[:3,:] #[y,x]
    print("--------------------")
    print(data1)
    
    print("--------------------")
    data2 = data[-3:,:] 
    print(data2)
# test7()

def test7a():
    data = np.random.randint(0,100,(10,6))
    print(data)
    print(type(data),data.shape)
    
    print("--------------------")
    data1 = data[1:6,:] # 두번째 줄에서 5번째까지 
    print(data1)
    
    print("--------------------")
    data2 = data[-3:,:] # 밑에서 r 3줄, c 전체 줄
    print(data2)
    print(data2.shape) # (3,6)
    
# test7a()

# 원하는 행만 자르기 
def test8():
    data = np.random.randint(0,100,(10,3))
    print(data)
    print(data.shape) #국 영 수
    
    print("--------------------")
    data1 = data[:,:2] # 0,1 국 영 점수 가져오기
    print(data1)
    print(data1.shape)
    
    print("--------------------")
    data2 = data[:,[1]] # 영어[1] 점수 줄 가져오기
    print(data2)
    print(data2.shape)
    
    print("--------------------")
    data3 = data[:,[0,2]] # 국어[0]와 수학[2]줄 점수만 가져오기
    print(data3)
    print(data3.shape)
    
    
# test8()

def test8a():
    data = np.random.randint(0,100,(7,4)) # 7명의 국영수과 데이터
    print(data)
    print(data.shape)
    print("--------------------")
    
    data1 = data[:,:2] # 국[0]영[1] 데이터 
    print(data1)
    print(data1.shape)
    
    print("--------------------")
    data2 = data[:,[1,3]]  # 영[1], 과[3] 데이터 
    print(data2)
    print(data2.shape)
    
    print("--------------------")
    data3 = data[:,[2]] # 수[2] 데이터
    
# test8a()

# 데이터 합치기
# y합치기, 컬럼합치기
# 조건 : shape가 (10,3), (5,3) c 개수가 같아야함
# axis = 0 r 합치기 : c(x)값이 동일 
# axis = 1 c 합치기 : r(y)값이 동일
def test9():
    #a
    data1 = np.random.randint(0,100,(5,3))
    #b
    data2 = np.random.randint(0,100,(3,3))
    
    print(data1,data1.shape)
    print("--------------------")
    print(data2,data2.shape)
    
    print("--------------------")
    data3 = np.concatenate([data1,data2]) #r 합치기
    print(data3,data3.shape)
    
# test9()

def test9a():
    #a
    data1 = np.random.randint(0,100,(3,5))
    #b
    data2 = np.random.randint(0,100,(3,10))
    
    print(data1,data1.shape)
    print("--------------------")
    print(data2,data2.shape)
    
    print("--------------------")
    data3 = np.concatenate([data1,data2], axis =0) # axis0 생가
    print(data3,data3.shape)

# test9a()

# 옆으로 붙, r 같음
def test10():
    data1 = np.random.randint(0,100,(10,3)) # 국 영 수
    print(data1,data1.shape)
    
    print("--------------------")
    data2 = np.random.randint(0,100,(10,2)) # 물 화
    print(data2,data2.shape)
    
    print("--------------------")
    data3 = np.concatenate([data1,data2],axis = 1) # (10, 5)
    print(data3, data3.shape)
    
# test10()

def test10a():
    data1 = np.random.randint(0,100,(7,4)) # 7명의 4과목 시험
    print(data1,data1.shape)
    print("--------------------")
    
    data2 = np.random.randint(0,100,(7,3)) # 7명의 3과목 추가 시험
    print(data2,data2.shape)
    print("--------------------")
    
    data3 = np.concatenate([data1,data2],axis = 1)
    print(data3,data3.shape) # (7, 7)
test10a()


