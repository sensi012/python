#############
# shopping cart program
#################

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item: (q to exit) ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("--------Your Cart ---------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")


# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter the food item: (Enter q to exit)")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of the {food} item: $"))
#         foods.append(food)
#         prices.append(price)

# print("--------Your Cart ---------")

# for food, price in zip(foods, prices):
#     print (f"{food} ${price}")

# for price in prices:
#     total += price

# print(f"your total is ${total}")

