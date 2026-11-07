"""Domínio do exemplo completo (slide 10): quem pode se cadastrar."""

import re
from dataclasses import dataclass


@dataclass
class Usuario:
    nome: str
    email: str
    cpf: str
    idade: int


def cpf_valido(cpf: str) -> bool:
    """Confere formato e dígitos verificadores de um CPF.

    Aceita o CPF com ou sem pontuação ('721.175.500-88' ou '72117550088').
    """
    digitos = re.sub(r"\D", "", cpf)

    if len(digitos) != 11:
        return False
    # '111.111.111-11' passa na conta dos dígitos, mas não é um CPF válido.
    if len(set(digitos)) == 1:
        return False

    # O 10º dígito usa os 9 primeiros (pesos 10..2);
    # o 11º usa os 10 primeiros (pesos 11..2).
    for tamanho in (9, 10):
        soma = sum(int(digitos[i]) * (tamanho + 1 - i) for i in range(tamanho))
        verificador = (soma * 10) % 11 % 10
        if verificador != int(digitos[tamanho]):
            return False

    return True


def pode_cadastrar(u: Usuario) -> bool:
    """Maior de idade, e-mail com arroba e CPF válido."""
    return u.idade >= 18 and "@" in u.email and cpf_valido(u.cpf)
