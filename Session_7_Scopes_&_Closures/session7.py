## Task 1
def check_docstring(max_len) -> 'Function':  
    """
    Wrapper for closure function which checks doc string length
    :param max_len: Gets the length of docstring that a function should contain
    :type max_len: Integer
    :return func: closure function
    """  
    if not isinstance(max_len,int):
        raise TypeError("Needs a integer as input")
    def docstring_fifty(func) -> 'bool':
        '''        
        :param func: Gets the function of which doc string is to be checked
        :type func: function
        :return result: True or False if doc string is above specified length or below specified length 
        '''       
        if not hasattr(func, '__call__'):
            raise TypeError("Needs a function as input")
        result = len(func.__doc__) > max_len
        return result
    return docstring_fifty

## Task 2
def generate_fibanoci() -> 'Function':   
    """
    Wrapper to generate fibanoci number
    Every time when closure is called we can get new fibnoci number
    :return next_fib: Closure function
    """

    n = 0    
    def next_Fib() -> 'Integer' :
        """
        Generates fibanoci number every time when function is called
        :return : Next fibanoci number
        """
        a = 0
        b = 1
        c = 0
        nonlocal n    
        if (n==0):
            n = n + 1            
            return 0
        elif n==1:
            n = n + 1            
            return b 
        else:            
            for i in range(1,n):
                c = a + b
                a = b
                b = c 
            n = n + 1
            return b
    return next_Fib

## Task 3
function_call_counter = dict()
def function_counter() -> 'Function':
    """
    Wrapper for counting number of times a function is called
    :return inner: add/mult/div is passed
    """
    count = dict()
    def inner(fn,*args, **kwargs) -> 'Function(*args, **kwargs)':
        """
        :fn : function is passed and global counter is used to count 
        :return fn(*args, **kwargs): funciton is called with arguments
        """
        if not hasattr(fn, '__call__'):
            raise TypeError("Needs a function as input")
        nonlocal count 
        count[fn.__name__] = count.get(fn.__name__, 0) + 1
        function_call_counter[fn.__name__] = count[fn.__name__] 
        return fn(*args, **kwargs)
    return inner

## Task 4 
def function_counter_mod(user_dict) -> 'Function':
    """
    Wrapper for counting number of times a function is called with a user input dictionary
    :param dict1: User defined dictionary 
    :type dict1: dictionary
    :return inner: add/mult/div is passed
    """
    if not isinstance(user_dict,dict):
        raise TypeError("Needs a dictionary as input")
    def inner(fn, *args, **kwargs) -> 'Function':
        """
        :fn : function is passed and global counter is used to count 
        :return fn(*args, **kwargs): funciton is called with arguments
        """
        if not hasattr(fn, '__call__'):
            raise TypeError("Needs a function as input")          
        user_dict[fn.__name__] = user_dict.get(fn.__name__, 0) + 1
        return fn(*args, **kwargs)
    return inner 

