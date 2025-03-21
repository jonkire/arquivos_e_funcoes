# Registros encontrados no arquivo
def registros(file: str) -> list:
    arq = open(file, 'r', encoding="UTF-8")
    lista = arq.read().splitlines()
    arq.close()
    # A primeira linha contém o cabeçalho de cada campo.
    # Retornar a partir da segunda linha
    return lista[1:]


# Quantidade de registros
def quantidade_registros(registros: list) -> int:
    return len(registros)


# Relação dos Campi da Instituição.
def campi(registros: list) -> list:
    ans = list()
    for linha in registros:
        campi = linha.split(';')
        if campi[4].replace('"', '') not in ans:
            ans.append(campi[4].replace('"', ''))
    return ans


# Relação dos Cursos de um determinado Campus.
def cursos(registros: list, nome_campus: str) -> list:
    ans = list()
    for linha in registros:
        line = linha.split(';')
        campi = line[4]
        if nome_campus in campi:
            if line[6].replace('"', '') not in ans:
                ans.append(line[6].replace('"', ''))
    return ans


# Maior nota da instituição
def maior_nota_instituicao(registros: list) -> float:
    ans = list()
    for linha in registros:
        line = linha.split(';')
        nota = line[16]
        nota = nota.replace('"', '').replace(',', '.')
        if nota not in ans:
            ans.append(float(nota))
    return max(ans)


# Maior nota do Campus
def maior_nota_campus(registros: list, nome_campus: str) -> float:
    ans = list()
    for linha in registros:
        line = linha.split(';')
        campi = line[4]
        if nome_campus in campi:
            nota = line[16]
            nota = nota.replace('"', '').replace(',', '.')
            ans.append(float(nota))
    return max(ans)
        

# Maior nota de um Curso
def maior_nota_curso(registros: list, codigo_curso: int) -> float:
    ans = list()
    for linha in registros:
        line = linha.split(';')
        cd = line[5]
        if str(codigo_curso) in cd:
            nota = line[16]
            nota = nota.replace('"', '').replace(',', '.')
            ans.append(float(nota))
    return max(ans)


# Maior nota de corte da instituição
def maior_nota_corte_instituicao(registros: list) -> float:
    ans = list()
    for linha in registros:
        line = linha.split(';')
        notacorte = line[17]
        notacorte = notacorte.replace('"', '').replace(',', '.')
        ans.append(float(notacorte))
    return max(ans)


# Maior nota do Campus
def maior_nota_corte_campus(registros: list, nome_campus: str) -> float:
    ans = list()
    for linha in registros:
        line = linha.split(';')
        nc = line[4]
        if nome_campus in nc:
            nota = line[17]
            nota = nota.replace('"', '').replace(',', '.')
            ans.append(float(nota))
    return max(ans)


# Maior nota de um Curso
def maior_nota_corte_curso(registros: list, codigo_curso: int) -> float:
    ans = list()
    for linha in registros:
        line = linha.split(';')
        cd = line[5]
        if str(codigo_curso) in cd:
            nota = line[17]
            nota = nota.replace('"', '').replace(',', '.')
            ans.append(float(nota))
    return max(ans)


# Retorna o código de um determinado curso de um determinado campus
def codigo_curso(registros: list, nome_campus: str, nome_curso: str) -> int:
    for linha in registros:
        line = linha.split(';')
        if nome_campus in line[4] and nome_curso in line[6]:
            return int(line[5].replace('"', ''))
