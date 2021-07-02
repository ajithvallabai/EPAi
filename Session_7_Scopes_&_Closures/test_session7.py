import session7
import pytest
import os 
import inspect
import re 

README_CONTENT_CHECK_FOR = [
    'check_docstring',
    'generate_fibanoci',
    'closure',
    'free variable',
    'non local',
    'function_counter',
    'function_counter_mod'
]

### Readme test

def test_session7_readme_exists():
    """ Checks if readme.md file exists    """    
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session7_readme_100_words():
    """ Checks if Readme contains atleast 500 words """    
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 500 words"


def test_session7_readme_proper_description():
    """ Checks if important contents are being convered in readme    """    
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:            
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session7_readme_file_for_more_than_10_hashes():
    """ Checks if we have done proper formating  """    
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_session7_function_name_had_cap_letter():
    """ Checks if all function in session5 has used any captial letters    """    
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

## Tast 1 test



# doc strings,  input value , check if 50is a free variable

def test_check_docstring_doc_string():
    """ Check if doc string is more than 50 in length"""
    assert len(session7.check_docstring.__doc__) > 50, "Please improve your length of doc strings" 

def test_input_values():
    """ Checks if Type error is raised for string input and non function input"""
    with pytest.raises(TypeError):
        session7.check_docstring('fifty')
    with pytest.raises(TypeError):        
        inp = session7.check_docstring(50)
        inp(34)

def test_check_docstring_closure():
    """ Checks if function has closure """
    inp = session7.check_docstring(50)
    assert len(inp.__closure__) >= 1

def test_free_variable():
    """ Checks if there is a free variable """
    assert len(session7.check_docstring(50).__code__.co_freevars) == 1, "There should be 1 free variable"

def test_check_docstring_funcitonality():
    """ Checks if a Closure function has doc string greater than 50 """
    def add(a,b):
        '''
        This function is one and one and it adds
        This function is one and one and it adds
        a: input of first number to be added
        b: input of second number to be added
        return total: sum of a+b
        '''
        total = a+b
        return total
    docStringLengthCheck = session7.check_docstring(50)
    assert docStringLengthCheck(add) == True, "Please check your doc string functionality"

def test_generate_fibanoci_closure():
    """ Checks if function has closure """
    fibGenerate = session7.generate_fibanoci()
    assert len(fibGenerate.__closure__) >= 1, "You need to write a closure"

def test_generate_fibanoci_functionality():
    """ Checks if fibanoci number is generated next to next """
    fibGenerate = session7.generate_fibanoci()
    assert fibGenerate() == 0, "Please check you closure functionality"
    assert fibGenerate() == 1, "Please check you closure functionality"
    assert fibGenerate() == 1, "Please check you closure functionality"
    assert fibGenerate() == 2, "Please check you closure functionality"
    assert fibGenerate() == 3, "Please check you closure functionality"
    assert fibGenerate() == 5, "Please check you closure functionality"

## Task 3

def test_function_counter_closure_presence():
    """ Checks if function has closure """
    funcCount = session7.function_counter()    
    assert len(funcCount.__closure__) >= 1, "You need to write a closure"


def test_function_counter_functionality():
    """ Checks if function counter has its functionlality """
    funcCount = session7.function_counter()
    def mult(a, b, c):
        return a * b * c 
    def add(a, b):
        return a + b
    def div(a, b):
        return a/ b
    funcCount(add, 1, 2)
    funcCount(mult, 1, 2, 3)
    funcCount(add, 1, 2)
    funcCount(mult, 1, 2, 3)
    funcCount(div, 4, 2)
    funcCount(div, 4, 2)
    assert session7.function_call_counter == {'add' : 2,'mult' : 2, 'div': 2}, "Please check functionality"
    funcCount(mult, 1, 2, 3)
    assert session7.function_call_counter == {'add' : 2,'mult' : 3, 'div': 2}, "Please check functionality"
    

def test_function_counter_dictionary_assurance():
    """ Checks if we change global variable "function_call_counter" and if its changing 
    original counter """
    funcCount = session7.function_counter()
    def mult(a, b, c):
        return a * b * c 
    def add(a, b):
        return a + b
    def div(a, b):
        return a/ b
    session7.function_call_counter = {'add': 4}
    funcCount(add, 1, 2)
    funcCount(mult, 1, 2, 3)
    funcCount(add, 1, 2)
    funcCount(mult, 1, 2, 3)
    funcCount(div, 4, 2)
    funcCount(div, 4, 2)
    
    assert session7.function_call_counter == {'add' : 2,'mult' : 2, 'div': 2}, "Please check functionality"
    
def test_function_counter_input_check():
    """ Checks if its taking correct input """
    funcCount = session7.function_counter()    
    def add(a, b):
        return a + b    
    with pytest.raises(TypeError):
        funcCount(4, 1, 2)

def test_function_counter_doc_string_presence():
    """ Checks if doc strings are present in function """
    assert len(session7.function_counter.__doc__) > 10, "Please improve your length of doc strings" 


def test_function_counter_annotations():
    """ Checks if annotations are  present in function """
    assert len(session7.function_counter.__annotations__) > 0, "Please write annotations"

## Test next 6 




def test_function_counter_mod_doc_string_presence():
    """ Checks if doc strings are present in function """
    assert len(session7.function_counter_mod.__doc__) > 10, "Please improve your length of doc strings" 


def test_function_counter_mod_annotations():
    """ Checks if annotations are  present in function """
    assert len(session7.function_counter_mod.__annotations__) > 0, "Please write annotations"

def test_generate_function_input_check():
    """ Checks if we are providing a function to closure """
    dict1  = dict()
    funcCount = session7.function_counter_mod(dict1)    
    def add(a, b):
        return a + b    
    with pytest.raises(TypeError):
        funcCount(4, 1, 2)

def test_function_counter_mod_functionality():
    """ Checks if properfly the function is taking place """
    function_call_counter_user = {'add':45,'mult':3}
    funcCount = session7.function_counter_mod(function_call_counter_user)
    def mult(a, b, c):
        return a * b * c 
    def add(a, b):
        return a + b
    def div(a, b):
        return a/ b
    funcCount(add, 1, 2)
    funcCount(mult, 1, 2, 3)
    funcCount(add, 1, 2)
    funcCount(mult, 1, 2, 3)
    funcCount(div, 4, 2)
    funcCount(div, 4, 2)    
    assert function_call_counter_user == {'add' : 47,'mult' : 5, 'div': 2}, "Please check functionality"
    funcCount(mult, 1, 2, 3)
    assert function_call_counter_user == {'add' : 47,'mult' : 6, 'div': 2}, "Please check functionality"

def test_function_counter_mod_dict_assurance():
    """ Dictionary is modified at middle and checks if it rreturns it """
    function_call_counter_user = {}
    funcCount = session7.function_counter_mod(function_call_counter_user)
    def mult(a, b, c):
        return a * b * c 
    def add(a, b):
        return a + b
    def div(a, b):
        return a/ b
    funcCount(add, 1, 2)
    funcCount(mult, 1, 2, 3)
    funcCount(add, 1, 2)
    function_call_counter_user = {'add':45,'mult':3}
    funcCount(mult, 1, 2, 3)
    funcCount(div, 4, 2)
    funcCount(div, 4, 2)        
    assert function_call_counter_user == {'add':45, 'mult' : 3}, "Please provide user defined dict properly"
    
def test_function_counter_mod_input_check_dict():
    """ Checks if the input is a dictionary to function """
    with pytest.raises(TypeError):
        session7.function_counter_mod(45)    










