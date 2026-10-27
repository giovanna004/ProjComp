def sem_cmd(c, ts):
    if c[0] == 'decl':
        for nome in c[1]:
            if nome in ts: raise SemanticError(f"'{nome}' redeclarada")
            ts[nome] = len(ts)
    elif c[0] == 'atrib':
        exige(c[1], ts)
        sem_expr(c[2], ts)

def exige(c, ts):

def sem_exp(c, ts):
