# Slide 8 — "Faltou um tipo de dado? Crie o seu provider"
# Rode a partir da raiz:  python demos/05_providers_customizados.py
#
# Os providers estão em src/providers_ufmg.py (reaproveitados pelos testes).
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.stdout.reconfigure(encoding="utf-8")

from faker import Faker  # noqa: E402

from providers_ufmg import adicionar_providers_ufmg  # noqa: E402

fake = adicionar_providers_ufmg(Faker("pt_BR"))
fake.seed_instance(5)

print("fake.matricula_ufmg() ->", repr(fake.matricula_ufmg()))  # '2026945807'
print("fake.curso()          ->", repr(fake.curso()))
# Atenção: o slide mostra 'Matemática Computacional' para curso(), mas esse
# valor não é reproduzível com o código do slide (veja o docstring de
# criar_provider_cursos em src/providers_ufmg.py).
