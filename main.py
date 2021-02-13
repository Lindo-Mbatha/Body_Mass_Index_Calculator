print("Welcome to the Body Mass Index Calculator!")
print("""Underweight: < 18.5
Normal Weight: > 18.5 and < 23
Overweight: > 23 and < 25
Moderately Obese: > 25 and < 30
Severely Obese: > 30""")
height = input("Enter your height in metres: ")
weight = input("Enter your weight in kg: ")

result = int(weight) / (float(height) * float(height))
print(int(result))