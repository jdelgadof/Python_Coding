# 7_1

Winter = [12, 1, 2]
Spring = [3, 4, 5]
Summer = [6, 7, 8]
Autumn = [9, 10, 11]
month_list = (Winter, Spring, Summer, Autumn)
month = int(input("Please enter the number of a month: "))

if month in month_list[0]:
    season = "winter"
elif month in month_list[1]:
    season = "Spring"
elif month in month_list[2]:
    season = "Summer"
elif month in month_list[3]:
    season = "Autumn"
else:
    print("That is not a month!")

print(f"The season is {season}")

# 7_2

name = input("Enter a name: ")
print("New name!")
lista = set()
while name != "":
    lista.add(name)
    name = input("Enter a name: ")
    if name in lista:
        print("existing name")
    elif name == "":
        break
    else:
        print("New name!")
        lista.add(name)

for x in set(lista):
    print(x)

# 7_3
