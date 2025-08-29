# 🐍 Python OOP Assignment  

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python, including **classes, inheritance, encapsulation, and polymorphism**.  

---

## 📌 Assignment 1: Design Your Own Class 🏗️  

We created a `Smartphone` class (child class) that inherits from a `Device` class (parent class).  

### Features:
- **Attributes:** brand, model, storage  
- **Methods:** `power_on()`, `call(number)`, `get_storage()`  
- **Encapsulation:** Storage attribute is private (`__storage`).  
- **Inheritance:** Smartphone inherits from Device.  

### Example Usage:
```python
phone1 = Smartphone("Apple", "iPhone 14", 128)
phone1.power_on()
phone1.call("+123456789")
print(phone1.get_storage())
