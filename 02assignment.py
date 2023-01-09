# 메모리 할당
a = '붕어빵'
print(a, '>>', id(a))

b = a
print(b, '>>', id(b))

a = '잉어빵'
print(a, '>>', id(a))

# 붕어빵 >> 1796663963888
# 붕어빵 >> 1796663963888
# 잉어빵 >> 1796663965040


a = [1,2,3,4,5]

b = a

c = [1,2,3,4,5]


print(id(a))
print(id(b))
print(id(c))

# 2031521729600
# 2031521729600
# 2031522705728

# is : 같은 객체인지 판단
print(a is b)
print(a is c)
print(b is c)

# True
# False
# False


# == : 같은 값인지 판단
print(a == b)
print(a == c)
print(b == c)

# True
# True
# True


a = 101
b = 100 + 1

print(a is b)

print(id(a))
print(id(b))

print(a == b)

c = 'korea'
d = 'korea'

print(c is d)
print(c == d)

e = [1,2,3,4,5]
f = [1,2,3,4,5]

print(e is f)
print(e == f)

# True >> 숫자는 기존에 있는거 할당
# True
# True >> 문자열은 기존에 있는거 할당
# True
# False >> 리스트는 따로 할당됨
# True

a = "korea"
print(id(a))
# 1389725845872

b = "korea"
print(id(b))
print(a is b)
# 1389725845872
# True

b += "!"
print(b, id(b))
print(a is b)
# korea! 1389726824624
# False

c = b[:-1]
print(c, id(c))
print(a is c)
# korea 1389726903024
# False