print("Welcome to compound interest calculator, please follow the instructions below\n")
principal = float(input("How much is your principal?\n"))
rate_raw = float(input("How much is your interest rate?\n"))
rate = rate_raw / 100
compound = float(input("How often does it compound? Example: Monthly = 12, yearly = 1, weekly = 52\n"))
time = float(input("How many years are you investing? \n"))
time_rounded = int(time)
outcome = principal * (1 + (rate / compound)) ** time
rounded_outcome = round(outcome , 2)
print("Your amount after ", time_rounded, "years will be " + str(rounded_outcome))
