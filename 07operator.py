# ** : 제곱
# // : 몫
# % : 나머지
print(3**3)
print(10//3)
print(10%3)
# 27
# 3
# 1


# and, or ,not
a = 1
b = 0

if(a == 1 and b == 1) : print("true") 
else : print("false") 

if(a == 1 and not(b == 1)) : print("true") 
else : print("false") 

if(a == 1 or b == 1) : print("true") 
else : print("false") 

# false
# true
# true

# in
lst = [1,2,3,4,5]
print(1 in lst)
# true

# bool
print(bool(1))
print(bool(0))