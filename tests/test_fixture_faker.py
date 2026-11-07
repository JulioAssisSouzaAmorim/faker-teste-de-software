"""A fixture `faker` que vem com o plugin do Faker (slide 9)."""

from faker import Faker

from cadastro import cpf_valido


def test_email_valido(faker):
    email = faker.email()
    assert "@" in email


def test_locale_do_conftest_foi_aplicado(faker):
    # cpf() só existe no pt_BR: se o conftest fosse ignorado, isso daria
    # AttributeError, porque o padrão do plugin é en_US.
    assert faker.locales == ["pt_BR"]
    assert cpf_valido(faker.cpf())


def _primeiro_nome_com_seed_do_conftest():
    referencia = Faker("pt_BR")
    referencia.seed_instance(2026)
    return referencia.name()


# Os dois testes abaixo fazem a mesma coisa de propósito: a fixture é
# re-semeada antes de CADA teste, então a primeira chamada sempre devolve o
# mesmo valor, seja qual for a ordem de execução. Cada um compara com uma
# instância de referência, e não com o outro teste.
def test_primeira_chamada_e_reproduzivel(faker):
    assert faker.name() == _primeiro_nome_com_seed_do_conftest()


def test_primeira_chamada_e_reproduzivel_em_outro_teste(faker):
    assert faker.name() == _primeiro_nome_com_seed_do_conftest()


def test_seed_da_fixture_vem_do_conftest(faker, faker_seed):
    assert faker_seed == 2026
