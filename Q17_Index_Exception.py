# Q17 - Handle IndexError

numbers = [7, 4, 0, -2, 3]

print("List:", numbers)

try:
    index = int(input("Enter index: "))
    print("Value =", numbers[index])

except IndexError:
    print("Invalid index!")

except ValueError:
    print("Please enter a valid number.")
