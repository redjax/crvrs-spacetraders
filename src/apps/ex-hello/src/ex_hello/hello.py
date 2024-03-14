from ex_randomname import random_firstname, random_lastname, random_fullname


def say_hello(name: str = None) -> str:
    if not name:
        name: str = "world"

    print(f"Hello, {name}!")


if __name__ == "__main__":
    first_name = random_firstname()
    print(f"Random first name: {first_name}")
    last_name = random_lastname()
    print(f"Random last name: {last_name}")
    full_name = random_fullname()
    print(f"Random full name: {full_name}")

    say_hello(full_name)
