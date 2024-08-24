import numpy as np

def function_2(x):
    return x[0]**2 + x[1]**2

def numerical_gradient(f,x):    #인수 f는 함수, x는 넘파이 배열
    h = 1e-4
    grad = np.zeros_like(x)     #x와 형상이 같고 원소가 모두 0인 배열 생성

    for idx in range(x.size):
        tmp_val = x[idx]        #f(x+h) 계산

        x[idx] = tmp_val +h     #f(x-h)계산
        fxh1=f(x)
        x[idx]=tmp_val -h
        fxh2 = f(x)

        grad[idx] = (fxh1-fxh2) / (2*h)
        x[idx] = tmp_val        # 값 복원
    return grad

print(numerical_gradient(function_2, np.array([3.0, 4.0]))) #[6., 8.]
print(numerical_gradient(function_2, np.array([0.0, 2.0]))) #[0., 4.]
