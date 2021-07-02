from fractions import Fraction

def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    if base < 2 or base > 36:
        raise ValueError("Input base value must be from 2 to 36")
    if len(digit_map) != len(set(digit_map)):
        raise ValueError("please provide unique digit map values some values are repeating please check it")
    if len(digit_map) != base:
        raise ValueError("base value and digit map length are different! it should be equal")
    digits = []
    case = 1
    if number < 0:
        number = number*-1
        case = -1
    elif number == 0:
        return digit_map[0]
    while number > 0:
        number,m = divmod(number,base)
        digits.insert(0,m)
    if case == 1:
        return "".join(digit_map[i] for i in digits)
    else:
        return "-"+"".join(digit_map[i] for i in digits)


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05    
    max_val = max(abs(a),abs(b))
    sTolerance = max(rel_tol*max_val, abs_tol)
    result = abs(a-b) <sTolerance
    return result


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''    
    f_num = str(f_num).split(".")[0]    
    f_num_length = len(f_num)
    num=0
    if "-" not in f_num:
        for i in f_num:
            num = num *10+(ord(i)-48)
        f_num = num 
    else:
        f_num = f_num[1:]
        for i in f_num:
            num = num *10+(ord(i)-48)
        num = num*-1
        f_num = num 
    return f_num

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    quo = f_num//1
    deno = f_num - quo
    if deno >=0.5:
        quo = quo+1
    else:
        quo = quo//1
    return quo

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    case = 1
    if f_num <0:
        case = -1
        f_num = f_num*-1
    elif f_num == 0:
        return 0
    quo, deno = divmod(f_num)
    if case == 1:
        if deno >0.5:
            quo = quo+1    
    else:
        quo += 1
        if deno > 0.5:
            quo = quo - 1
    return quo