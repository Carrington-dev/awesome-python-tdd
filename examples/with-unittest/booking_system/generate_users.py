from pprint import pprint
from faker import Faker
import random

fake = Faker()

def fake_sa_id():
    return fake.bothify("##########08#")  # SA IDs are 13 digits

def generate_users(n=20):
    users = {

    }
    for i in range(1, n + 1):
        id = fake_sa_id()
        users[id] = ({
            "id": id,
            "full_name": fake.name(),
            "age": random.randint(18, 60),
        })
    return users

users = generate_users()

pprint(users)
