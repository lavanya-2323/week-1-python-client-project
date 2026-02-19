# Week-1 Client Project
# Basic Data Processing Script - Average Temperature Calculator

print("===== Average Temperature Calculator =====")

n = int(input("Enter number of days: "))

temperatures = []

for i in range(n):
    temp = float(input(f"Enter temperature for day {i+1}: "))
    temperatures.append(temp)

total = sum(temperatures)
average = total / n

print("\n----- Results -----")
print("Temperature values:", temperatures)
print("Total Temperature:", total)
print("Average Temperature:", round(average, 2), "°C")
