# Q12 - Celsius to Fahrenheit using lambda

convert = lambda c: (c * 9 / 5) + 32

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = convert(celsius)

print("Temperature in Fahrenheit =", fahrenheit)
