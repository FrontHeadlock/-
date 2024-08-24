import numpy as np

#1차원 배열
x=np.array([1.0, 2.0, 3.0])
print(x)
#[1. 2. 3.]
type(x)
#<class 'numpy.ndarray'>


x=np.array([1.0,2.0,3.0])
y=np.array([2.0,4.0,6.0])
print(x+y)
print(x-y)
print(x*y)
print(x/y)

#2차원 배열
A= np.array([[1,2],[3,4]])
print(A)
print(A.shape)
print(A.dtype)

#브로드캐스트
A=np.array([[1,2],[3,4]])
B=np.array([10,20])
print(A*B)

X=np.array([[51,55],[14,19],[0,4]])
print(x[0])
#array([51,55])
print(x[0][1])
#55

for row in X:
    print(row)
#[51 55] [14 19] [0 4]

#평탄화
x=x.flatten()
print(x)
#[51 55 14 19 0 4]








