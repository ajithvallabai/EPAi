# Session 3 assignment of EPAi3.0

## Numeric Types - I


### encoded_from_base10
    Three paramters are to be passed number, base and digit_map
    - number(int) contains a ordinary base 10 number
    - base(int) contains the number to which base is to be converted
    - digit_map(string) contains encodings

    We raise a ValueError ("base value and digit map length are different! it should be equal") if base value and length of digit map is different
    We raise a error ("Base value must be from 2 to 36") if base is not from 2 to 36
    We raise a ValueError ("base value and digit map length are different! it should be equal") if base value and length of digit map is different
    We raise a error ("please provide unique digit map values") if digit map numbers are not unique
    We raise a ValueError ("base value and digit map length are different! it should be equal") if base value and length of digit map is different

    if number is less than 0 we are making it positive , if its zero then we are returning digit_map[0]
    We are using divmod function to get the numerator and denominator and we are reducing the "number" variable

    if "nummber" is less than zero we are adding a negative symbol infront and returning

    hex() function converts a integer to corresponding hexadecimal number in string form and returns

    bin() converts and returns binary equivalent string of a given integer

    Test-
        - All basic test are done
        - In test_hexadecimal_conversions() 50 numbers randomly from 0 to 32767(positive number) is passed and then checked whether its correct or not

        - In test_hexadecimal_conversions() 50 numbers randomly from -1 to -32767(negative number) is passed and then checked whether its correct or not


### float_equality_testing()
    it takes two numbers and checks if its close or not with certian conditions relative tolerance and absolute tolerance.
    We are taking maximum of absolute values of a and b and multiplying with relative tolerance. Then we are taking maxmimum of above result and absolute torlerance . Further we are comparing with absolute difference between a and b and returning the result. it is to simulate isclose function which takes a , b , relative tolerance and absolute tolerance parameters

    Test-
        - for 10 thousand times two numbers ( a and b) that are closer are passed 


### manual truncation function
    f_num -> int
    it takes a number and then converts to a string and then takes the value before "." . After getting that value it converts to integer without using int type casting. it is to stimulate truncation function from math.

    test-
        - for hundered times a random number is passed to truncation function

### manual rounding function
    We are taking the decimal numbers and checking whether its greater than 0.5 or not. if its so we are returing numerator +1 else we are giving the floor value. it stimulate round() function from math
    Test -
        - Four numbers are taken and their rounding of value is compared with the implemented function and the equality is checked

### rounding away from zero
    We are taking a divmod and checking if its above positive, zero or negative .if its zero, zero is returned if its positve decimal point is checked if its greater than 0.5 we are adding 1. if its a negative number and above 0.5 we are decreasing by 1
