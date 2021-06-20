from math import pi

print("Hello"[4])

# String
print("123" + "456")

# Integer
print(123 + 456)

# Float
print(format(pi, '.5f'))

# Boolean
True
False

a = input("Type the first number\n")
b = input("Type the second number\n")

if a > b:
  print(a + " is greater than " + b)
elif a < b:
  print(b + " is greater than " + a)
else:
  print(a + " equals " + b)
