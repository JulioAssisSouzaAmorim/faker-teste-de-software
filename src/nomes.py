"""Separação de nome e sobrenome (slide 11)."""

TITULOS = {"Sr.", "Sra.", "Srta.", "Dr.", "Dra."}


def separar_nome_ingenuo(nome: str) -> tuple[str, str]:
    """Versão com bug proposital: supõe que todo nome tem exatamente duas palavras.

    Lança ValueError para 'Dr. Benício Pereira', 'Ravy da Luz' ou
    'Maria Laura Porto', que o Faker gera com frequência.
    """
    primeiro, sobrenome = nome.split()
    return primeiro, sobrenome


def separar_nome(nome: str) -> tuple[str, str]:
    """Versão robusta: devolve (primeiro nome, restante do nome).

    - Remove títulos comuns no início (Sr., Sra., Srta., Dr., Dra.);
    - o primeiro token vira o primeiro nome;
    - todo o restante vira o sobrenome, com preposições e nomes compostos.

    Exemplos:
        'Dr. Benício Pereira' -> ('Benício', 'Pereira')
        'Ravy da Luz'         -> ('Ravy', 'da Luz')
        'Maria Laura Porto'   -> ('Maria', 'Laura Porto')
        'Pelé'                -> ('Pelé', '')
    """
    partes = nome.split()
    while partes and partes[0] in TITULOS:
        partes.pop(0)

    if not partes:
        raise ValueError(f"nome sem conteúdo: {nome!r}")

    return partes[0], " ".join(partes[1:])
