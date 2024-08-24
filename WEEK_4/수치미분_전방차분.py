#수치 미분
def numerical_diff(f,x):
    h= 1e-50
    return (f(x+h)-f(x))/h

#중앙 미분
def numerical_diff(f,x):
    h= 1e-4     #0.001
    return (f(x+h)-f(x))/(2*h)