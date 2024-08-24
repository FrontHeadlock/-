import numpy as np
x = np.array([0, 1])        #입력
w = np.array([0.5, 0.5])    #가중치
b= -0.7                     #편향

print(w*x)
#[0. 0.5]
print(np.sum(w*x))
#0.5
print(np.sum(w*x)+b)
#대략 -0.2





