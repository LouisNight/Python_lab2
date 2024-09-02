import math

name = "Louis Night"
age = 25
height = 173    # height in cm
favorite_color = "purple"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f"My name is {name} and I am {age} years old. My favorite color is {favorite_color} and I am {height} cm tall.")
formatted_text = "My name is %s and I am %d years old." % (name, age)
print(formatted_text)

print(f"""
Name: {name}
Age: {age}
Height: %d
Favorite color: %s
""" % (height, favorite_color))

#            print(f"""      **This results in an IndentationError: unexpected indent**
#          Name: {name}
#       Age: {age}
#     Height: %d
# Favorite color: %s
#  """ % (height, favorite_color))

circle_area = math.pi * 5**2
print(round(circle_area, 1))

print(math.sqrt(age))

print(math.sin(height))
print(math.cos(height))

age_sum = age + 5
height_difference = 173 - 4
age_height_product = age * height
height_quotient = height / 2
age_remainder = age % 3
age_power = age**2

print(age_sum, height_difference, age_height_product, height_quotient, age_remainder, age_power)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

fahrenheit = float(input("Please enter a temperature in fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)

print(f"{fahrenheit}\u00b0 Fahrenheit is equal to {celsius: .2f}\u00b0 Celsius")
