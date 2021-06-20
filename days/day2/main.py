print("Welcome to the tip calculator") 

bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
num_of_people = float(input("How many people to split the bill? "))

tip = (tip + 100) / 100
bill *= tip
bill /= num_of_people

print(f"Each person should pay: ${format(bill, '.2f')}")
