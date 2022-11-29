# Exercise 1
class Elevator:

    def __init__(self, bottom, top, current):
        self.bottom = bottom
        self.top = top
        self.current = current

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"current floor {self.current}")

    def floor_down(self):
        if self.current > 0:
            self.current -= 1
            print(f"current floor {self.current}")

    def go_to_floor(self, floor):
        while self.current < floor:
            h.floor_up()
        while self.current > floor:
            h.floor_down()


h = Elevator(0, 100, 0)
h.go_to_floor(5)
h.go_to_floor(0)


# Exercise 2


class Building:

    def __init__(self, bottom, top, number_elev):
        self.bottom = bottom
        self.top = top
        self.number_elev = number_elev
        self.list_elev = list(range(1, number_elev+1))

    def run_elevator(self, number, destination):
        if number in self.list_elev:
            print(f"Elevator number {number} go to floor {destination}")
            h.go_to_floor(destination)   # Calling the method go_to_floor from the previous class
        else:
            print("Number of elevator does not exist, try again")
# Exercise 3

    def fire_alarm(self):
        print("There is a Fire alarm all the elevators go down")
        h.go_to_floor(0)


B1 = Building(0, 100, 5)  # Bottom floor, Number of floors, Number of elevators
print(f"These are the available elevator in the Building 1 {B1.list_elev}")
B1.run_elevator(int(input("Which Elevator would you like to use? ")),
                int(input("To which floor would you like to go?")))  # Number of elevator to use, Floor os destination
B1.fire_alarm()

# Exercise 4

from Programming_exercise_9 import Car
import random


class Race:
    def __init__(self, name, distance, lista):
        self.name = name
        self.distance = distance
        self.cars_list = lista

    def hour_passes(self):
        for car in self.cars_list:
            car.accel(random.randint(-10, 15))
            car.drive(1.)

    def print_status(self):
        print(self.name + "")
        print("Reg num   Speed   Travelled distance")
        for car in self.cars_list:
            print(f"{car.reg_number:6s}    {car.current_speed:3d}     {car.t_distance}km")

    def race_finished(self):
        for car in self.cars_list:
            if car.t_distance >= self.distance:
                return False
            else:
                return True


car_list = []
for i in range(10):
    car_list.append(Car("ABC-"+str(i+1), random.randint(100, 200)))

race = Race("Grand Demolition Derby", 8000, car_list)
h = 0
while race.race_finished():
    race.hour_passes()
    h += 1
    if h % 10 == 0:
        print(f"After {h} hours")
        race.print_status()
print(f"final result is in {h} hours")
race.print_status()
