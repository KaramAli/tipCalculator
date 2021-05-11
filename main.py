print("Welcome to the tip calculator.")
total_bill = int(input("What was the total bill? "))
number_of_people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? "))
split = (total_bill + ((total_bill/100)*tip_percentage))/number_of_people
print(f"Each person should pay: ${split}")
