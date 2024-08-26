import json
import os

filePath = 'db.json'

def clearTerminal():
    # Clear command for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear command for macOS and Linux
    else:
        os.system('clear')

def loadCars():
    try:
        with open(filePath, 'r') as file:
            cars = json.load(file)
        return cars
    except FileNotFoundError:
        print(f"Error: The file '{filePath}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{filePath}' contains invalid JSON.")
        return []
    
def saveCars(cars):
    with open(filePath, 'w') as file:
        json.dump(cars, file, indent=4)
    print(f"Data has been saved to {filePath}.")

def menu():
    print("choose:")
    print("1 - add a car")
    print("2 - delete a car")
    print("3 - show all cars")
    print("4 - search cars by color")
    print("5 - save changes")
    print("x - Exit")
    choice = (input("Your choice please: "))
    return choice

def execute(choice, cars):
        if choice == "1": addCar(cars)
        if choice == "2": deleteCar(cars)
        if choice == "3": showAll(cars)
        if choice == "4": searchCarByColor(cars)
        if choice == "5": saveCars(cars)      
        if choice == "x": exit()      


def searchCarByColor(cars):
    color = input("which car color you want to search? ").lower()
    for car in cars:
        if car['color'].lower() == color:
            print(car)
    print(color)

def addCar(cars):
    brand = input("What is the brand? ")
    model = input("What is the model? ")
    color = input("What is the color? ")
    cars.append({"brand": brand, "model": model, "color": color})
    clearTerminal()

def deleteCar(cars):
    delIndex = input("what is the car's list number you wish to erase? ")
    del cars[int(delIndex)]
    clearTerminal()

def showAll(cars):
    for index in range(len(cars)):
        car = cars[index]
        print(f"Index: {index}, Brand: {car['brand']}, Model: {car['model']}, Color: {car['color']}")

def main():
    cars = loadCars()

    while True:
        choice = menu()
        execute(choice, cars)
  
if __name__ == "__main__":
    main()