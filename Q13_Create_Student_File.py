# Q13 - Create student.txt using exception handling

try:
    file = open("student.txt", "x")

    file.write("Python is easy to learn.\n")
    file.write("File handling is important.\n")
    file.write("Practice makes perfect.")

    file.close()

    print("File created successfully.")

except FileExistsError:
    print("File already exists.")

except Exception as e:
    print("Error:", e)
