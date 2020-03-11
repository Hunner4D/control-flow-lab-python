# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Please enter the requested month (Jan - Dec) ")
day = int(input("Please enter the requested day "))

winter = ["Dec", "Jan", "Feb", "Mar"]
spring = ["Mar", "Apr", "May", "Jun"]
summer = ["Jun", "Jul", "Aug", "Sep"]
fall = ["Sep", "Oct", "Nov", "Dec"]

if month in winter:
    if month == "Dec" and day >= 21:
        print("The season is winter")
    if month == "Jan" or month == "Feb":
        print("The season is winter")
    if month == "Mar" and day <= 19:
        print("The season is winter")
if month in spring:
    if month == "Mar" and day >= 20:
        print("The season is spring")
    if month == "Apr" or month == "May":
        print("The season is spring")
    if month == "Jun" and day <= 20:
        print("The season is spring")
if month in summer:
    if month == "Jun" and day >= 21:
        print("The season is summer")
    if month == "Jul" or month == "Aug":
        print("The season is summer")
    if month == "Sep" and day <= 21:
        print("The season is summer")
if month in fall:
    if month == "Sep" and day >= 22:
        print("The season is fall")
    if month == "Oct" or month == "Nov":
        print("The season is fall")
    if month == "Dec" and day <= 20:
        print("The season is fall")



# where_my_things_are = {
#     'pokemon' : 'pokeball',
#     'badges' : 'pokedex',
#     'money' : 'chest',
#     'tatertots' : 'pocket'
# }

# for key, val in where_my_things_are.items():
#     print( f"My {key} is stored in my {val}" )