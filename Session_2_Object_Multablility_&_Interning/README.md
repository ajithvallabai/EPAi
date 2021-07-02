# Session 2 assignment of EPAi3.0

## Object Mutability and Interning

### Contents

- Something()
- SomethingNew()
- add_something()
- clear_memory()
- critical_function()
- compare_strings_old()
- compare_strings_new()
- sleep()
- char_list()
- collection()
- __init__()

#### Something()

- Something is a class with constructor(init()) and a object "something_new: is declared in class and assigned None
- When a instance is created with Something() class, something_new is initalized by constructor

#### SomethingNew()

- SomethingNew class has two attributes "i" which is of datatype int and "something" which is assinged a class
- repr() is used to pass the test case which returns a string, previously it was returining default object

#### add_something()

- Creates cyclical reference using class and objects of "Something" and "SomethingNew()" classes
- repr() is used to pass the test case which returns a string, previously it was returining default object

#### clear_memory()

-  objects are deleted by collection.clear() and the Cyclical references made are deleted with gc.collect() 
- gc module provides access to garbage collector for reference cycles
- gc.collect() does a full collection of current garbage

#### critical_function()
- a list is created in the name of collection
- add_something function is called 1024*128 times , add-something function creates cyclical reference by calling both Something and something_new class
- clear_memory function is called to clear the collection list and free memory


#### compare_strings_old()
- "a" and "b" are created with a long string
- A forloop of n iterations is used to compare and check if "a" and "b" are equal
- inside the if loop pass is used which means it doing nothing and there is no else part
- A list is created in the name of char_list and a for loop is used n number of times to check it 
- inside the if loop pass is used which means it doing nothing and there is no else part

#### compare_strings_new()
- "a" and "b" are created with a long string with sys.intern so that references for those strings remain same as the values are same
- Now a forloop is used n times but as only references are compared because of string interning the program runs faster
- As the objective is to check only the presence of 'd' we can use a set instead of a list
- Both the for loops are combined to reduce the time further (loop fusion is done)

#### sleep()
- sleep function is used to pause the program for particular period of time 

#### char_list()
- a set is used instead of a list as the objective to find only the presence of "d"


#### collection
- collections is list in which each object is appended with cyclical reference and to clear the objects we are using list.clear() and to the references it has made we are using gc.collect()
- collection is passed as a parameter in add_something function and then cyclical references are made in add_something function, later the memory is cleared using clear_memory function


#### __init__()
- init is a constructor and everything written in init will get executed as soon as function is called
- In something() class its used to and a object something_new is created


