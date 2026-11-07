# Slide 6 — "O mesmo código, dados de 110 lugares diferentes"
# Rode a partir da raiz:  python demos/03_locales.py
import sys

from faker import Faker

sys.stdout.reconfigure(encoding="utf-8")  # necessário para o nome em japonês

for locale in ["pt_BR", "en_US", "ja_JP"]:
    fake = Faker(locale)
    fake.seed_instance(42)
    print(f'Faker("{locale}").name() -> {fake.name()}')

print()
fake = Faker(["pt_BR", "en_US"])
print('fake = Faker(["pt_BR", "en_US"])')
print("fake.name()          ->", fake.name(), " # de um dos dois")
print('fake["en_US"].name() ->', fake["en_US"].name(), " # só en_US")

print()
print("Cada locale traz o que é específico do lugar:")
print('  fake["pt_BR"].ssn() ->', fake["pt_BR"].ssn(), " # CPF")
print('  fake["en_US"].ssn() ->', fake["en_US"].ssn(), " # SSN")
