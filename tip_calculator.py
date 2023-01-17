# Tip Calculator:

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $\n"))
tip = float(
    input("What percentage tip would you like ti give? 10, 12 or 15\n"))
people = float(input("How many people to split the bill? \n"))
tip_count = float(tip / 100)

total = ((bill * tip_count) + bill) / people
round_total = round(total, 2)
round_total = "{:.2f}".format(round_total)

print(f"Each person should pay: ${round_total}")
