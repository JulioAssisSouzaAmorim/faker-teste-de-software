# Slide 7 — "Aleatório, mas repetível: seed e unique"
# Rode a partir da raiz:  python demos/04_seed_e_unique.py
import sys

from faker import Faker
from faker.exceptions import UniquenessException

sys.stdout.reconfigure(encoding="utf-8")

print("Seed: mesma semente, mesmos dados")
Faker.seed(42)
print("  Faker.seed(42); Faker('pt_BR').name() ->", repr(Faker("pt_BR").name()))
Faker.seed(42)
print("  Faker.seed(42); Faker('pt_BR').name() ->", repr(Faker("pt_BR").name()))

print()
print("Unique: nunca repete um valor")
fake = Faker("pt_BR")
fake.seed_instance(2026)  # mesma seed do tests/conftest.py
print("  fake.unique.email()   ->", repr(fake.unique.email()))
print("  fake.unique.boolean() ->", fake.unique.boolean())
print("  fake.unique.boolean() ->", fake.unique.boolean())
try:
    fake.unique.boolean()
except UniquenessException as erro:
    print("  fake.unique.boolean() -> UniquenessException:", erro)
