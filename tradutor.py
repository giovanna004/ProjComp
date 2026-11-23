def traduzir(ast, ts):
  cod = ["INPP"]
  for _ in ts:                 # um ALME por variavel
    cod.append("ALME 1")
  trad_cmds(ast, ts, cod)
  cod.append("PARA")
  return cod

def trad_cmds(cmds, ts, cod):
  for c in cmds:
    trad_cmd(c, ts, cod)

def trad_cmd(c, ts, cod):
  if c[0] == 'decl':
    return
  if c[0] == 'atrib':
    trad_expr(c[2], ts, cod)
    cod.append(f"ARMZ {ts[c[1]]}")
  elif c[0] == 'print':
    cod.append(f"CRVL {ts[c[1]]}")
    cod.append("IMPR")
  elif c[0] == 'while':
    inicio = len(cod)
    trad_cond(c[1], ts, cod)
    sf = len(cod); cod.append("DSVF 0")
    trad_cmds(c[2], ts, cod)
    cod.append(f"DSVI {inicio}")
    cod[sf] = f"DSVF {len(cod)}"
  elif c[0] == 'if':
    trad_cond(c[1], ts, cod)
    sf = len(cod); cod.append("DSVF 0")
    trad_cmds(c[2], ts, cod)
    if c[3]:
      si = len(cod); cod.append("DSVI 0")
      cod[sf] = f"DSVF {len(cod)}"
      trad_cmds(c[3], ts, cod)
      cod[si] = f"DSVI {len(cod)}"
    else:
      cod[sf] = f"DSVF {len(cod)}"

def trad_expr(e, ts, cod):
  if e[0] == 'num':
    cod.append(f"CRCT {e[1]}")
  elif e[0] == 'id':
    cod.append(f"CRVL {ts[e[1]]}")
  elif e[0] == 'leit':
    cod.append(f"LEIT")
  elif e[0] == 'neg':
    trad_expr(e[1], ts, cod)
    cod.append(f"INVE")
  elif e[0] == 'bin':
    trad_expr(e[2], ts, cod)   # esquerda
    trad_expr(e[3], ts, cod)   # direita
    cod.append({'+': 'SOMA', '-': 'SUBT', '*': 'MULT', '/': 'DIVI'}[e[1]])

def trad_cond(c, ts, cod):
  trad_expr(c[1], ts, cod)
  trad_expr(c[3], ts, cod)
  cod.append({'==': 'CPIG', '!=': 'CDES', '>': 'CPMA', '<': 'CPME', '>=': 'CMAI', '<=': 'CPMI'}[c[2]])
      

