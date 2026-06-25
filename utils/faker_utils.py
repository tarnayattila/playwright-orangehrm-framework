from faker import Faker

fake = Faker()


def generate_employee():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "username": fake.user_name(),
        "password": fake.password(length=10),
    }