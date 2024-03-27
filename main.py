print ("Welcome to tip calculator!")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage would you like to tip? ")
people = input("How many people to split the bill? ")
totalbill = (float(total_bill) / int(people))

final = totalbill + (float(tip_percentage) * 0.01 * float(totalbill))

print(f"Each person should pay: ${round(final , 2)}")