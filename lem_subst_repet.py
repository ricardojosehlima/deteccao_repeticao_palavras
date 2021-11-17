substituicoes = {
    # Começo do conjunto de regras
    # Beginning of the set of rules
    # Consertando palavras no plural que ficam com lemas no plural
    # Fixing words in plural whose lemmas remain in plural
    "lema_plural": (r"(?P<tudo>(?P<rad>\b\w+)s\b)(?P<morfo>/\1/\S+plur\S*)", r"\g<tudo>/\g<rad>\g<morfo>"),
    # Consertando e dividindo contrações de preposições e artigos
    # Fixing and splitting contractions of prepositions and determiners
    "dos": (r"\bd(?P<dos>[oa]s?\b)\S+", r"de/de/adp \g<dos>/o/det"),
    "nos": (r"\bn(?P<nos>[oa]s?\b)\S+", r"em/em/adp \g<nos>/o/det"),
    "aos": (r"\ba(?P<aos>os?\b)\S+", r"a/a/adp \g<aos>/o/det"),
    "pelos": (r"\bpel(?P<pelos>[oa]s?\b)\S+", r"por/por/adp \g<pelos>/o/det"),
    # Consertando algumas palavras específicas
    # Fixing more specific words
    "suas": (r"(?P<suas>\bsuas?\b)\S+", r"\g<suas>/seu/pron"),
    "umas": (r"(?P<umas>\bumas?\b)\S+", r"\g<umas>/um/det"),
    "vou_vamos": (r"(?P<vou_vamos>\b(vou|vamos)\b)\S+", r"\g<vou_vamos>/ir/verb"),
    "diga": (r"(?P<diga>zbdiga\b)\S+", r"\g<diga>/dizer/verb"),
    "nós": (r"(?P<nós>\bnós\b)\S+", r"\g<nós>/nós/pron"),
    "e_ser": (r"(?P<é>\bé\b)\S+", r"\g<é>/ser/verb"),
    "vi": (r"(?P<vi>\bvi\b)\S+", r"\g<vi>/ver/verb"),
    "quero": (r"(?P<quero>\bquero\b)\S+", r"\g<quero>/querer/verb"),
    "para": (r"(?P<para>\bpara\b)\S+", r"\g<para>/para/adp"),

    # Consertando e dividindo contrações de preposições e pronomes
    # Fixing and splitting contractions of prepositions and pronouns
    "de_pron": (
        r"\bd(?P<rad>aquel|es?[lts]?)(?P<des>[ea]s?)\b\S+",
        r"de/de/adp \g<rad>\g<des>/\g<rad>e/pron",
    ),
    "de_pron_i": (r"\bd(?P<rad>aquil|is[ts]?)o\b\S+", r"de/de/adp \g<rad>o/\g<rad>o/pron"),
    "em_pron": (
        r"\bn(?P<rad>aquel|es?[lts]?)(?P<des>[ea]s?)\b\S+",
        r"em/em/adp \g<rad>\g<des>/\g<rad>e/pron",
    ),
    "em_pron_i": (r"\bn(?P<rad>aquil|is?[ts]?)o\b\S+", r"em/em/adp \g<rad>o/\g<rad>o/pron"),
    # Consertando situações com a preposição "a"
    # Fixing issues envolving preposition "a"
    "a": (r"(?P<a>\ba\b)/o/[sa]\S+", r"\g<a>/a/adp"),
    "à": (r"(?P<à>\bàs?\b)\S+", r"\g<à>/a/adp a/a/det"),
    # Consertando casos de classes gramaticais fechadas
    # Fixing issues with closed class words
    "final_r": (
        r"(?P<pal>\b\w+\b)/\b\w+r\b/(?P<tags>det|adv|adp|sconj)\S*",
        r"\g<pal>/\g<pal>/\g<tags>",
    ),
    # Consertando número e gênero de adjetivos
    # Fixing number and gender of adjectives
    "adj_fp": (r"(?P<tudo>(?P<rad>\b\w+)as?\b/adj\S+)", r"\g<tudo>/\g<rad>o/adj"),
    # Consertando substantivos
    # Fixing nouns
    "subs_a": (
        r"(?P<tudo>(?P<simples_a>\b\w+a)s\b)/\w+[rs]/(?P<adjnoun>adj|noun)\S+plur",
        r"\g<tudo>/\g<simples_a>/\g<adjnoun>",
    ),
    # empresas, amoras mas professoras fica professora (mesmo problema do Udpipe e Stanza)
    "subs_r": (
        r"(?P<tudo>(?P<simples_r>\b\w+)es\b)/\w+r/(?P<adjnoun>adj|noun)\S+plur",
        r"\g<tudo>/\g<simples_r>/\g<adjnoun>",
    ),  # cores, mares, meses, pazes
    "subs_l": (
        r"(?P<tudo>(?P<simples_l>\b\w+)is\b)/\w+r/(?P<adjnoun>adj|noun)\S+plur",
        r"\g<tudo>/\g<simples_l>l/\g<adjnoun>",
    ),  # portais
    "subs_sg": (
        r"(?P<simples_sg>\b\w+[^r]\b)/\w+r/(?P<adjnoun>adj|noun)\S+sing",
        r"\g<simples_sg>/\g<simples_sg>/\g<adjnoun>",
    ),  # livro, empresa
    # Consertando particípios de verbos da 1ª conjugação
    # Fixing participles of verbs from the 1st conjugation
    "partic": (
        r"(?P<tudo>(?P<rad>\b\w+a)(?P<partic>d[oa]s?)\b)/\w+d[oa]s?/verb\S+",
        r"\g<tudo>/\g<rad>r/verb",
    ),
    # Consertando parcialmente particípios de verbos da 2ª e 3ª conjugações,
    # Partially fixing participles of verbs from the 2nd and 3rd conjugations,
    "partic_e": (
        r"(?P<tudo>(?P<rad>\b\w+[csho])[ií](?P<partic>d[oa]s?)\b)/\w+d[oa]s?/verb\S+",
        r"\g<tudo>/\g<rad>er/verb",
    ),
    "partic_e_2": (
        r"(?P<tudo>(?P<rad>\breceb)i(?P<partic>d[oa]s?)\b)/\w+d[oa]s?/verb\S+",
        r"\g<tudo>/\g<rad>er/verb",
    ),
    "partic_i": (
        r"(?P<tudo>(?P<rad>\b\w+[anju])[ií](?P<partic>d[oa]s?)\b)/\w+d[oa]s?/verb\S+",
        r"\g<tudo>/\g<rad>ir/verb",
    ),
    "partic_i_2": (
        r"(?P<tudo>(?P<rad>\bl)i(?P<partic>d[oa]s?)\b)/lidar/verb\S+",
        r"\g<tudo>/\g<rad>er/verb",
    ),
    # Removendo as postags e as features das tags remanescentes
    # Removing the remaining postags and tag features
    # "pal_lema": (r"(?P<pal_lema>\b\w+(-\w+)*/\w+(-\w+)*\b)\S*", r"\g<pal_lema>"),
    "so_postag": (r'\w+/(\w+/\w+)(/(\S*))?', r'\1'),
    "sem_pontuacao": (r'[.,;:?!-"\']\S*', r""),
    "sem_numeros": (r"\d+([.,/-]?(\d+))*", r""),
    "sem_num_card": (r"\S*/(num|card)", r""),
    # Ao comentar a linha abaixo, vai ser gerado o par palavra/lema em vez
    # de apenas os lemas. Pode ser útil para checar inconsistências do código.
    # If the line below is commented, instead of generating only the lemmas,
    # the code will generate a pair word/lemma. This can be useful to check
    # inconsistencies in the code.
    # Apenas os lemas
    # Only the lemmas
    # "lemas": (r"\b\w+(-\w+)*\b/(?P<lemas>\b\w+(-\w+)*\b)", r"\g<lemas>"),
}
