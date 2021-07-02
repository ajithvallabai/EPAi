# Epai3 - Session5

### Contents

- Timer function
- Squared power list
- Polygon_area
- Temp converter
- Speed converter

### Timer function:

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


- we can feed a function, parameters needed for function and number of times we need to repeat the calculation
- perf_counter() function is used to measure timing
- We need to measure only the time taken to execute a function so we need to use it only at start and end of the function instead of using it outside forloop

### Squared power list 
    
    def squared_power_list(number,*args, start=0, end=5,**kwargs):
        """Retruns list by raising number to power from start to end
        -> number**start to number**end. Default start is 0 and end is 5"""
        result = []
        for i in range(start,end):
            result.append(number**i)
        #print(result)
        return result

- Squared power list takes a number as input and iterates from start value to end value, during iteration it calculates the input power to the iter value.

    ```not isinstance(number,int) ```

- We are checking whether the number is integer else we would raise a Type error 

    ```len(args) >=1 , len(kwargs) >= 1```

- if any additional position arguments or keyword arguments  are given we are raise a Typeerror and informing user 

    ```(start < 0) or (end < 0) , start > end ```
- Start value and end value should not be negative , also start value should be less than end

    ```number >= 10```
- if number is greater than 10 raise a error

### Polygon_area
    def polygon_area(length, *args, sides = 3, **kwargs):
        """Retruns area of a regular polygon with number of sides between
        3 to 6 bith inclusive"""
        area = sides * (length ** 2) / (4 * tan(pi / sides))
        return area 
- Takes length and sides of the polygon as input and calculates the area of polygon with formula.

    ```sides in [0,1,2,7]```

- There is a constraint where it should calculate area for sides of 3 to 6 only 

    ```not isinstance(length,int) , not isinstance(sides,int)```

- if length or sides is not a int then error is thrown

### Temperature Converter 

    def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
        """Converts temprature from celsius 'c' to fahrenheit 'f' or
        fahrenheit to celsius"""
        if temp_given_in == 'f' or temp_given_in == 'F':            
            return ((temp - 32)*5)/9
        elif temp_given_in == 'c' or temp_given_in == 'C':            
            return (temp*1.8) + 32
    
- Temp converter takes in temperature as a input parameter and converts it to either farenhiet or celsius depending on "temp_given_in" parameter

    ```not ((isinstance(temp,int)) or (isinstance(temp,float))), temp_given_in.isalpha(), not isinstance(temp_given_in,str)```

- if the input temperature is not a int or float raise a error 

    ```temp <=-273.15, temp <=-459.67```

- temperature should not beless than -273.15 celsius and it should not be less than -459.67 Farenheit


### Speed_Converter 

    def speed_converter(speed, *args, dist='km', time='min', **kwargs):
        """Converts speed from kmph (provided by user as input) to different units
        dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

        time_dict = {'h_ms' :  3600000, 'h_s': 3600 ,'h_min' : 60 ,'h_hr': 1 , 'h_day' : 0.0416667}
        distance_dict = {'km_km': 1, 'km_m': 1000, 'km_ft': 3280.8399999999001011, 'km_yrd': 1093.610}
        result = speed * (distance_dict["km_" + dist]/time_dict["h_" +time])
        print("speed-",result)
        result = round(result,0)
        return result   

- In Speed converter , the speed in km/hr is given as a input and the desired conversion format is given in "dist" and "time" parameter
-We have used a dictinary and stored the conversion values in it so that we can easily fetch it when needed. it also reduces the code.
- Formula  = speed * ( distance_metrics/ time_metrics)

    ```speed< 0, speed >=300001```

- Speed should not be negative and it should not be more than speed of light

    ```not (isinstance(speed,int) or isinstance(speed,float))```
- Speed should be either a int or float

    ```not (isinstance(dist,str) ) ```
- Desired distance format should be a string

    ```not (isinstance(time,str) )```
- Desired distance time should be a string









