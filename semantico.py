class ErroSemantico(Exception):
    pass

def analisar(ast):
    ts = {}
    sem_cmds(ast, ts)
    return ts

def sem_cmds(cmds, ts):
    for cmd in cmds:
        sem_cmd(cmd, ts)

def sem_cmd(cmd, ts):
    if cmd[0] == 'decl':
        for nome in cmd[1]:
            if nome in ts: 
                raise ErroSemantico(f"'{nome}' redeclarada")
            ts[nome] = len(ts)
    elif cmd[0] == 'atrib':
        exige(cmd[1], ts)
        sem_exp(cmd[2], ts)
    elif cmd[0] == 'print':
        exige(cmd[1], ts)
    elif cmd[0] == 'if':
        sem_cond(cmd[1], ts)
        sem_cmds(cmd[2], ts)
        sem_cmds(cmd[3], ts)
    elif cmd[0] == 'while':
        sem_cond(cmd[1], ts)
        sem_cmds(cmd[2], ts)

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
        sem_exp(e[2], ts)
        sem_exp(e[3], ts)

def exige(nome, ts):
    if nome not in ts:
        raise ErroSemantico(f"variavel '{nome}' uada antes de ser declarada")
