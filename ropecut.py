# Q1

# def max_product(n):
#     if n == 1:
#         return 0
# #this function will call the helper function and will return the maximum product
#     return findmax(1,n-1)

# #helper function to calculate maximum product
# def findmax(alpha,val):
#     if val ==1:
#         return 1
    
#     max_product=alpha * val
# #recursive calls to calculate all possible cuts and max function will return the maximum of these values
#     max_product = max(max_product,findmax(alpha+1,val-1))
#     return max_product

# rope_length = int(input("enter rope length to calculate "))
# max_prod = max_product(rope_length)
# print("Maximum product is ",max_prod ,"for length ",rope_length)






# Q2
# calculated is used to store memorization table
calculated = [[None for _ in range(100)] for _ in range(100)]
def max_product(n):
    if n == 1:
        return 1
# this function will call the helper function and will return the maximum product
    return findmax(1, n - 1, calculated)


# helper function to calculate maximum product
def findmax(alpha, val, calculated):
    if val == 1:
       return 1
    
# check if the values are already calculated then they wont be calculated again 
    if calculated[alpha][val] is not None or calculated[alpha][val] is not None:
        return calculated[alpha][val]
    
# else they are stored in the table
    max_prod = alpha * val
    calculated[alpha] [val] = max_prod

# recursive calls to calculate all possible cuts and max function will return the maximum of these values
    max_prod = max(max_prod, findmax(alpha + 1, val - 1, calculated))
    return max_prod

rope_length = int(input("enter rope length to calculate "))
max_prod = max_product(rope_length)

print("Maximum product is ",max_prod ,"for input length ",rope_length)

# Displaying the memoization table
print("Memoization Table:")
for alpha in range(1, rope_length + 1):
    for val in range(1, rope_length + 1):
        if calculated[alpha][val] is not None:
            print(f"({alpha}, {val}):", calculated[alpha][val])






# # Q4
# def max_product(n, count):
#     if n == 1:
#         return 0
#     count[n] += 1  # Increment the count for the current subproblem
#     return findmax(1, n-1, count)

# def findmax(alpha, val, count):
#     if val == 1:
#        return 1
#     count[val] += 1  # Increment the count for the current subproblem

#     max_product = alpha * val
#     max_product = max(max_product, findmax(alpha+1, val-1, count))
#     return max_product

# rope_length = int(input("enter rope length to calculate "))
# count = [0] * (rope_length + 1)
# max_prod = max_product(rope_length, count)

# print("Maximum product is", max_prod, "for length", rope_length)

# # Display the table of counts
# print("Subproblem Counts:")
# for i in range(1, rope_length + 1):
#     print("Length", i, ":", count[i])






#Q5
#     # to calculate the running time complexity of the algoritham
#     running_time = sum(count)

# print("Running time complexity:", running_time)