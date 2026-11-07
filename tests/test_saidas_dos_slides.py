"""Prova que os valores mostrados nos slides são saídas reais do Faker 40.44.0.

Cada teste repete a MESMA seed e a MESMA ordem de chamadas que gerou os
valores: qualquer chamada a mais ou a menos muda a sequência aleatória.
"""

from datetime import date, timedelta
from decimal import Decimal

import pytest
from faker import Faker

from cadastro import cpf_valido
from providers_ufmg import adicionar_providers_ufmg


def test_slide_3_tres_linhas_para_gerar_uma_pessoa():
    Faker.seed(42)
    fake = Faker("pt_BR")

    assert fake.name() == "Brenda Alves"
    assert fake.cpf() == "721.175.500-88"
    assert fake.email() == "mirellapereira@example.org"
    assert fake.phone_number() == "+55 82 8637-9402"


def test_slide_3_cpf_mostrado_e_valido():
    assert cpf_valido("721.175.500-88")


def _sequencia_do_slide_5():
    fake = Faker("pt_BR")
    fake.seed_instance(7)
    nomes = (
        "name cpf cnpj address city estado_sigla postcode phone_number email "
        "user_name ipv4 url company job license_plate date_of_birth iban "
        "color_name sentence uuid4"
    ).split()
    saidas = {nome: getattr(fake, nome)() for nome in nomes}
    saidas["date_between"] = fake.date_between(start_date="-30d", end_date="today")
    saidas["pydecimal"] = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
    return saidas


def test_slide_5_providers():
    saidas = _sequencia_do_slide_5()

    assert saidas["name"] == "Sr. Miguel Rezende"
    assert saidas["cpf"] == "080.592.042-03"
    assert saidas["cnpj"] == "86.094.712/0001-32"
    assert saidas["address"].splitlines()[0] == "Passarela de Aragão, 90"
    assert saidas["email"] == "sabrina75@example.net"
    assert saidas["ipv4"] == "192.103.142.99"
    assert saidas["license_plate"] == "KWL-7T97"
    assert saidas["color_name"] == "Violeta claro"
    assert saidas["pydecimal"] == Decimal("4780.21")


def test_slide_5_date_between_cai_no_intervalo():
    # O valor exato depende do dia em que o teste roda, então só
    # conferimos o intervalo pedido: de 30 dias atrás até hoje.
    data = _sequencia_do_slide_5()["date_between"]
    hoje = date.today()
    assert hoje - timedelta(days=30) <= data <= hoje


@pytest.mark.parametrize(
    ("locale", "esperado"),
    [("pt_BR", "Brenda Alves"), ("en_US", "Allison Hill"), ("ja_JP", "佐藤 淳")],
)
def test_slide_6_mesmo_codigo_em_varios_locales(locale, esperado):
    fake = Faker(locale)
    fake.seed_instance(42)
    assert fake.name() == esperado


def test_slide_6_lista_de_locales():
    fake = Faker(["pt_BR", "en_US"])
    fake.seed_instance(42)

    assert isinstance(fake.name(), str)
    assert isinstance(fake["en_US"].name(), str)
    assert fake["pt_BR"].cpf()
    assert fake["en_US"].ssn()


def _fake_do_slide_8():
    fake = adicionar_providers_ufmg(Faker("pt_BR"))
    fake.seed_instance(5)
    return fake


def test_slide_8_matricula_ufmg():
    assert _fake_do_slide_8().matricula_ufmg() == "2026945807"


@pytest.mark.xfail(
    strict=True,
    reason=(
        "DIVERGÊNCIA COM O SLIDE 8: o slide mostra 'Matemática Computacional', "
        "mas o valor não é reproduzível. Com o DynamicProvider do slide (sem "
        "generator=fake), curso() usa o random global e muda a cada execução, "
        "apesar do seed_instance(5). Ligando o provider à instância, como em "
        "src/providers_ufmg.py, a mesma sequência dá 'Ciência da Computação'. "
        "O slide precisa ser corrigido."
    ),
)
def test_slide_8_curso():
    fake = _fake_do_slide_8()
    fake.matricula_ufmg()
    assert fake.curso() == "Matemática Computacional"
