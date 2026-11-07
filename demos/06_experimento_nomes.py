# Slide 11 — "Dados aleatórios revelam suposições, e também podem esconder falhas"
# Rode a partir da raiz:  python demos/06_experimento_nomes.py
import sys

from faker import Faker

sys.stdout.reconfigure(encoding="utf-8")

fake = Faker("pt_BR")
fake.seed_instance(3)
nomes = [fake.name() for _ in range(1000)]

fora_do_padrao = [n for n in nomes if len(n.split()) != 2]
print(f"{len(fora_do_padrao)} de {len(nomes)} nomes não têm exatamente duas palavras")
print()
print("Exemplos:")
for nome in fora_do_padrao[:8]:
    print("  ", repr(nome))

print()
print("Um split() ingênuo quebra com eles:")
try:
    primeiro, sobrenome = "Dr. Benício Pereira".split()
except ValueError as erro:
    print("   'Dr. Benício Pereira'.split() -> ValueError:", erro)
