#This is my first real python program. It's not much, but it is fun!

print("This program is designed to help you caclulate the amount you should tip.")

meal_cost = float(input("Please enter the amount on your bill with tax: "))
tip = 15.0 / 100

total_with_tip = meal_cost + (meal_cost * tip)

print("Tip: " + str(round((meal_cost * tip),2)))
print("Total w/Tip: " + str(round((total_with_tip),2)))
