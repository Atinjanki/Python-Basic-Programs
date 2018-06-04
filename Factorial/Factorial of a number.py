#Find factorial of a given number
import math

#take a number as input from user
print("Enter a number for finding its factorial: ")
value = int(input())

#calulate factorial
def fact(k):
    factorial = 1       #Initialize
    if k > 0:
        for i in range(1, k+1):
            factorial = factorial * i
        print("factorial of ",value," is: ",factorial)
    elif k == 0:
        print("factorial of ", value, " is: ", factorial)
    else:
        print("Cannot calculate factorial of a negative number")
fact(value)
