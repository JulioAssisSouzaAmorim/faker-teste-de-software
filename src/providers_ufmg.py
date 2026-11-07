"""Providers customizados com dados da UFMG (slide 8).

Usado por tests/test_providers_customizados.py, tests/test_saidas_dos_slides.py
e demos/05_providers_customizados.py.
"""

from faker import Faker
from faker.providers import BaseProvider, DynamicProvider

CURSOS = [
    "Ciência da Computação",
    "Sistemas de Informação",
    "Matemática Computacional",
]


class MatriculaProvider(BaseProvider):
    """Jeito 1: herdar de BaseProvider, quando o dado tem lógica própria."""

    def matricula_ufmg(self) -> str:
        # numerify troca cada '#' por um dígito aleatório.
        return self.numerify("2026######")


def criar_provider_cursos(fake: Faker) -> DynamicProvider:
    """Jeito 2: DynamicProvider, quando o dado é uma escolha dentro de uma lista.

    Cuidado: passamos generator=fake. Sem isso, o DynamicProvider cria um
    Generator próprio, que usa o random global do Faker; aí fake.seed_instance()
    não afeta fake.curso() e o resultado muda a cada execução, mesmo com seed.
    """
    return DynamicProvider(provider_name="curso", elements=CURSOS, generator=fake)


def adicionar_providers_ufmg(fake: Faker) -> Faker:
    """Registra os dois providers na instância e a devolve."""
    fake.add_provider(MatriculaProvider)
    fake.add_provider(criar_provider_cursos(fake))
    return fake
