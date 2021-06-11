from functools import partial


## Task 1
fibanociNumbers = [0,1]
for i in range(2,21):
  fibanociNumbers.append(fibanociNumbers[i-1]+fibanociNumbers[i-2])

CheckFibanoci = lambda inputNum : True if list(filter(lambda x:(x in fibanociNumbers),[inputNum] )) else False


# def CheckFibanoci(input):
#   res = True if list(filter(lambda x:(x in fibanociNumbers),[input] )) else False
#   return res

## task 2

## 2.1
total = 0
addevenodd = lambda list1,list2: sum([a+b for a,b in zip(list1,list2) if a%2==0 and b%2!=0])


## 2.2
output = ''
strip_vowel = lambda inputString: ''.join([output+x for x in inputString if ord(x) not in [97,101,105,111,117] ])

## 2.3
import math
Array_1d = [3,-4,5,6,7,8]
sigmoid = lambda input_array: [(1/(1+math.exp(-x))) for x in input_array]


## 2.4
stringName = 'tsay'
dict1 = {118:92,119:93,120:94,121:95,122:96}
shitbyfive = lambda inputString: ''.join([chr((ord(each)+5)) if (ord(each) not in dict1.keys())  else chr(dict1[ord(each)]+5) for each in inputString  ])


## Task 4
# 4.1
from functools import reduce
list1 = [2,3,4,5,6,7]
addEvenNumbers = lambda list1: reduce(lambda a,b : a+b, filter(lambda x:x%2 ==0 ,list1) )

# 4.2
list2 = ['a','b','c','d','Z']
findbig = lambda list1: reduce(lambda a,b : a if a>b else b, list2 )
#print(result)

# 4.3 
list1 = [10,1,2,3,4,5,6,7]
addthirdnum = lambda list1: reduce(lambda a,b : a+b, [x for x in range(1,len(list1)) if x%3==0]  )



# Task 5
import random 

numberlist = list(range(10,99+1))
numberlist2 = list(range(1000,9999+1))
alphalist = list(map(chr,range(65,91)))
numberplateGeneration = lambda numberlist,numberlist2,alphalist: ['KA'+str(a)+str(b)+str(c)+str(d) for a, b,c,d in zip(random.choices(numberlist,k=15),random.choices(alphalist,k=15),random.choices(alphalist,k=15), random.choices(numberlist2,k=15))]


# Task 6
def GenrateNumberPlate(state, division, alpha, number):

  if (not isinstance(state, str)) or (len(state)!=2):
    raise ValueError("Please provide two state name")
  if (not isinstance(division, int)) or (len(str(division))!=2):
    raise ValueError("Please provide two digit region division")
  if (not isinstance(number, int)) or (len(str(number))!=4):
    raise ValueError("Please provide four digit integer")
  if (not isinstance(alpha,str)) and (len(alpha)==2):
    raise ValueError("Please provide two digit alpha")
  return state + str(division) + alpha + str(number)
partialNumPlate =  partial(GenrateNumberPlate, division=12, alpha='WQ' , number=1000)
partialNumPlate('DL')




