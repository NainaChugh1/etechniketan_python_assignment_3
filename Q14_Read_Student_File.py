# Q14 - Read file content

file = open("student.txt", "r")

print("Complete Content:\n")
print(file.read())

file.close()

print("\nReading Line by Line:\n")

file = open("student.txt", "r")

line_number = 1

for line in file:
    print("Line", line_number, ":", line.strip())
    line_number += 1

file.close()
