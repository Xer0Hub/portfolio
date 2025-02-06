print("Welcome to the tip calculator!")
bill_total = int(input("Please enter your total bill "))
tip_select = int(input("How much would you like to tip? Answer in percentage, example: 15, 20, 25 "))
tip_percentage = tip_select / 100
bill_final = bill_total * tip_percentage + bill_total
split_select = int(input("This bill is for how many people? "))

payment_amount = round(bill_final / split_select, 2)
print(f"You and whoever you're splitting with should pay ${payment_amount}, this includes the tip. ")

