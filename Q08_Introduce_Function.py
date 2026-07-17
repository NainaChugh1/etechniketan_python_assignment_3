def introduce(name, age=None):

    if age is None:
        print("My name is", name + ".")
        print("My age is secret.")
    else:
        print("My name is", name + ".")
        print("I am", age, "years old.")


introduce("John", 20)
print()

introduce("John")
