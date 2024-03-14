from faker import Faker


def random_firstname(fake: Faker = None) -> str:
    if not fake:
        fake: Faker = Faker()

    return fake.unique.first_name()


def random_lastname(fake: Faker = None) -> str:
    if not fake:
        fake: Faker = Faker()

    return fake.unique.last_name()


def random_fullname(fake: Faker = None) -> None:
    if not fake:
        fake: Faker = Faker()

    full_name: str = f"{random_firstname(fake)} {random_lastname(fake)}"

    return full_name


if __name__ == "__main__":
    full_name: str = random_fullname()
    print(f"Random full name:  {full_name}")
