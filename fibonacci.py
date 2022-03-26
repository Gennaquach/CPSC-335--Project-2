def fibonacci(n):
         
    # If n = 0 returns 0
    if n == 0:
        return 0
       
    # If n = 1 returns 1
    elif n == 1:
        return 1

    # If n >= 2 returns the term of sequence
    else:
        term = fibonacci(n-1) + fibonacci(n-2)
        return term
# Input for 15th term
input_n = input("Please enter a positive integer n to find the fibonacci term for: ")

if input_n.strip().isdigit() and int(input_n) >= 0:
    n = int(input_n)
    print("The n value entered is:", n, "\nThe fibonacci term for that is:", fibonacci(n))

else:
    print("That is not a valid positive integer, please try again.")

# OUTPUT:
# Please enter a positive integer n to find the fibonacci term for: 15
# The n value entered is: 15 
# The fibonacci term for that is: 610
