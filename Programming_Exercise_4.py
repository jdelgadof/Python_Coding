# 4.1 All number divisible by three

n = 1
while n < 1000:
    if n % 3 == 0:
        print(n)
    n = n + 1

# 4.2 Inches to cm

n_1 = int(input("Please type inches, if you want to stop type a negative number "))
while n_1 >= 0:
    n_1 = int(input("Please type inches, if you want to stop type a negative number "))
    print(f"{n_1} means {n_1 * 2.54} cm")
print("Bye!")

# 4.3 Smallest and largest number

n_2 = 0
mi = 9999999999
maxx = -9999999999

while n_2 != "":
    n_2 = input(f"Please type a number: ")
    if n_2 == "":
        break
    n_2 = int(n_2)
    if n_2 < mi:
        mi = n_2
    if n_2 > maxx:
        maxx = n_2
print(F"The smallest number is {mi} and the largest is {maxx}")

# 4.4 Guess a number
import random

hide = random.randint(1, 10)
guess = int(input("try to guess a number between 1 and 10: "))
while hide != guess:
    if guess > hide:
        print("Your guess is too high")
    if guess < hide:
        print("Your guess is too low")
    guess = int(input("try again: "))
print("Correct!")

# 4.5 Credentials

User = "python"
pasw = "rules"
attempt = 1

while attempt < 5:
    u_1 = input(f"User: ")
    p_1 = input(f"Password: ")
    if u_1 != User or p_1 != pasw:
        print(f"Access denied, try again")
        attempt = attempt + 1
    if u_1 == User and p_1 == pasw:
        print(f"Welcome!")
        break

# 4.6 Value of Pi

N = int(input("Generate random points inside square: "))
n_5 = 0
while n_5 <= N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x ** 2) + (y ** 2) <= 1:
        n_5 = n_5 + 1

print(f"The approximation for the value of pi is {4 * n_5 / N}")
