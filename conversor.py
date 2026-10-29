def converter(raiz):
    # PROG -> CMDS
    return conv_cmds(raiz.filhos[0])


# ---------- COMANDOS ----------

def conv_cmds(no):
    # CMDS -> ε  |  CMD MAIS_CMDS
    if not no.filhos:
        return []
    cmd = conv_cmd(no.filhos[0])
    return [cmd] + conv_mais_cmds(no.filhos[1])


def conv_mais_cmds(no):
    # MAIS_CMDS -> ε  |  ; CMDS
    if not no.filhos:
        return []
    return conv_cmds(no.filhos[1])


def conv_cmd(no):
    primeiro = no.filhos[0]
    cat = primeiro.token[0]

    # CMD -> puts id
    if cat == 'puts':
        return ('print', no.filhos[1].token[1])

    # CMD -> if CONDICAO then CMDS PFALSA end
    if cat == 'if':
        cond = conv_condicao(no.filhos[1])
        entao = conv_cmds(no.filhos[3])
        pfalsa = no.filhos[4]
        senao = conv_cmds(pfalsa.filhos[1]) if pfalsa.filhos else []
        return ('if', cond, entao, senao)

    # CMD -> while CONDICAO do CMDS end
    if cat == 'while':
        return ('while', conv_condicao(no.filhos[1]), conv_cmds(no.filhos[3]))

    # CMD -> id ID_CONT
    nome = primeiro.token[1]
    filho = no.filhos[1].filhos[0]        # RESTO_IDENT ou MAIS_VAR

    if filho.simbolo == 'RESTO_IDENT':    # x = ...
        return ('atrib', nome, conv_exp_ident(filho.filhos[1]))

    ids = [nome]                          # a, b, c
    coletar_ids(filho, ids)
    return ('decl', ids)


def coletar_ids(mais_var, ids):
    # MAIS_VAR -> ε  |  , VARS        VARS -> id MAIS_VAR
    if not mais_var.filhos:
        return
    vars_ = mais_var.filhos[1]
    ids.append(vars_.filhos[0].token[1])
    coletar_ids(vars_.filhos[1], ids)


# ---------- CONDICAO ----------

def conv_condicao(no):
    # CONDICAO -> EXPRESSAO RELACAO EXPRESSAO
    esq = conv_expressao(no.filhos[0])
    op = no.filhos[1].filhos[0].token[1]  # "==", "<", ...
    dir = conv_expressao(no.filhos[2])
    return ('cond', esq, op, dir)


# ---------- EXPRESSOES ----------

def conv_exp_ident(no):
    # EXP_IDENT -> EXPRESSAO  |  gets.to_f
    primeiro = no.filhos[0]
    if primeiro.simbolo == 'gets.to_f':
        return ('leit',)
    return conv_expressao(primeiro)


def conv_expressao(no):
    # EXPRESSAO -> TERMO OUTROS_TERMOS
    res = conv_termo(no.filhos[0])
    return conv_outros_termos(no.filhos[1], res)


def conv_termo(no):
    # TERMO -> OP_UN FATOR MAIS_FATORES
    res = conv_fator(no.filhos[1])
    if no.filhos[0].filhos:               # OP_UN nao vazio = tem "-"
        res = ('neg', res)
    return conv_mais_fatores(no.filhos[2], res)


def conv_fator(no):
    # FATOR -> id | numero_real | ( EXPRESSAO )
    primeiro = no.filhos[0]
    cat = primeiro.token[0]
    if cat == 'id':
        return ('id', primeiro.token[1])
    if cat == 'numero_real':
        return ('num', primeiro.token[1])
    return conv_expressao(no.filhos[1])   # "(" EXPRESSAO ")"


def conv_outros_termos(no, esq):
    # OUTROS_TERMOS -> ε  |  OP_AD TERMO OUTROS_TERMOS
    if not no.filhos:
        return esq
    op = no.filhos[0].filhos[0].token[1]  # "+" ou "-"
    dir = conv_termo(no.filhos[1])
    return conv_outros_termos(no.filhos[2], ('bin', op, esq, dir))


def conv_mais_fatores(no, esq):
    # MAIS_FATORES -> ε  |  OP_MUL FATOR MAIS_FATORES
    if not no.filhos:
        return esq
    op = no.filhos[0].filhos[0].token[1]  # "*" ou "/"
    dir = conv_fator(no.filhos[1])
    return conv_mais_fatores(no.filhos[2], ('bin', op, esq, dir))
