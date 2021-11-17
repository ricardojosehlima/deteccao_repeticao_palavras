import re
from more_itertools import locate, difference

with open('resultados.txt') as arquivo:
    lemas_lista = arquivo.read().split()

# Eliminando artigos e preposição 'de' da lista de lemas
# Todas as palavras estão com a classificação gramatical
# Caso seja interessante eliminar alguma classe, é só fazer o mesmo abaixo
artigos = re.compile(r"(\b([oa]|u(ma|n)s?)/ARTIGO)|(\bde\b/\S+)")
sem_artigos = [sem_art for sem_art in lemas_lista if not artigos.match(sem_art)]

# Removendo as classes gramaticais dos lemas
so_lemas = []
for lema in sem_artigos:
    lema = re.sub(r'(\w+)/\S+', r'\1', lema)
    so_lemas.append(lema)

# Detecta se há lemas repetidos três ou mais vezes em qualquer lugar do texto
# Gera lista de dicionários com o lema e os locais no texto onde ele se repete
lema_tres_repet = []
for lema in so_lemas:
    if so_lemas.count(lema) >=3:
        lema_tres_repet.append({lema: tuple(locate(so_lemas, lambda x: x == lema))})

def primeira(lista):
    '''Realiza a primeira parte de operações com lemas.'''
    # Reduz a lista a uma ocorrência apenas da informação sobre lemas e local
    lema_repet_unicos = [dict(t) for t in {tuple(d.items()) for d in lista}]

    # Informa a distância entre as repetições do lema
    global local_repet
    local_repet = []
    for d in lema_repet_unicos:
        for k, diff in d.items():
            local_repet.append({k: list(difference(diff))})

def segunda():
    '''Realiza a segunda parte de operações com lemas.'''
    # Verifica se há repetições no intervalo de 10 palavras
    repet_perto = []
    repet_perto_info = []
    for d in local_repet:
        for k, diff in d.items():
            for perto in diff[1:]:
                if perto <= 10:
                    repet_perto.append("Existem itens repetidos com menos de 10 "
                                     "palavras de distância entre eles.")
                    repet_perto_info.append((k, perto))

    # Informa se há repetições (e quantas) no intervalo de 10 palavras
    if repet_perto:
        print("\nExistem itens repetidos com menos de 10 "
              "palavras de distância entre eles.")
        print(f"Isso aconteceu {len(repet_perto)} vezes.")
        
        lemas_repetidos = []
        for t in repet_perto_info:
            lemas_repetidos.append(t[0])
        print(f"A lista dos lemas repetidos três ou mais vezes: "
          f"{set(lemas_repetidos)}")
        
        tam_texto = len(so_lemas)
        prop_lemas_texto = round((len(repet_perto)/tam_texto)*100)

        print(f"A proporção de itens repetidos em relação ao texto é de "
              f"{prop_lemas_texto:.2f}%")       
    else:
        print("\nSó há repetições distantes (+10 palavras)")

if lema_tres_repet:
    primeira(lema_tres_repet)
    segunda()
else:
    print("Não há itens repetidos três ou mais vezes no intervalo de 10 palavras.")
