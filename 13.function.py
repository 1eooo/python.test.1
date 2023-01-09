def testFunc1():
    print('붕어빵')

def testFunc2():
    print('개구리빵')

testFunc1()
testFunc2()


def testFunc3():
    result = '붕어붕어빵'
    return result

def testFunc4():
    result = '개굴개구리빵'
    return result

print(testFunc3())
print(testFunc4())


englishScore = [35, 66, 87, 98, 48, 88, 77, 65, 91, 79]

def maxScore(englishScore):
    return max(englishScore)

print(maxScore(englishScore))

def minScore(englishScore):
    return min(englishScore)

print(minScore(englishScore))

def maxMinScore(englishScore):
    return{ 'max':max(englishScore), 'min':min(englishScore)}
     
print('max : ', maxMinScore(englishScore)['max'], '/ min : ',maxMinScore(englishScore)['min'])



# list.sort() / sorted(list)

testList = [9, 10, 7, 8, 5, 6]
testList.sort() #오름차순
print(testList)
testList.sort(reverse=True) #내림차순
print(testList)

testList = [9, 10, 7, 8, 5, 6]
sortedTestList = sorted(testList) #오름차순 reverse=False
print(sortedTestList)

sortedTestList = sorted(testList, reverse=True) #내림차순
print(sortedTestList)


# parameter assign
def parameterTest(id, name, strength) :
    return id, name, strength

print(parameterTest('3', 'leo', '1000'))
print(parameterTest(name='3', strength='leo', id='1000'))


# default parameter
def defaultParameterTest(price, taxRate = 0.1):
    tax = round(price/(1+taxRate))
    originPrice = price-tax
    result = (originPrice, tax, price)
    return result

print(defaultParameterTest(11000))


# 가변 parameter
def variableParameter(*param) :
    result = 'input '+(str)(len(param))+' params sum : '+(str)(sum(param))
    return result

print(variableParameter(1,1,1,1))
print(variableParameter(1,2,3,4,5,6,7,8,9,0))

def variableParameterCheck(*param) :
    eSum = 0
    eCnt = 0
    for i in param :
        if i%2 != 0 :
            eSum += i
            eCnt += 1
    result = (eCnt, eSum)
    return result

print(variableParameterCheck(1,1,1,1))
print(variableParameterCheck(1,2,3,4,5,6,7,8,9,0))