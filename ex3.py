# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

length = len(l)
for j in range(length):
    print_factors(l[j])