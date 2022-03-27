from math import sqrt

# Using formula 3 to get the Fibonacci number
def fibonacci_equ_three(n):
    fibonacci_n = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    return fibonacci_n

# Using formula 4 
def fibonacci_equ_four(n,p):
    fibonacci_p = fibonacci_equ_three(p)*(((1+sqrt(5))/2)**(n-p))
    return fibonacci_p
    
# Using formula 5
def fibonacci_equ_five(n):
    fibonacci_five = fibonacci_equ_three(n) *((1+sqrt(5))/2)
    return fibonacci_five

# Ask user to enter 'p' until it is a valid positive integer and non floating point. 
while True:
    input_p = input("Please enter a positive integer and non-floating point, p to find the fibonacci term for: ")
    if input_p.strip().isdigit() and int(input_p) >= 0:
        p = int(input_p)
        print("The p value entered is:", p)
        break

    else:
        print("That is not a valid integer, please try again.")

# Ask user to enter 'n' until it is a valid positive integer and non floating point. 
while True:
    input_n = input("Please enter a positive integer and non-floating point, n to find the fibonacci term for: ")
    if input_n.strip().isdigit() and int(input_n) >= 0:
        n = int(input_n)
    
        print("The n value entered is:", n)
        break

    else:
        print("That is not a valid integer, please try again.")

# Golden ratio using fourth formula
print("Using the fourth formula:")
for i in range(0, n+1):
     print(fibonacci_equ_four(i,p), end=", ")

print("\n")

# Golden ration using fifth formula
print("Using the fifth formula:")
for i in range(0, n+1):
    print(fibonacci_equ_five(i), end=", ")