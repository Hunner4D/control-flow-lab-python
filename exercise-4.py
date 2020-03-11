# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


side_a = input("Please enter side a of the triangle: ")
side_b = input("Please enter side b of the triangle: ")
side_c = input("Please enter side c of the triangle: ")

if side_a == side_b and side_b == side_c:
    print("The triangle is an equilateral triangle, all sides are equal")
elif side_a != side_b and side_b != side_c:
    print("The triangle is an scalene triangle, all three sides are unequal")
elif (side_a == side_b and (side_a != side_c and side_b != side_c)) or (side_b == side_c and (side_b != side_a and side_c != side_a)) or (side_c == side_a and (side_c != side_b and side_a != side_b)):
    print("The triangle is isoceles, two side lengths are equal")