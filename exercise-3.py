# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

age_in_human = int(input("Please enter the dogs age in human years"))
age_in_dog = 0

for num in range(age_in_human):
    if num == 0 or num == 1:
        age_in_dog += 10
    else:
        age_in_dog += 7
    print(age_in_dog)
