# Parent class
class Device:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"{self.brand} device is powering on...")

# Child class (Inheritance + Encapsulation)
class Smartphone(Device):
    def __init__(self, brand, model, storage):
        super().__init__(brand)     # Call parent constructor
        self.model = model
        self.__storage = storage    # Encapsulation (private attribute)

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")

    def get_storage(self):  # Controlled access
        return f"Storage: {self.__storage}GB"

# Create objects
phone1 = Smartphone("Apple", "iPhone 14", 128)
phone2 = Smartphone("Samsung", "Galaxy S23", 256)

phone1.power_on()
phone1.call("+123456789")
print(phone1.get_storage())

phone2.power_on()
phone2.call("+987654321")
print(phone2.get_storage())
