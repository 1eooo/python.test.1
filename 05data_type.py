a = 100
b = 3.14
c = 'korea'
d = '010-1234-5678'
lst = [1,2,2,4,5]
tpl = (1,2,2,4,5)
st = {1,2,2,4,5}
di = {'a':97, 'b':98}

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(lst, type(lst))
print(tpl, type(tpl))
print(st, type(st)) # 집합형 : 중복 X
print(di, type(di))

# 100 <class 'int'>
# 3.14 <class 'float'>
# korea <class 'str'>
# 010-1234-5678 <class 'str'>
# [1, 2, 3, 4, 5] <class 'list'>
# (1, 2, 3, 4, 5) <class 'tuple'>
# {1, 2, 3, 4, 5} <class 'set'>
# {'a': 97, 'b': 98} <class 'dict'>