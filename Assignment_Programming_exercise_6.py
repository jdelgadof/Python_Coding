
# 6_1
import random


def dice():
    return random.randint(1, 6)


count = 1
while True:
    no = int(dice())
    print(no)
    if no == 6:
        break
    count += 1
print(f' it took {count} attempt to get a 6')

# 6_2


def dice(x):
    return random.randint(1, x+1)


count = 1
side = int(input("How many sides have your dice? "))
while True:
    no = dice(side)
    print(no)
    if no == side:
        break
    count += 1
print(f'it took {count} attempt to get a {side}')

# 6_3


def convert_gas(x):
    gas = x * 3.78
    return gas


gas = int(input('quantity of gasoline in American gallons'))
while gas > 0:
    print(f'That means {convert_gas(gas)} litters')
    gas = int(input('quantity of gasoline in American gallons'))

# 6_4


def sumOfList(list, size):
    if size == 0:
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


list1 = [11, 5, 17, 18, 23]

total = sumOfList(list1, len(list1))
print("Sum of all elements in given list: ", total)


# 6_5

num_list = [1, 2, 3, 44, 45, 46, 47, 80, 89, 100, 0, 2]
even_num = []

print(f"The original numbers are: {num_list} ")


def num_for_list(original):
    for x in original[:]:
        if x % 2 != 0:
            original.remove(x)
    even_num.append(original)
    return print(f"The even numbers are: {even_num}")


num_for_list(num_list)


# 6_6

def pizza(diameter, price):
    # diameter of a round pizza in centimeters
    # price of the pizza in euros
    area = (3.1416*((diameter/2)**2))/100
    unit = price / area
    return unit


d1 = float(input('Please type the cm of the Pizza 1: '))
p1 = float(input('Please type the price in Euros of the Pizza 1: '))
d2 = float(input('Please type the cm of the Pizza 2: '))
p2 = float(input('Please type the price in Euros of the Pizza 2: '))

a1 = pizza(d1, p1)
a2 = pizza(d2, p2)

if a1 < a2:
    print(f'Pizza 1 is the better value for money')
elif a1 > a2:
    print(f'Pizza 2 is the better value for money')
elif a1 == a2:
    print(f'both Pizzas offer the same value for money')
