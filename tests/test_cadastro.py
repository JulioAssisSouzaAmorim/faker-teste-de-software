"""Exemplo completo com factory_boy + Faker + pytest (slide 10)."""

import factory

from cadastro import Usuario, cpf_valido, pode_cadastrar


class UsuarioFactory(factory.Factory):
    class Meta:
        model = Usuario

    nome = factory.Faker("name", locale="pt_BR")
    email = factory.Faker("email")
    # locale="pt_BR" é obrigatório: o factory_boy usa en_US por padrão,
    # e o método cpf só existe no locale brasileiro.
    cpf = factory.Faker("cpf", locale="pt_BR")
    idade = factory.Faker("pyint", min_value=18, max_value=90)


def test_adulto_com_dados_validos_pode_se_cadastrar(faker):
    usuario = Usuario(
        nome=faker.name(),
        email=faker.email(),
        cpf=faker.cpf(),
        idade=faker.pyint(min_value=18, max_value=90),
    )
    assert pode_cadastrar(usuario)


def test_menor_nao_pode_se_cadastrar():
    usuario = UsuarioFactory(idade=16)
    assert not pode_cadastrar(usuario)


def test_usuario_da_factory_pode_se_cadastrar():
    assert pode_cadastrar(UsuarioFactory())


def test_cpf_gerado_pelo_faker_e_valido(faker):
    cpfs = [faker.cpf() for _ in range(1000)]
    invalidos = [cpf for cpf in cpfs if not cpf_valido(cpf)]
    assert invalidos == []


def test_cpf_com_todos_os_digitos_iguais_e_invalido():
    assert not cpf_valido("111.111.111-11")


def test_cpf_com_tamanho_errado_e_invalido():
    assert not cpf_valido("721.175.500-8")


def test_cpf_com_digito_verificador_errado_e_invalido():
    assert not cpf_valido("721.175.500-89")


def test_cpf_do_slide_3_e_valido():
    assert cpf_valido("721.175.500-88")
    assert cpf_valido("72117550088")
