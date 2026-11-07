"""Reprodutibilidade: seed, seed_instance e unique (slide 7)."""

import pytest
from faker import Faker
from faker.exceptions import UniquenessException


def test_mesma_seed_gera_o_mesmo_nome():
    Faker.seed(42)
    primeiro = Faker("pt_BR").name()
    Faker.seed(42)
    segundo = Faker("pt_BR").name()

    assert primeiro == segundo == "Brenda Alves"


def test_seed_instance_isola_uma_instancia_das_demais():
    isolada = Faker("pt_BR")
    isolada.seed_instance(42)
    esperado = [isolada.name() for _ in range(3)]

    isolada.seed_instance(42)
    # Mexer na seed global e usar outras instâncias não afeta a isolada.
    Faker.seed(999)
    outra = Faker("pt_BR")
    [outra.name() for _ in range(10)]

    assert [isolada.name() for _ in range(3)] == esperado


def test_unique_boolean_esgota_na_terceira_chamada(faker):
    valores = {faker.unique.boolean(), faker.unique.boolean()}
    assert valores == {True, False}

    with pytest.raises(UniquenessException):
        faker.unique.boolean()


def test_unique_email_nao_repete(faker):
    emails = [faker.unique.email() for _ in range(200)]
    assert len(set(emails)) == 200


def test_unique_clear_libera_os_valores(faker):
    faker.unique.boolean()
    faker.unique.boolean()

    faker.unique.clear()

    assert {faker.unique.boolean(), faker.unique.boolean()} == {True, False}
