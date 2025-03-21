import enem, random

# Nome do arquivo que contém dos dados obtidos no site do MEC
nome_do_arquivo = 'dados_mec.csv'

# Registros desse arquivo
registros = enem.registros(nome_do_arquivo)

# Verifica a quantidade de registros
print('Quantidade de Registros:', enem.quantidade_registros(registros))

# Verifica a maior nota da instituição
print(f'\nMaior nota da instituição:', enem.maior_nota_instituicao(registros))

# Verifica a maior nota de corte da instituição
print(f'\nMaior nota de corte da instituição:', enem.maior_nota_corte_instituicao(registros))

# Campus
campi = enem.campi(registros)
print('\nCAMPI')
for campus in campi:
    maior_nota_campus = enem.maior_nota_campus(registros, campus)
    maior_nota_corte = enem.maior_nota_corte_campus(registros, campus)
    print(f'{campus} - Maior nota: {maior_nota_campus} - Maior nota de corte: {maior_nota_corte}')
    print(type(maior_nota_corte))
    
# Cursos de um campus escolhido aleatoriamente
campus = campi[random.randint(0, len(campi) - 1)]
cursos = enem.cursos(registros, campus)
print(f'\nCURSOS - {campus}')
for curso in cursos:
    codigo = enem.codigo_curso(registros, campus, curso)
    maior_nota_curso = enem.maior_nota_curso(registros, codigo)
    maior_nota_corte = enem.maior_nota_corte_curso(registros, codigo)
    print(f'{curso} - Maior nota: {maior_nota_curso} - Maior nota de corte: {maior_nota_corte}')