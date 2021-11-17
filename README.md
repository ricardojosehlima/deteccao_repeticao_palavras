# deteccao_repeticao_palavras
Programa para detectar repetições de palavras utilizando lemas. Com isso, captura situações não detectadas por outras ferramentas.

Esse programa é resultado da disciplina eletiva oferecida por mim em 2020.2 para alunos de graduação de Letras da UERJ (Campus Maracanã).

A ideia do programa surgiu da observação de que ferramentas que detectam repetição se limitam a ocorrências idênticas da palavra. Assim:
(1) Eu quero comprar um caderno, mas tem que ser um caderno bonito e não um caderno caro.
(2) Eu quero comprar cadernos, mas tem que ser um caderno bonito e não um caderno caro.

As ferramentas (Word, Languagetool) acusam repetição tripla em (1), mas não em (2).

Lemas são as formas básicas das palavras. Para substantivos, é a forma masculino singular; para verbos, é o infinitivo, etc. Desse modo, (2) passaria a ter três ocorrências do lema 'caderno' e isso seria detectado pelo programa, que também detectaria a repetição em (1).

O programa é composto por 4 arquivos:

lem_subst_repet.py: realiza a lematização das palavras, usando como base a biblioteca Spacy e em seguida são adicionadas as correções dessa lematização (para mais sobre isso ver o repositório Lematização_Spacy_pt).

classgram_substituicoes.py: transforma e corrige a etiquetagem das palavras, usando como base a biblioteca Spacy. 

lem_repet.py: é necessário rodar esse arquivo, que recebe um .txt como fonte, para gerar o resultados.txt, com os lemas classificados gramaticalmente.

detec_repet_func.py: em seguida, deve-se rodar esse arquivo que informa se há repetição de lemas no texto.

Algumas observações sobre decisões tomadas na produção do programa:

-- retiramos apenas os artigos ('o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas') e a preposição 'de' da contagem de lemas repetidos. O interessado pode expandir o que será retirado para não ser contabilizado como repetição;

-- o programa detecta três ou mais repetições de lemas (é possível parametrizar para duas repetições);

-- em vez de fazer a busca de repetição por frase ou parágrafo, optamos por utilizar um intervalo de 10 palavras entre uma ocorrência e outra do lema.

O que ainda falta fazer:

-- nenhuma ferramenta de lematização para o português fornece o lema 'contribuir' para 'contribuição'; assim, uma frase como "Nossa contribuição para esse trabalho foi contribuir com a pesquisa. Contribuíram os seguintes alunos..." não será detectada como tendo três ocorrências de 'contribuir'; para isso, é preciso uma ferramenta semelhante ao de stemming para detectar esses casos;

-- unificar os arquivos ou algum outro modo de ser necessário rodar apenas um arquivo e não dois.
