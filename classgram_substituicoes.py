cg_substituicoes = {
    # 'o, a, os, as' (exceto pronomes) e 'um, uma, uns, umas' como Artigos
    'det_artigos': (r'(?i)(\b([oa]|u((ma?)|n))s?/)[^P]\w+\b', r'\1ARTIGO'),
    # 'do, da, dos das'; 'no, na, nos, nas' (exceto pronomes); 'pelo, pela, pelos, pelas'; 'pro, pra, pros, pras' como Preposição+Artigo
    'de_em_art_def_prep': (r'(?i)(\b((p(r|el)|[dn])[oa]s?)/)[^P]\S+\b', r'\1PREPOSIÇÃO#ARTIGO'),
    # Forçando 'de' a ser Preposição
    'de_prep': (r'(?i)(\bde/)\S+\b', r'\1PREPOSIÇÃO'),
    # Pronomes (e outros?) classificados como DET passam para Pronomes 
    'det_pronomes': (r'(?i)(\b\w{3,}/)DET\b', r'\1PRONOME'),
    # 'tu' e 'te' como Pronomes
    '2ap_pronome': (r'(?i)(\bt[ue]/)\S+\b', r'\1PRONOME'),
    # 'comigo, contigo, conosco, convosco' como Pronomes
    'com_pronome': (r'(?i)(\bco((m|nt)ig|nv?osc)o/)\S+\b', r'\1PRONOME'),
    # 'à, às, ao, aos' como Preposição+Artigo
    'a_art_prep': (r'(?i)(\b(à|ao)s?/)\S+\b', r'\1PREPOSIÇÃO#ARTIGO'),
    # 'dum, duma, duns, dumas', 'num, numa...' como Preposição+Artigo
    'de_em_art_indef_prep_': (r'(?i)(\b[dn]u(m(as?)?|ns)/)\S+\b', r'\1PREPOSIÇÃO#ARTIGO'),
    # 'àquilo, àquele, àqueles, àquela, àquelas' como Preposição+Pronome
    'à_aquele': (r'(?i)(\b(àquel[ea]s?|àquilo)/)\S+\b', r'\1PREPOSIÇÃO#PRONOME'),
    # Contração de 'de' e 'em' com aquele, este, isto, aquilo, outro e variações como Preposição+Pronome
    'de_em_pron_demonstr': (r'(?i)(\b[dn](((aqu)?el[ea]s?)|(es[ts][ea]s?)|is[st]o|aquilo|outr[oa]s?)/)\S+\b', r'\1PREPOSIÇÃO#PRONOME'),
    # Contração de 'de' e 'aí, ali, aqui' como Preposição+ Advérbio
    'de_adv': (r'(?i)(\bd(aqui|aí|ali)/)\S+\b', r'\1PREPOSIÇÃO#ADVÉRBIO'),
    # Situações de ênclise como Verbo+Pronome
    'enclise': (r'(?i)(\w+-([mts]e|lhes?|[lnv][oa]s?)/)\S+\b', r'\1VERBO#PRONOME'),
    # Situações de mesóclise como Verbo+Pronome+Desinência
    'mesoclise': (r'(?i)(\w+-([mts]e|lhes?|[lnv][oa]s?)(-\w+)/)\S+\b', r'\1VERBO#PRONOME#DESINENCIA'),
    # Forçando 'aquele' e variações classificados como Adjetivos para Pronomes
    'aquele_pronome': (r'(?i)(\baquel[ea]s?/)\S+\b', r'\1PRONOME'),
    # Forçando 'ante' e 'dentre' como Preposição
    'ante_dentre_prep': (r'(?i)(\b(ante|dentre)/)\S+\b', r'\1PREPOSIÇÃO'),
    # Forçando 'devagar' e 'trás' como Advérbio
    'devagar_trás_adv': (r'(?i)(\b(devagar|trás)/)\S+\b', r'\1ADVÉRBIO'),
    # Forçando 'sã' e 'lindos' como Adjetivo
    'sã_lindos_adjetivo': (r'(?i)(\b(sã|lindos)/)\S+\b', r'\1ADJETIVO'),
    # Forçando 'talvez' como Advérbio
    'talvez_adverbio': (r'(?i)(\btalvez/)\S+\b', r'\1ADVÉRBIO'),
    # Forçando 'tomara' como Interjeição
    'tomara_interjeição': (r'(?i)(\btomara/)\S+\b', r'\1INTERJEIÇÃO'),
    # Forçando 'remos' e como Substantivo
    'remos_substantivo': (r'(?i)(\bremos/)\S+\b', r'\1SUBSTANTIVO'),
    # Forçando 'extremos' como Adjetivo
    'extremos_adjetivo': (r'(?i)(\bextremos/)\S+\b', r'\1ADJETIVO'), # "Os extremos..."
    # Forçando 'roeu' como Verbo
    'roeu_verbo': (r'(?i)(\broeu/)\S+\b', r'\1VERBO'),
    # Forçando 'perto' e 'longe' como Advérbio
    'longe_perto_advérbio': (r'(?i)(\b(longe|perto)/)\S+\b', r'\1ADVÉRBIO'),
    # Forçando números como Numerais
    'numeros_numerais': (r'(?i)(\b\d+/)\S+\b', r'\1NUMERAL'),
    # Forçando 'cada' como Pronome
    'cada_pronome': (r'(?i)(\bcada/)\S+\b', r'\1PRONOME'),
    # Forçando 'oi' e 'olá' como Interjeição
    'oi_ola_interjeicao': (r'(?i)(\b(oi|olá)/)\S+\b', r'\1INTERJEIÇÃO'),
    # Forçando numerais classificados como adjetivos a serem numerais
    'num_adj_numerais_1': (r'(?i)(\b(primeir|segund|terceir|quart|quint|sext|sétim|oitav|non)[oa]s?/)\S+\b', r'\1NUMERAL'), # ver 'Vou sair na quarta'
    'num_adj_numerais_2': (r'(?i)(\b(décim|(vi|tri|quadra|quinqua|sexa|hepta|octa|nona)gésim|(cent|mil)ésim)[oa]s?/)\S+\b', r'\1NUMERAL'), # Faltam: milhão etc.
    # Mudando Verbo-do e variações (Particípio) para Adjetivo 
    'participio_adjetivo': (r'(?i)(\b\w+[^n\s]d[oa]s?/)VERB\b', r'\1ADJETIVO'),
    # Muda verbo-adjetivo para verbo-advérbio (errou feio)
    'v_adj': (r'(?i)(\b\w+/VERB\s\w+/)ADJ', r'\1ADVÉRBIO'),
    # Forçando'no entanto' como Conjunção
    'no_entanto': (r'(?i)(\bno\b/)\S+(\s\bentanto\b/)\S+',
                   r'\1CONJUNÇÃO\2CONJUNÇÃO'),
    # Forçando'às vezes' como Conjunção
    'as_vezes': (r'(?i)(\bàs\b/)\S+(\s\bvezes\b/)\S+',
                   r'\1CONJUNÇÃO\2CONJUNÇÃO'),
    # Forçando'posto que' como Conjunção
    'posto_que': (r'(?i)(\bposto\b/)\S+(\s\bque\b/)\S+',
                   r'\1CONJUNÇÃO\2CONJUNÇÃO'),
        
    # Transformando as etiquetas de UD nas da gramática tradicional
    # Tem que vir no final se não as regras det_pronomes, participio_adjetivo não funcionam 
    'det_artigo': (r'det\b', r'ARTIGO'),
    'noun_substantivo': (r'noun\b', r'SUBSTANTIVO'),
    'propn_nome_proprio': (r'propn\b', r'NOME#PRÓPRIO'),
    'verb_verbo': (r'verb\b', r'VERBO'),
    'adj_adjetivo': (r'adj\b', r'ADJETIVO'),
    'adv_advérbio': (r'adv\b', r'ADVÉRBIO'),
    'num_numeral': (r'num\b', r'NUMERAL'),
    'pron_pronome': (r'pron\b', r'PRONOME'),
    'adp_preposição': (r'adp\b', r'PREPOSIÇÃO'),
    'scconj_conjunção': (r'[cs]conj\b', r'CONJUNÇÃO'),
    'intj_interjeição': (r'intj\b', r'INTERJEIÇÃO'),
    'aux_auxiliar': (r'aux\b', r'AUXILIAR'),
    'sym_simb': (r'sym\b', r'SIMB'),
    'punct_pontuação': (r'punct\b', r'PONTUAÇÃO'),
    'X_outros': (r'/x\b', r'/OUTROS'),
          }
