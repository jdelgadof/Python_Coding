
# Phase 3.1 length of a zander
length = float(input("What is the length of your zander in centimeters? "))
zander = 42
if length <= 42:
    print(f"Please release back the fish. Your zander is {42 - length:.0f} cm short of the size limit.")
else:
    print(f"Congrats, you can keep this Zander")

# Phase 3.2 Cabin of the ship
cabin = input("What type of cabin do you have? ")
if (cabin == "LUX") or (cabin == "Lux") or (cabin == "lux"):
    print(f"Upper-deck cabin with a balcony")
elif (cabin == "A") or (cabin == "a"):
    print(f"Above the car deck, equipped with a window")
elif (cabin == "B") or (cabin == "b"):
    print(f"Windowless cabin above the car deck")
elif (cabin == "C") or (cabin == "c"):
    print(f"Windowless cabin below the car deck")
else:
    print(f"Invalid cabin class")

# Phase 3.3 Hb and gender

gender = input("What is your gender? ")
hb = float(input("What is your hemoglobin value? "))
gender = gender.lower()
    # normal_male_min = 134
    # normal_male_max = 167
    # normal_female_min = 117
    # normal_female_max = 155

if (gender == "Male") or (gender == "male") or (gender == "MALE"):
    if hb > 167:
        print(f"the hemoglobin value is high, please contact your doctor. ")
    elif hb < 134:
        print(f"the hemoglobin value is low, please contact your doctor. ")
    else:
        print(f"the hemoglobin value is normal.")

if (gender == "Female") or (gender == "female") or (gender == "FEMALE"):
    if hb > 155:
        print(f"the hemoglobin value is high, please contact your doctor. ")
    elif hb < 117:
        print(f"the hemoglobin value is low, please contact your doctor. ")
    else:
        print(f"the hemoglobin value is normal.")

else:
    print(f"Please try again your gender, check about typo or grammar. The values of the hb should be a positive value")

# Leap year

year = int(input("Please type in a year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("That year is a leap year")
    else:
        print("That year is not a leap year")
else:
    if year % 4 == 0:
        print("That year is a leap year")
    else:
        print("That year is not a leap year")

