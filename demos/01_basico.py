# Slide 3 — "Três linhas para gerar uma pessoa inteira"
# Rode a partir da raiz:  python demos/01_basico.py
import sys

from faker import Faker

sys.stdout.reconfigure(encoding="utf-8")  # acentos no terminal do Windows

Faker.seed(42)
fake = Faker("pt_BR")

print("fake.name()         ->", repr(fake.name()))          # 'Brenda Alves'
print("fake.cpf()          ->", repr(fake.cpf()))           # '721.175.500-88'
print("fake.email()        ->", repr(fake.email()))         # 'mirellapereira@example.org'
print("fake.phone_number() ->", repr(fake.phone_number()))  # '+55 82 8637-9402'
