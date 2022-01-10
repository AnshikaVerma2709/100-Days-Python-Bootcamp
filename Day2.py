#Day 2
# Tip Calculator

print("Welcome to tip calculator")
bill = float(input("Enter total money: "))
people = int(input("How many people are you in total? "))
tip = int(input("What percentage of tip you would like to give? "))

result = (bill + (bill * (tip/100)))/people
print("Each one should give: ", result, "unit of money.")
