
# 5.1 Roll dices
import random
dice = int(input(f"Please enter a number of dice? "))
attempt = 0
for number in range(1,dice+1):
    n = random.randint(1,6)
    attempt += n
    print(f"{n}")

print(f"your number is {attempt}")

# 5.2 Five greatest numbers

numbers = []
while True:
    user_input = input("Please type in an integer, leave empty to exit: ")
    if len(user_input) == 0:
        break
    numbers.append(int(user_input))

ordered = sorted(numbers, reverse=True)
five = ordered[:5]
print(five)


# 5.3 Prime number

numero = int(input("Number: "))
serPrimo = True
for n in range(2,numero):
    if numero % n == 0:
        serPrimo = False
        break
if serPrimo:
    print(numero,"It is a prime number")
else:
    print(numero,"It is not a prime number")

# 5.4 Five Cities

c_lst = []
for element in range(1,6):
    city = input("Write a city:")
    c_lst.append(city)
for cities in c_lst:
    print(cities)


