"""Cuidados com dados aleatórios (slide 11)."""

import re

import pytest
from faker import Faker

from nomes import TITULOS, separar_nome, separar_nome_ingenuo


def gerar_nomes_do_experimento() -> list[str]:
    """Mesma configuração do slide: pt_BR, seed_instance(3), 1.000 nomes."""
    fake = Faker("pt_BR")
    fake.seed_instance(3)
    return [fake.name() for _ in range(1000)]


def test_438_de_1000_nomes_nao_tem_exatamente_duas_palavras():
    nomes = gerar_nomes_do_experimento()
    fora_do_padrao = [n for n in nomes if len(n.split()) != 2]

    # Esse número exato só vale para a versão fixada no requirements.txt
    # (Faker==40.44.0). Os dados gerados mudam entre versões, até nas de patch.
    assert len(fora_do_padrao) == 438
    for exemplo in ("Dr. Benício Pereira", "Ravy da Luz", "Maria Laura Porto"):
        assert exemplo in fora_do_padrao


@pytest.mark.parametrize(
    "nome",
    ["Dr. Benício Pereira", "Ravy da Luz", "Maria Laura Porto"],
)
def test_separar_nome_ingenuo_quebra_com_nomes_do_faker(nome):
    # O bug que o Faker revela: split() devolve 3 partes, não 2.
    with pytest.raises(ValueError):
        separar_nome_ingenuo(nome)


def test_separar_nome_ingenuo_funciona_no_caso_feliz():
    # Com um "João Silva" escrito à mão, o bug nunca apareceria.
    assert separar_nome_ingenuo("João Silva") == ("João", "Silva")


@pytest.mark.parametrize(
    ("nome", "esperado"),
    [
        ("Dr. Benício Pereira", ("Benício", "Pereira")),
        ("Ravy da Luz", ("Ravy", "da Luz")),
        ("Maria Laura Porto", ("Maria", "Laura Porto")),
        ("Srta. Ana Luiza Castro", ("Ana", "Luiza Castro")),
        ("João Silva", ("João", "Silva")),
    ],
)
def test_separar_nome_trata_os_casos_do_slide(nome, esperado):
    assert separar_nome(nome) == esperado


def test_separar_nome_funciona_para_os_1000_nomes_gerados():
    for nome in gerar_nomes_do_experimento():
        primeiro, sobrenome = separar_nome(nome)

        assert primeiro not in TITULOS
        assert sobrenome != ""
        assert nome.endswith(f"{primeiro} {sobrenome}")


def test_verifica_propriedades_do_email_e_nao_valor_exato(faker):
    email = faker.email()

    # Em vez de: assert email == "sabrina75@example.net"
    usuario, dominio = email.split("@")
    assert usuario
    assert re.fullmatch(r"[\w.-]+\.[a-z]{2,}", dominio)
