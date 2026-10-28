class ErroSemantico(Exception):
    pass

def analisar(ast):
    ts={}
    sem_cmds(ast, ts)
    return ts

def sem_cmds(cmds, ts)
    for cmd in cmds:
        sem_cmd(cmd, ts)

def sem_cmd(cmd, ts):
    if c[0] == 'decl':
        for nome in c[1]:
            if nome in ts: 
                raise SemanticError(f"'{nome}' redeclarada")
            ts[nome] = len(ts)
    elif c[0] == 'atrib':
        exige(c[1], ts)
        sem_expr(c[2], ts)
    elif c[0] == 'print':
        exige(c[1], ts)
    elif c[0] == 'if':
        sem_cond(c[1], ts)
        sem_cmds(c[2], ts)
        sem_cmds(c[3], ts)
    elif c[0] == 'while':
        sem_cond(c[1], ts)
        sem_cmds(c[2], ts)

def sem_cond(c, ts):
    sem_exp(c[1], ts)
    sem_exp(c[3], ts)

def sem_exp(e, ts):
    tipo = e[0]

    if tipo == 'id':
        exige(e[1], ts)
    elif tipo == 'neg':
        sem_exp(e[1], ts)
    elif tipo == 'bin':
        sem_exp(c[2], ts)
        sem_exp(c[3], ts)

def exige(nome, ts):
    if nome not in ts:
        raise ErrorSemantico(f"variavel '{nome}' uada antes de ser declarada)
