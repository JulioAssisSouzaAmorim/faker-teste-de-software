"""Providers customizados: BaseProvider e DynamicProvider (slide 8)."""

import pytest
from faker import Faker

from providers_ufmg import CURSOS, adicionar_providers_ufmg


@pytest.fixture
def fake_ufmg():
    fake = adicionar_providers_ufmg(Faker("pt_BR"))
    fake.seed_instance(2026)
    return fake


def test_matricula_tem_10_digitos_e_comeca_com_2026(fake_ufmg):
    for _ in range(200):
        matricula = fake_ufmg.matricula_ufmg()
        assert len(matricula) == 10
        assert matricula.isdigit()
        assert matricula.startswith("2026")


def test_curso_esta_sempre_na_lista(fake_ufmg):
    for _ in range(200):
        assert fake_ufmg.curso() in CURSOS


def test_curso_e_reproduzivel_com_seed_instance():
    def tres_cursos():
        fake = adicionar_providers_ufmg(Faker("pt_BR"))
        fake.seed_instance(5)
        return [fake.curso() for _ in range(3)]

    # Só é reproduzível porque o DynamicProvider recebe generator=fake
    # (veja src/providers_ufmg.py).
    assert tres_cursos() == tres_cursos()


def test_providers_funcionam_na_fixture_faker(faker):
    adicionar_providers_ufmg(faker)
    assert faker.matricula_ufmg().startswith("2026")
    assert faker.curso() in CURSOS
