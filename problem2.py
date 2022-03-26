# Using exhaustive search algorithm 
def largest_sum(V,n):
 
    b = 0
    e = 1
  
    for i in range(0, n-1):
        for j in range (i+1, n):
            if sum(V[i:j]) > sum(V[b:e]):
                b = i
                e = j 
    return V[b:e]
    
#Sample inputs 
a = [-3, -5, 5, -1, -3, 1, 5, -6]
print("Largest sum subarray for:", a, "is:", largest_sum(a,len(a)))
b = [10, 2, -5, 1, 9, 0, -4, 2, -2]
print("Largest sum subarray for:", b, "is:", largest_sum(b,len(b)))
c = [-7, 1, 8, 2, -3, 1]
print("Largest sum subarray for:", c, "is:", largest_sum(c,len(c)))
d = [9, 7, 2, 16, -22, 11]
print("Largest sum subarray for:", d, "is:", largest_sum(d,len(d)))
e = [6,1, 9, -33, 7, 2, 9, 1, -3, 8, -2, 9, 12, -4]
print("Largest sum subarray for:", e, "is:", largest_sum(e,len(e)))

# OUTPUTS:
# Largest sum subarray for: [-3, -5, 5, -1, -3, 1, 5, -6] is: [5, -1, -3, 1, 5]
# Largest sum subarray for: [10, 2, -5, 1, 9, 0, -4, 2, -2] is: [10, 2, -5, 1, 9]
# Largest sum subarray for: [-7, 1, 8, 2, -3, 1] is: [1, 8, 2]
# Largest sum subarray for: [9, 7, 2, 16, -22, 11] is: [9, 7, 2, 16]
# Largest sum subarray for: [6, 1, 9, -33, 7, 2, 9, 1, -3, 8, -2, 9, 12, -4] is: [7, 2, 9, 1, -3, 8, -2, 9, 12]
