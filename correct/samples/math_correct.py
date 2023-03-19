def greet(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

def is_even(num):
    return num % 2 == 0

def main():
    greet("Alice")
    result = add_numbers(2, 3)
    print(f"2 + 3 = {result}")
    num = 7
    if is_even(num):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

if __name__ == "__main__":
    main()
