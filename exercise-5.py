# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

#for term in range(51):


    #print(f"term: {term} / number: ")

a = 0
b = 1
num = 51
term = 2
print(f"term: 0 / number: {a}")
print(f"term: 1 / number: {b}")
while(num-2):
    c = a + b
    a,b = b,c
    print(f"term: {term} / number: {c} ")
    num -= 1
    term += 1

