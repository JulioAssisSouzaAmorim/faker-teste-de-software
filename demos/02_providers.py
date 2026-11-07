# Slide 5 — "26 categorias de dados, prontas para usar"
# Rode a partir da raiz:  python demos/02_providers.py
#
# A ordem das chamadas importa: é ela que reproduz os valores do slide.
import sys

from faker import Faker

sys.stdout.reconfigure(encoding="utf-8")

fake = Faker("pt_BR")
fake.seed_instance(7)

METODOS = [
    "name", "cpf", "cnpj", "address", "city", "estado_sigla", "postcode",
    "phone_number", "email", "user_name", "ipv4", "url", "company", "job",
    "license_plate", "date_of_birth", "iban", "color_name", "sentence", "uuid4",
]
NO_SLIDE = {"name", "cpf", "cnpj", "address", "email", "ipv4", "license_plate", "color_name"}

for metodo in METODOS:
    valor = getattr(fake, metodo)()
    if metodo == "address":
        valor = valor.splitlines()[0]  # o slide mostra só a primeira linha
    marca = "  <- no slide" if metodo in NO_SLIDE else ""
    print(f"{metodo:>14}: {valor!r}{marca}")

# A maioria aceita parâmetros:
print(f"{'date_between':>14}: {fake.date_between(start_date='-30d', end_date='today')!r}"
      "  <- no slide (depende do dia de hoje)")
print(f"{'pydecimal':>14}: {fake.pydecimal(left_digits=4, right_digits=2, positive=True)!r}"
      "  <- no slide")
