# Base Class
class Smartphone:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self._battery_percentage = 100  # Private attribute
        self.battery_capacity = battery_capacity
    
    # Method to display phone details
    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery: {self._battery_percentage}% ({self.battery_capacity}mAh)")
    
    # Getter for battery percentage
    def get_battery_percentage(self):
        return self._battery_percentage
    
    # Setter for battery percentage
    def charge_battery(self, amount):
        if 0 <= self._battery_percentage + amount <= 100:
            self._battery_percentage += amount
        else:
            self._battery_percentage = 100
        print(f"Battery charged to {self._battery_percentage}%")
    
    # Method to use battery
    def use_battery(self, usage):
        if self._battery_percentage - usage < 0:
            self._battery_percentage = 0
            print("Battery drained! Please charge your phone.")
        else:
            self._battery_percentage -= usage
            print(f"Battery now at {self._battery_percentage}%")

# Derived Class: AndroidPhone
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, battery_capacity, android_version):
        super().__init__(brand, model, battery_capacity)
        self.android_version = android_version

    # Overridden method to display details with Android version
    def display_details(self):
        super().display_details()
        print(f"Android Version: {self.android_version}")

# Derived Class: iPhone
class iPhone(Smartphone):
    def __init__(self, brand, model, battery_capacity, ios_version):
        super().__init__(brand, model, battery_capacity)
        self.ios_version = ios_version
    
    # Overridden method to display details with iOS version
    def display_details(self):
        super().display_details()
        print(f"iOS Version: {self.ios_version}")

# Creating objects
android_phone = AndroidPhone("Samsung", "Galaxy S21", 4000, "11")
iphone = iPhone("Apple", "iPhone 13", 3240, "15.2")

# Demonstrating polymorphism
print("== Android Phone Details ==")
android_phone.display_details()
android_phone.use_battery(30)
android_phone.charge_battery(20)

print("\n== iPhone Details ==")
iphone.display_details()
iphone.use_battery(50)
iphone.charge_battery(60)
