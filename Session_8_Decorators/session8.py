from functools import wraps
from datetime import datetime
from time import perf_counter

# Decorator that allows to run a function only at odd seconds, else prints out "We're even!"
def odd_it(fn: "Function") -> 'Function':
	"""
	Wrapper for running a specific function during input time.
	:param fn: function to run at odd seconds
	:type fn: function
	:return func: closure function
	"""
	def inner(*args, **kwargs) -> 'Integer':
		"""
		:result : Result of executed function in case if its a odd second
		"""		
		if datetime.now().second % 2 != 0:			
			result = fn(*args, **kwargs)			
			return result
		else:
			print("We're even!")			
			return None 
	return inner

# The same logger that we coded in the class
# it will be tested against a function that will be sent 2 parameters, and 
# it would return some random string. 
def logger(fn: "Function") -> 'Function':	
	"""
	Wrapper for logging execution time, arguments, description and return type
	:param fn: function to be logger
	:type fn: function
	:return func: closure function
	"""
	from functools import wraps 
	from datetime import datetime, timezone
	import inspect
	import ast
	@wraps(fn)
	def inner(*args, **kwargs):
		"""
		:result : Result of executed function in case if its a odd second
		"""	
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



# start with a decorator_factory that takes an argument one of these strings, 
# high, mid, low or no
# then write the decorator that has 4 free variables
# based on the argument set by the factory call, give access to 4, 3, 2 or 1 arguments
# to the function being decorated from var1, var2, var3, var4
# YOU CAN ONLY REPLACE "#potentially missing code" LINES WITH MULTIPLE LINES BELOW
# KEEP THE REST OF THE CODE SAME
def decorator_factory(access:str) -> 'Function':
	"""
	Factory for giving access to variables depending on priority/access level
	:param access: Tells the access level
	:type access: String
	:return func: closure function
	"""	
	var1 = "1"
	var2 = "2" 
	var3 = "3" 
	var4 = "4" 
	def check_access(fn) -> 'Function':
		"""
		Wrapper for giving access to variables
		:param fn: function to give access level
		:type fn: function
		:return func: closure function
		"""		
		def inner(*args,**kwargs) -> 'Tuples':
			"""
			:vars : Depending of access level a tuple of variables will be returned
			"""	
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

# The authenticate function. Start with a dec_factory that sets the password. It's inner
# will not be called with "password", *args, **kwargs on the fn
def authenticate(set_password) -> 'Function':	
	"""
	Factory for authenticating a password
	:param set_password: Original password set by developer
	:type set_password: String
	:return func: closure function
	"""	
	def authenticate_user(fn) -> 'Function':
		"""
		Wrapper for authenticating a password
		:param fn: function to authenticate
		:type fn: function
		:return func: closure function
		"""	
		def inner(user_password) -> 'String':
			"""
			:param user_password : password provided by user is checked
			:type user_password: function
			:return : "Amazing!" if user's password is matching else "Wrong Password"
			"""			
			if len(user_password) == 0:
				raise TypeError("Please provide a password")	
			if set_password == user_password:				
				return "Amazing!"
			else:
				return "Wrong Password"
		return inner	
	return authenticate_user

# The timing function
def timed(reps):
	"""
	Factory for calculating time of a function when ran "n" times
	:param reps: Number of times a function should run
	:type reps: String
	:return func: closure function
	"""	    
	import time 
	def timedwrap(fn):
		"""
		Wrapper for calculating time of a function when ran "n" times
		:param fn: function which is to be ran "n" times
		:type fn: function
		:return func: closure function
		"""	
		def inner(*args, **kwargs):
			"""			
			:return : result of the function executed
			"""		
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