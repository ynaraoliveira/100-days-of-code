print("Let's calculate your Body Mass Index")

weight = float(input("Enter your weight in kilos: "))
height = float(input("Enter your height in meters: "))

bmi = weight / height ** 2
print(int(bmi))