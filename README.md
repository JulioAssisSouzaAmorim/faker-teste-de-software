# Faker: dados falsos para testes de verdade

[![testes](https://github.com/JulioAssisSouzaAmorim/faker-teste-de-software/actions/workflows/testes.yml/badge.svg)](https://github.com/JulioAssisSouzaAmorim/faker-teste-de-software/actions/workflows/testes.yml)

Código que acompanha o Seminário 6 (Test Double) da disciplina **Teste de Software**, UFMG, 2026/2, com o **Prof. André Hora**.

**Integrantes:** Júlio Assis Souza Amorim, Gustavo Chaves Ferreira e Daniel Vitor Rabelo Rodrigues.

## O que é o Faker

O [Faker](https://faker.readthedocs.io/) é uma biblioteca Python, open source, que gera dados falsos mas plausíveis: nomes, CPFs, endereços, e-mails, datas e muito mais, em 110 locales. Com ele, os testes usam dados variados e realistas que não pertencem a ninguém, sem copiar dados de produção.

**O Faker não é um test double.** Stubs, mocks e fakes substituem dependências do código testado. O Faker gera os **dados de entrada** do teste, como o usuário que vai ser salvo num banco fake em memória. Por isso eles se combinam: os test doubles cuidam das dependências e o Faker cuida dos dados.

## Como rodar

Requer Python 3.10 ou mais recente.

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
pytest -q
```

As demos rodam a partir da raiz do repositório e imprimem as mesmas saídas dos slides:

```bash
python demos/01_basico.py
python demos/02_providers.py
python demos/03_locales.py
python demos/04_seed_e_unique.py
python demos/05_providers_customizados.py
python demos/06_experimento_nomes.py
```

O `requirements.txt` fixa o **Faker 40.44.0**. Os valores dos slides só se reproduzem nessa versão.

## Slide → arquivo

| Slide | Assunto | Código | Testes |
|---|---|---|---|
| 3 | Três linhas para gerar uma pessoa | [demos/01_basico.py](demos/01_basico.py) | [tests/test_saidas_dos_slides.py](tests/test_saidas_dos_slides.py) |
| 5 | Providers | [demos/02_providers.py](demos/02_providers.py) | [tests/test_saidas_dos_slides.py](tests/test_saidas_dos_slides.py) |
| 6 | Localização | [demos/03_locales.py](demos/03_locales.py) | [tests/test_saidas_dos_slides.py](tests/test_saidas_dos_slides.py) |
| 7 | Seed e unique | [demos/04_seed_e_unique.py](demos/04_seed_e_unique.py) | [tests/test_seed_e_unique.py](tests/test_seed_e_unique.py) |
| 8 | Providers customizados | [src/providers_ufmg.py](src/providers_ufmg.py), [demos/05_providers_customizados.py](demos/05_providers_customizados.py) | [tests/test_providers_customizados.py](tests/test_providers_customizados.py), [tests/test_saidas_dos_slides.py](tests/test_saidas_dos_slides.py) |
| 9 | Faker no pytest | [tests/conftest.py](tests/conftest.py) | [tests/test_fixture_faker.py](tests/test_fixture_faker.py) |
| 10 | Exemplo completo com factory_boy | [src/cadastro.py](src/cadastro.py) | [tests/test_cadastro.py](tests/test_cadastro.py) |
| 11 | Cuidados | [src/nomes.py](src/nomes.py), [demos/06_experimento_nomes.py](demos/06_experimento_nomes.py) | [tests/test_cuidados.py](tests/test_cuidados.py) |

## Cuidados

Dados aleatórios revelam suposições, mas também podem esconder falhas (slide 11):

- **Use seed e fixe a versão.** Sem seed, um bug que só aparece com certos dados torna o teste flaky. E os dados gerados mudam entre versões do Faker, até nas de patch. Em 1.000 nomes `pt_BR` com seed 3, **438** não têm exatamente duas palavras (`'Dr. Benício Pereira'`, `'Ravy da Luz'`, `'Maria Laura Porto'`). Esse número só vale para o Faker 40.44.0.
- **Verifique propriedades, não valores.** Confira que o e-mail tem `@` e um domínio, e não que ele é igual a `'sabrina75@example.net'`.
- **Plausível não é real.** O Faker inventa cidades, gera lorem ipsum em latim mesmo no `pt_BR` e pode dar uma data de nascimento em 1920. Quando isso importa, passe parâmetros (por exemplo, `minimum_age` e `maximum_age`).
- **Não use o Faker para o valor que o teste verifica.** Se o teste é sobre a idade, a idade fica escrita no teste: `UsuarioFactory(idade=16)`.

### Armadilha: `DynamicProvider` e seed

Um `DynamicProvider` criado sem `generator` usa o gerador aleatório global, e não o da instância. Por isso `fake.seed_instance(...)` não controla os valores dele. Em [src/providers_ufmg.py](src/providers_ufmg.py) passamos `generator=fake` para que o resultado seja reproduzível.
