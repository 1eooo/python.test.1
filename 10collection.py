# list []
# tuple ()
# set {}
# dict {}

# [1, 2, 3, 4, 5] <class 'list'>
# (1, 2, 3, 4, 5) <class 'tuple'>
# {1, 2, 3, 4, 5} <class 'set'>
# {'a': 97, 'b': 98} <class 'dict'>

# if dont use list
person1_name = 'leo'
person1_age = '몰?루'
person1_phone = '010-0000-0000'
person1_address = 'seoul'

print(person1_name)
print(person1_age)
print(person1_phone)
print(person1_address)
# leo
# 몰?루
# 010-0000-0000
# seoul



# if use list
person1 = ['leo', '몰?루', '010-0000-0000', 'seoul']
print(person1)
# ['leo', '몰?루', '010-0000-0000', 'seoul']



# int list
intList = [1, 2, 3, 4, 5]

# float list
floatList = [1.0, 2.0, 3.0, 4., 5.]

# char list
charList = ['a', 'b', 'c', 'd', 'e']

print(intList, type(intList))
print(floatList, type(floatList))
print(charList, type(charList))
# [1, 2, 3, 4, 5] <class 'list'>
# [1.0, 2.0, 3.0, 4.0, 5.0] <class 'list'>
# ['a', 'b', 'c', 'd', 'e'] <class 'list'>


# 모든 자료형 담기 가능
allTypeList = [ 1,
                1.0,
                'a',
                'bab', 
                [1, 2, 3, 4, 5], 
                (1, 2, 3, 4, 5), 
                {'a' : 1, 'b' : 2}
            ]
print(allTypeList)
# [1, 1.0, 'a', 'bab', [1, 2, 3, 4, 5], (1, 2, 3, 4, 5), {'a': 1, 'b': 2}]
