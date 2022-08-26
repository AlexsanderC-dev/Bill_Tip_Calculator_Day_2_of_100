#English  version
# Simple calculator of total restaurant bill amount divided by a group.
# The result will be rounded to 2 decimal places.
print("Welcome to the tip calculator!\n")
bill = float(input("What is the total amount of the Bill? $ "))
tip = int(input("What percentage of the tip should you pay? 5, 10, 12, or 15? "))
people = int(input("How many people will split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
