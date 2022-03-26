from math import sqrt
# Using formula 3 to get the Fibonacci number
def fibonacci_equ_three(n):
    fibonacci_n = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    return fibonacci_n

# Using formula 4 
def fibonacci_equ_four(n,p):
    fibonacci_p = (((((1+sqrt(5))**p)-((1-sqrt(5)))**p)/(2**p*sqrt(5)))*(((1+sqrt(5))/2)**(n-p)))
    return fibonacci_p
    
# Using formula 5
def fibonacci_equ_five(m):
    n1 = m + 1
    fibonacci_five = ((((1+sqrt(5))**n1)-((1-sqrt(5)))**n1)/(2**n1*sqrt(5)))*((1+sqrt(5))/2)
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

# Fibonacci sequence using third formula
print("Using the third formula:")
for x in range(0, n+1):
   print(fibonacci_equ_three(x))

# # Golden ratio using fourth formula
# print("Using the fourth formula:")
# for (x, y) in [(x,y) for x in range(0, n+1) for y in  range(0, p+1)]:
#     print("Using the fourth formula", fibonacci_equ_four(x,y))

# Golden ration using fifth formula
print("Using the fifth formula:")
for z in range(0, n+1):
    print(fibonacci_equ_five(z))


