# 산술연산
A = 1-2
B = 4*5
C = 7/5
D = 3**2

print(A,B,C,D)

# 자료형
A1 = type(10)
B1 = type(.27178)
C1 = type("Hello")

print(A1)
print(B1)
print(C1)

#변수
x = 10
print(x)

#리스트
a = [1,2,3,4,5]
print (a)
len (a)
a[0]
a[4]
a[3] = 99 # 값 대입

a[0:2]  #슬라이싱
print(a[0:-1])

#딕셔너리
me = {'height' : 180}
me['height']
me['weight'] = 64
print(me)

#부울린
hungry = True
sleepy = False
print(type(hungry))
print(not hungry)

#if문
hungry = True
if hungry:
        print("i'm hungry")


hungry = False
if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")
    print("I'm sleepy")

# for 문
for i in [1,2,3] :
    print (i)

#함수
def hello():
    print("HELLO WORLD")

hello()

