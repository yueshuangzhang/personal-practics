# Hello, world!
print("Hello, world!")
# cmd: python hello.py
# ==============================================

# decorator
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello world")

hello()
# ==============================================

# lambda

people = [
    {"name": "Harry",
     "house": "Gryffindor"},
     {"name": "Draco",
     "house": "Slytherin"},
    {"name": "Cho",
     "house": "Ravenclow"}
    
]

# sort people, we can't sort people.sort()
# sort people by house
def f(person):
    return person["house"]

people.sort(key=f)
print(people)

# Same as above, key takes a person, and return the person's name
# sort people by name
people.sort(key=lambda person: person["name"])
print(people)

# ==============================================
import sys

# exceptions: we want to handle the error nicely
try: 
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: invalid input")
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1) # something went wrong: 1

print(f"{x} / {y} = {result}")

# ==============================================

# Class
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False

        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

    
flight = Flight(3)

people = ["Amy", "Bob", "Charlie", "David"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No avilable seat for {person}")


