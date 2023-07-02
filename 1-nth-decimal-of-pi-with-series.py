import math
# Function to calculate PI


def calculate_pi():
    PI = 3
    n = 2
    # Add for 1000000 times
    for i in range(0,100000):
        
        
        sign = (-1) **i
        PI = PI + (sign * (4 / ((n) * (n + 1)* (n + 2))))
 
        
        
 
        # Increment by 2 according to formula
        n += 2
        
    # Return the value of Pi
    return PI
 
# Function call
a = calculate_pi()

decimal=input("Please enter the decimal of pi you want to know.\n")
 
print("The approximation of Pi is ",end="")
print(round(a,int(decimal)))



b=(a*(10**int(decimal)))%10
print(f"the nth decimal of pi is : {int(b)}")
