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
    fibonacci_five = ((((1+sqrt(5))**m)-((1-sqrt(5)))**m)/(2**m*sqrt(5)))*((1+sqrt(5))/2)
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

    input_n = input("\nPlease enter a positive integer and non-floating point, n to find the fibonacci term for: ")
    if input_n.strip().isdigit() and int(input_n) >= 0:
        n = int(input_n)
    
        print("The n value entered is:", n)
        break

    else:
        print("That is not a valid integer, please try again.")

# Fibonacci sequence using third formula
# print("\nUsing the third formula:")
# for x in range(0, n+1):
#    print(fibonacci_equ_three(x))

# # Golden ratio using fourth formula
print("\nUsing the fourth formula:")
# for x in range(0, p+1): 
#     print(fibonacci_equ_four(n,x), end=", ")
x = 0
y = 0
while x < n+1 and y < p+1:
     print(fibonacci_equ_four(x,y), end=" ")
     x += 1
     y += 1


print("\n")
# Golden ration using fifth formula
print("\nUsing the fifth formula:")
for i in range(0, n+1):
    print(fibonacci_equ_five(i), end=" ")


