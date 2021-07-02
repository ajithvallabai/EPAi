"""Squared_power_list, Polygon_area calculation, TempConverter, SpeedConverter are implemented and timer is integrated with it"""
import time
from math import tan, pi 
def time_it(fn, *args, repetitions= 1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""
    total_time = 0
    # Repetition should be positive number    
    for i in range(0,repetitions):
        start = time.perf_counter() 
        fn(*args,**kwargs)
        end = time.perf_counter() 
        total_time += (end-start)
    return total_time

def squared_power_list(number,*args, start=0, end=5,**kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""    
    # Validations "if" block
    if len(args) >=1 :
        raise TypeError("takes maximum 1 positional arguments")
    if len(kwargs) >= 1:
        raise TypeError("maximum 2 keyword/named arguments")
    if not isinstance(number,int) :
        raise TypeError("Only integer type arguments are allowed")      
    if (start < 0) or (end < 0):
        raise ValueError("Value of start or end can't be negative")
    if start > end:
        raise ValueError("Value of start should be less than end")
    if number >= 10:
        raise ValueError("Value of number should be less than 10") 
    # Return the list of number to the power of numbers from start to end    
    result = []
    for i in range(start,end):
        result.append(number**i)    
    return result


def polygon_area(length, *args, sides = 3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""
    # Validations    
    if len(args) >=1:
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")
    if len(kwargs) >=1 :
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")       
    if not isinstance(length,int) :
        raise TypeError("A integer is expected for length")    
    if not isinstance(sides,int):
        raise TypeError("A integer is expected for sides")
    if sides in [0,1,2,7]:
        raise TypeError("Invalid sides value for a polygon")
    # Return area
    area = sides * (length ** 2) / (4 * tan(pi / sides))
    return area 

def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""
    # Validations
    if len(args)>=1:
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs)>=1:
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")        
    if not isinstance(temp_given_in,str):    
        raise TypeError("Charcater string expected")
    elif temp_given_in.isalpha() and (temp_given_in not in ['c','C','f','F']):
        raise ValueError("Only f or c is allowed")        
    if not ((isinstance(temp,int)) or (isinstance(temp,float))):        
        raise TypeError("A integer or float is expected")
    if temp <=-273.15 and temp_given_in in ['c','C']:
        raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")
    if temp <=-459.67  and temp_given_in in ['f','F']:
        raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")
    # Return the converted temprature    
    if temp_given_in == 'f' or temp_given_in == 'F':        
        return ((temp - 32)*5)/9
    elif temp_given_in == 'c' or temp_given_in == 'C':        
        return (temp*1.8) + 32

def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """
    # Validations
    if not (isinstance(speed,int) or isinstance(speed,float)) :     
        raise TypeError("Speed can be int or float type only")
    if not (isinstance(dist,str) ) :     
        raise TypeError("Charcater string expected for distance unit")    
    if not (isinstance(time,str) ):
        raise TypeError("Charcater string expected for time unit")
    if speed< 0:
        raise ValueError("Speed can't be negative")
    elif speed >=300001:
        raise ValueError("Speed can't be greater than speed of light")
    dist = dist.lower()
    time = time.lower()
    if time not in ['ms','s','min','hr','day']:
        raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")
    if dist not in ['km','s','m','ft','yrd']:
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")
    if len(args) >=1 :
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")    
    if len(kwargs) >=1:
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")
    # Return the converted speed    
    time_dict = {'h_ms' :  3600000, 'h_s': 3600 ,'h_min' : 60 ,'h_hr': 1 , 'h_day' : 0.0416667}
    distance_dict = {'km_km': 1, 'km_m': 1000, 'km_ft': 3280.8399999999001011, 'km_yrd': 1093.610}
    result = speed * (distance_dict["km_" + dist]/time_dict["h_" +time])    
    result = round(result,0)
    return result   