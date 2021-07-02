### EPAi - Session 8 

**Contents**

- odd_it
- logger
- decorator_factory
- authenticate
- timed

### odd_it()

    def odd_it(fn: "Function") -> 'Function':        
        def inner(*args, **kwargs) -> 'Integer':            	
            if datetime.now().second % 2 != 0:			
                result = fn(*args, **kwargs)			
                return result
            else:
                print("We're even!")			
                return None 
        return inner

**Description**

Wrapper for running a specific function during input time.
Gets a function as input and runs it only at odd seconds if its a even "second" then it prints out We're even and returns None

**Test**

In test decorator is used over adder function. Assert function is used to check cases when its odd and even.

### logger()

    def logger(fn: "Function") -> 'Function':
        from functools import wraps 
        from datetime import datetime, timezone
        import inspect
        import ast
        @wraps(fn)
        def inner(*args, **kwargs):		
            run_dt = datetime.now(timezone.utc)
            result = fn(*args, **kwargs)
            run_dt_end = datetime.now(timezone.utc)
            print(f'{fn.__name__}: called at {run_dt}')
            print(f'Execution time {run_dt_end - run_dt}')
            print(f'Function description {fn.__doc__}')
            print(f'Function annotation {fn.__annotations__}')
            print(f'arguments {inspect.signature(fn)}')
            print("return " + result )		
            return result 
        return inner 


**Description**

Wrapper for logging execution time, arguments, description and return type.
Result of executed function in case if its a odd secondis returned	

**Test**

A function(function_name) is decorated with logger and we are checking the output of it from console. it should contain function name, execution time, function description, function annotation, function description.

### decorator_factory()

    def decorator_factory(access:str) -> 'Function':		
        var1 = "1"
        var2 = "2" 
        var3 = "3" 
        var4 = "4" 
        def check_access(fn) -> 'Function':		
            def inner(*args,**kwargs) -> 'Tuples':			
                nonlocal var1,var2,var3,var4
                if access == "high":				
                    return var1,var2,var3,var4
                elif access == "mid":				
                    return var1,var2,var3
                elif access == "low":				
                    return var1,var2
                elif access == "no":				
                    return var1
                else:
                    return "Improper access keyword set"			
            return inner 
        return check_access


**Description**

Decorator Factory for giving access to variables depending on priority/access level.Wrapper for giving access to variables. it can get the priority as string and returned variables correspodingly.
Depending of access level a tuple of variables will be returned

**Test**

Decorator factory is used on a function and we are passing high, mid, log, no and random strings to test if its behaving correspondingly.


### authenticate()


    def authenticate(set_password) -> 'Function':			
        def authenticate_user(fn) -> 'Function':		
            def inner(user_password) -> 'String':						
                if len(user_password) == 0:
                    raise TypeError("Please provide a password")	
                if set_password == user_password:				
                    return "Amazing!"
                else:
                    return "Wrong Password"
            return inner	
        return authenticate_user


**Description**

Decorator factory for authenticating a password which can get the original password from developer,
Wrapper for authenticating a password is written and
password provided by user is checked in inner() with original password and closure returns "Amazing!" if it matched else it returns "Wrong Passoword"

**Test**

When user gives no password it should raise a type error. When password other than "secret"(dev designed password) is passed it should return "Wrong password" and if it matches then "Amazing!" is returned

### timed  ()

    def timed(reps):
        import time 
        def timedwrap(fn):
            def inner(*args, **kwargs):			
                average = 0	
                for i in range(reps):
                    start_time = time.perf_counter()
                    result = fn()
                    end_time = time.perf_counter()
                    run_time = end_time - start_time
                    print("Run time ", run_time)
                    average += run_time
                average = average/reps
                print(f"Average time for {reps} iterations",average ,"s")
                return result
            return inner
        return timedwrap

**Description**

Decorator Factory for calculating time of a function when ran "n" times. Decorator factory gets repetation times as a string. Wrapper for calculating time of a function when ran "n" times. Results of the function executed is returned.

**Test**

@timed decorator is used on a function that sleeps for some seconds, decorator should get repetations specified in decorator parameter and return average time taken to run .