def main() -> None:
    print("Hello from explore-uv!")
    greet_user("Alishba")
    result = add_numbers(10, 5)
    print(f"The sum of 10 and 5 is: {result}")

def greet_user(name: str) -> None:
    print(f"Hello, {name}! Welcome to explore-uv.")

def add_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    main()



