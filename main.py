numclasses = input("How many classes do you have? ") 
averageclassestime = input("How many minutes do you spend on your classes for homework? ")

numclasses = int(numclasses)
averageclassestime = int(averageclassestime)

print(f"Your average time spent on homework is {round(averageclassestime /numclasses , 1)} minutes per class.")