
import random


class Car:

    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.t_distance = 0

    def accel(self, acceleration):
        self.current_speed = min(max(self.current_speed+acceleration, 0), self.max_speed)

    def drive(self, time):
        self.t_distance += self.current_speed * time


car_1 = Car("ABC-123", 142)
print(f"Registration number: {car_1.reg_number}, maximum speed is: {car_1.max_speed}\n"
      f"The current speed of this car is: {car_1.current_speed} and has travelled: {car_1.t_distance}")
"""
car_1.accel(30)
print(f"The current speed is: {car_1.current_speed}")
car_1.accel(70)
print(f"The current speed is: {car_1.current_speed}")
car_1.accel(50)
print(f"The current speed is: {car_1.current_speed}")
car_1.accel(-200)
print(f"The current speed is: {car_1.current_speed}")

car_1.accel(60)
car_1.drive(1.5)
print(f"The distance travelled is {car_1.t_distance}")
"""
List_cars = []
for i in range(10):
    List_cars.append(Car("ABC-"+str(i+1), random.randint(100, 200)))

TravelMax = 0
while TravelMax < 10000:
    for racingcar in List_cars:
        racingcar.accel(random.randint(-10, 15))
        racingcar.drive(1)
        TravelMax = max(racingcar.t_distance, TravelMax)

for racingcar in List_cars:
    print(f"{racingcar.reg_number:6s}: {racingcar.max_speed}km/h, Travelled {racingcar.t_distance} km"
          f" The winner was able to travel {TravelMax}")
