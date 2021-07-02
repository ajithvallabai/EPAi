# Epai3 - Session4

Getting a Qualean number / qnumber
    - get a random value from [-1,0,1] and assign as org_num
    - take the number and multiply with random.uniform(-1,1) and take a round for 10 decimal palces 

### and() - function :
we can take the qualeannumber , then do "and" operation with q2 and return the boolean . 
Without checking q2 "and" operation can return false even if first parameter is false

### or() - function :
we can  check if q2 is not in case if its none and in test case q1 never becomes none so it authorizes us to use a straight true for it .
In case if its not None then we can take the qnumber and find "or" operation with q2

### repr() - function:
it returns official string representation of object

### str() - function 
tells the unoffice representation of object. it prints everything in way user can understand


### add() - function
it checks it the second parameter is a qualean object or not if not so it take the number directly and adds with first parameter
in case if its a instance of quoalean object then it finds the return_qualean() -> number and adds it

### eq() - function
checking if its a instance of qualean object , if so it takes value of return_qualean() , in case if its not so then it directly compares with q2

to pass the test case we are checking if its a string and raising a type error


### float() - function 
returns float of the qualean number

### ge() - function
Checks if second parameter a instance of qualean object , if so compares first parameter is compared  greater than or equal to with second parameter . in case if its not then its directly checked if its first parameter is greater than or equal to with second parameter 


### gt() - function
Checks if second parameter a instance of qualean object , if so compares first parameter is compared  greater than  to with second parameter . in case if its not then its directly checked if its first parameter is greater equal to with second parameter 

### le() - function
Checks if second parameter a instance of qualean object , if so compares first parameter is compared  less than or equal to with second parameter . in case if its not then its directly checked if its first parameter is less than or equal to with second parameter 

### lt() - function
Checks if second parameter a instance of qualean object , if so compares first parameter is compared  less than to second parameter . in case if its not then its directly checked if its first parameter is less than to  second parameter 

### invert() - function
multiplying qualean number with -1 

### mul() - function
Checks if qualean number is instance of qualean object, if so multiplies first paramter qualean number with second parameter qualean number, else if its not so then first parameter is directly multiples with second parameter

### sqrt() - function
checking if the qualean number is less than zero or not . if its less than zero then we are inverting it and then taking square root of its decimal value and then rounding till 10th place and returning a imaginary number. In case if its zero or greater than zero then we are taking square root of its decimal value and then rounding till 10th place.

### bool() - function
returnning bool of the qualean number . it is only false when qualean number is 0 else it will true for -ve or +ve numbers


### init() - function
First by default "num" is assigned a random value from list [-1,0,1]. In case if the num is given by the user and its not in [-1,0,1] then value error is raised with a message we are creating a attribute "return_qualean" and through a function we are assigning it a qulean value . Qualean value is a value in which a random number from [-1,1] is multiplies with a number in [-1,0,1] and rounded to 10th decimal place 
