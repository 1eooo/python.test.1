#상수 vs 변수
PI = 3.14
GRAVITY = 9.8
print(PI)

# python에는 상수 없음
PI = 6 
print(PI)

# print() : console 출력
a = 100
b = 3.14
c = 'k'
d = 'Hello world'
e = ' '
# print(a)
# print(b)
# print(c)
# print(d)
print(a, e, a, e, a, e, a, e, a)


#다중할당
a = b = c = d = e = 100, 200, 300
#print(a,b,c,d,e)

print(type(a))
#class 'tuple'

a = b = c = d = 100, 3.14, 'k', 'korea'
print(type(a))
print(a)

# '', "" example
print('나는 엄마에게 말했다. "더 이상 카레는 먹기 싫어요!" 라고')
print('나는 엄마에게 말했다. "더 이상 \'카레\'는 먹기 싫어요!" 라고')
