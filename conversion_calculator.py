#print("What is your name:")
#name = input()
#print(name)

#print("Hello! What is the temperature:")
vaild = False
while not vaild: 
    try: 
        temp = int(input("Enter the temperature: "))
        vaild = True
    except ValueError:
        print("This is not a number! Please try again.")

valid = False
units = {"c": "Celsius", "f": "Fahrenheit"}
while not valid: 
    
    unit = input("Enter the unit (c for Celsius and f for Farhenhenit):").lower()
    valid = unit in units

print("The number you entered was", temp)
print("The unit you chose was", units[unit])

if unit == "c":
    converted = (temp * 1.8) + 32
    converted_unit = "f"
if unit == "f":
    converted = (temp -32) / 1.8
    converted_unit = "c"

print(f"The temp {temp}{unit} is {round(converted)} in {converted_unit}")