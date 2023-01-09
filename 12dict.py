# dictionary
dictItem = {}

dictItem['id'] = '1'
dictItem['name'] = 'leo'
dictItem['phone'] = '01000000000'
dictItem['address'] = 'seoul'

# print all
for i in dictItem.items():
    print(i, end=' ')

# print keys
for i in dictItem.keys():
    print(i, end=' ')

# print values
for i in dictItem.values():
    print(i, end=' ')

# update
dictItem['id'] = 2
print(dictItem)

# insert
dictItem['gender'] = 'M'
print(dictItem)

# delete
del dictItem['phone']
print(dictItem)
