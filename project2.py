"""
Vehicle Rental Management System
"""

class Vehicle:
    def __init__(self, brand, vehicle_type, rent_per_day):
        self.brand = brand
        self._vehicle_type = vehicle_type
        self.rent_per_day = rent_per_day

    @property
    def rent_per_day(self):
        return self.__rent_per_day

    @rent_per_day.setter
    def rent_per_day(self, amount):
        try:
            if amount > 0:
                self.__rent_per_day = amount
            else:
                print("Rent must be greater than zero!")
        except TypeError:
            print("Rent must be a number!")

    def calculate_rent(self, days):
        if days > 0:
            return self.rent_per_day * days
        else:
            print("Days must be greater than zero!")
            return None

    def display_details(self):
        print("Brand name:", self.brand)
        print("Vehicle type:", self._vehicle_type)
        print("Daily rental price:", self.rent_per_day)

vehicle1 = Vehicle("Toyota", "Car", 3000)
vehicle2 = Vehicle("Honda", "Scooter", 800)

vehicle1.display_details()
print("Total rent for 4 days:", vehicle1.calculate_rent(4))

print()

vehicle2.display_details()
print("Total rent for 3 days:", vehicle2.calculate_rent(3))

with open("vehicles.txt", "w") as file:
    file.write("Vehicle Rental Management System\n\n")

    file.write(f"Brand: {vehicle1.brand}\n")
    file.write(f"Type: {vehicle1._vehicle_type}\n")
    file.write(f"Daily Rent: Rs. {vehicle1.rent_per_day}\n\n")

    file.write(f"Brand: {vehicle2.brand}\n")
    file.write(f"Type: {vehicle2._vehicle_type}\n")
    file.write(f"Daily Rent: Rs. {vehicle2.rent_per_day}\n")

print("\nVehicle details saved successfully!")

with open("vehicles.txt", "r") as file:
    content = file.read()

print("\n--- Saved Vehicle Details ---")
print(content)
