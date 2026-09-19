# simple interest calculator

principal = 0.0
rate = 0.0
time = 0.0

while True:
    principal= float(input("Enter the principal amount: "))
    if principal < 0:
        print("Enter the principal amount can't be less than zero")
    else:
        break
while True:
    rate= float(input("Enter the rate of interest: "))
    if rate < 0:
        rate= float(input("Enter the rate of interest can't be less than zero: "))
    else:
        break
while True:
    time= float(input("Enter the time in years: "))
    if time < 0:
        time= float(input("Enter the time in years can't be less than zero: "))
    else:
        break

print(f"simple interest is ${round((principal * rate * time / 100), 2)}")