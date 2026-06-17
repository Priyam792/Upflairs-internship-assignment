# Create a function that calculates simple interest.  
# Use default arguments for rate and time. 
# Demonstrate calling the function using both positional and keyword arguments

#Solution -->

def simple_intrest(principal,rate = 8 , time = 2):
    SI = (principal * rate * time) / 100
    print(SI)

## POSITIONAL ARGUMENTS
simple_intrest(1000,9,4)

## KEYWORD ARGUMENTS
simple_intrest(principal=3000,rate=5,time=4)