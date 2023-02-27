"""Things i'll be imported."""

def addition(x: int, y: int):
    return x+ y

my_variable: str = "Hello!"

if __name__ == "__main__":
    print("This should only print when running my_functions")
else:
    print("my_functions is being imported")

#would not print the if statement because the name is not main, it is lessons.my_functions

#if you run lessons.my_functions it will print the if statement