# convert kg into grams

weight = float(input("Enter the weight: "))
unit = input("Enter the unit (kg or g): ")

if unit == "kg":
    weight = weight * 1000
    print(f"{round(weight, 2)} kgs is equal to {round(weight, 2)} grams")
    
elif unit == "g":
    weight = weight / 1000
    print(f"{round(weight, 2)} grams is equal to {round(weight, 2)} kgs")

else:
    print("Invalid input")
