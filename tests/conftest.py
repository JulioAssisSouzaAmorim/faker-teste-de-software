"""Configuração da fixture `faker` do plugin do Faker para o pytest (slide 9).

O plugin procura essas duas fixtures pelo nome:
- faker_session_locale: locale da instância compartilhada pela sessão;
- faker_seed: semente aplicada antes de cada teste (o padrão é 0).

Atenção: elas precisam ter autouse=True. O plugin só as enxerga se elas
estiverem entre as fixtures ativas do teste (request.fixturenames). Sem
autouse, ele as ignora e volta para o padrão: locale en_US e seed 0.
Descobrimos isso testando (veja faker/contrib/pytest/plugin.py).
"""

import pytest


@pytest.fixture(scope="session", autouse=True)
def faker_session_locale():
    return ["pt_BR"]


@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return 2026
