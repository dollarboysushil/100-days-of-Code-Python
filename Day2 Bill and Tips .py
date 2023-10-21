print("Welcome to tip calculator")
bill = float(input ("What was the total bill? "))
split = int(input("How many people to split the bill? "))
percent = int(input ("What percentage tip would you like to give?(10, 12 or 15) "))

total_cost = bill + percent/100 ;
cost = round(total_cost/ split , 2)

print(f"Each Person Should Pay: ${cost}")