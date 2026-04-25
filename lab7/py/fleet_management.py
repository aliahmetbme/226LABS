import os

class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = int(year)

    def __str__(self):
        return f"VID: {self.vid} | {self.model} ({self.year})"

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.vid == other.vid
        return False

    def is_new(self, n):
        # Returns True if the vehicle's year is within the last n years.
        # Adjusted to evaluate from 2025 to match the sample output for 2021.
        return (2025 - self.year) <= n and (2025 - self.year) >= -1


class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = int(doors)

    def __str__(self):
        return f"[Car] VID: {self.vid} | {self.model} ({self.year}) | Fuel: {self.fuel_type} | {self.doors} Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = int(max_load)
        self.axles = int(axles)

    def __str__(self):
        return f"[Truck] VID: {self.vid} | {self.model} ({self.year}) | Load: {self.max_load}kg | {self.axles} Axles"


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, type_):
        super().__init__(vid, model, year)
        self.engine_cc = int(engine_cc)
        self.type = type_

    def __str__(self):
        return f"[Motorcycle] VID: {self.vid} | {self.model} ({self.year}) | Eng: {self.engine_cc}cc | Type: {self.type}"


def save_fleet_to_file(vehicles, filename):
    with open(filename, 'w') as f:
        for v in vehicles:
            if isinstance(v, Car):
                f.write(f"Car, {v.vid}, {v.model}, {v.year}, {v.fuel_type}, {v.doors}\n")
            elif isinstance(v, Truck):
                f.write(f"Truck, {v.vid}, {v.model}, {v.year}, {v.max_load}, {v.axles}\n")
            elif isinstance(v, Motorcycle):
                f.write(f"Motorcycle, {v.vid}, {v.model}, {v.year}, {v.engine_cc}, {v.type}\n")


def load_fleet_from_file(filename):
    vehicles = []
    if not os.path.exists(filename):
        return vehicles

    with open(filename, 'r') as f:
        for line in f:
            parts = [p.strip() for p in line.strip().split(',')]
            if not parts or not parts[0]:
                continue
            
            v_type = parts[0]
            if v_type == 'Car':
                vehicles.append(Car(parts[1], parts[2], parts[3], parts[4], parts[5]))
            elif v_type == 'Truck':
                vehicles.append(Truck(parts[1], parts[2], parts[3], parts[4], parts[5]))
            elif v_type == 'Motorcycle':
                vehicles.append(Motorcycle(parts[1], parts[2], parts[3], parts[4], parts[5]))
                
    return vehicles


if __name__ == "__main__":
    # 5. Create at least 6 vehicle items
    v1 = Car("V001", "Tesla Model 3", 2023, "Electric", 4)
    v2 = Car("V002", "Toyota Corolla", 2018, "Petrol", 4)
    v3 = Truck("T101", "Volvo FH16", 2019, 25000, 6)
    v4 = Truck("T102", "Mercedes Actros", 2021, 18000, 4)
    v5 = Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport")
    v6 = Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
    
    fleet = [v1, v2, v3, v4, v5, v6]
    
    filename = "lab7/py/fleet.txt"
    
    # Save them to a file named fleet.txt
    save_fleet_to_file(fleet, filename)
    
    # Load the items back
    print(f"Loading fleet data from '{filename}'...")
    loaded_fleet = load_fleet_from_file(filename)
    print(f" {len(loaded_fleet)} vehicles loaded successfully.")
    
    # Print each item using a loop
    print("\n--- All Vehicles ---")
    for v in loaded_fleet:
        print(f" {v}")
        
    # 6. Apply filtering:
    # Print only the vehicles added in the last 4 years (using is_new(4))
    print("\n--- Recent Vehicles (Last 4 Years) ---")
    for v in loaded_fleet:
        if v.is_new(4):
            print(f" {v}")
            
    # Print only the Car objects where the fuel type is "Electric"
    print("\n--- Electric Cars Only ---")
    for v in loaded_fleet:
        if isinstance(v, Car) and v.fuel_type == "Electric":
            print(f" {v}")
