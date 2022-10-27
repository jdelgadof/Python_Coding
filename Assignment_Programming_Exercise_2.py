# Phase 2: 1. Name and greets
name = input("what is your name? ")
print("Hello, " + name + "!")

# Phase 2: 2. Radius of the circle
import math

radius = float(input("Give me the radius? "))
area = math.pi*radius**2
print(f"The area is {area:.2f}")

# Phase 2: 3. Rectangle

length = float(input("give me the length of a rectangle: "))
width = float(input("give me the width of the rectangle: "))
print(f"the perimeter of the rectangle is: {(2*length)+(2*width)}")
print(f"the area of the rectangle is: {length*width}")

# Phase 2: 4. three numbers

num1 = float(input("Please give me one number: "))
num2 = float(input("Please give me a second number: "))
num3 = float(input("Please give me a third number: "))
suma = num1+num2+num3
print(f"The sum of your numbers is: {suma}")
print(f"The product of your numbers is: {num1*num2*num3}")
print(f"The average of your numbers is: {suma/3}")


# Phase 2: 5.
talent = float(input("Please introduce how many talents: "))
pound = float(input("Please introduce how many pounds: "))
lots = float(input("Please introduce how many lots: "))
talent_in_kg= talent*8.512
pound_in_kg= pound*0.4256
lots_in_kg= lots*0.0133
kg_sum=int(lots_in_kg+pound_in_kg+talent_in_kg)
gr_sum=(lots_in_kg+pound_in_kg+talent_in_kg)
print(kg_sum)
print(f"grams {(gr_sum-kg_sum)*1000:.2f}")

# Phase 2: 6. Random numbers
import random

print(f"Randon numer is {random.randint (0,999):03d}")
print(f"Randon numer is {random.randint (1,6)}{random.randint (1,6)}{random.randint (1,6)}{random.randint (1,6)}")