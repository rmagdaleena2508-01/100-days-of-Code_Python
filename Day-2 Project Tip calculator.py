print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? Rs."))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# 1. Calculate the total bill multiplier (e.g., 10% tip is 1.10)
tip_as_percentage = tip / 100
total_multiplier = 1 + tip_as_percentage

# 2. Calculate the total amount with tip
total_bill_with_tip = bill * total_multiplier

# 3. Calculate the split amount and round to two decimal places
pay_split = round(total_bill_with_tip / people, 2)

print(f"Each person should pay: Rs. {pay_split}")
