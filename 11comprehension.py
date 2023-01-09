# 1
a = [1,2,3,4,5,6,7,8,9,10]
print(a)

# 2
for i in range(1, 11):
    print(i, end=', ')
print()

# 3
b = []
for i in range(1, 11):
    b.append(i)

print(b)

# list comprehension
c = [i for i in range(1, 11)]
print(c)


# list()
aa = list(i for i in range(1,11))
print(aa)

bb = list(i*i for i in range(1,11))
print(bb)

cc1 = list(i*i for i in range(1,11))
cc1.remove(cc1[4])
cc2 = list(i*i for i in range(1,11) if i != 5)
print(cc1)
print(cc2)

dd1 = list(i for i in range(1,51, 2))
dd2 = list(i for i in range(2,51, 2))
print(dd1)
print(dd2)
dd3 = list(i for i in range(1,51) if i%2 == 0)
dd4 = list(i for i in range(1,51) if i%2 != 0)
print(dd3)
print(dd4)


aaa = [(i,'X',j,'=',i*j) for i in range(1, 4) for j in range(1, 4)]
print(aaa)