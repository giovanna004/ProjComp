def gerar(ast, ts):
  cod = ["INPP"]
  for _ in ts:                 # um ALME por variável
    cod.append("ALME 1")
  gerar_comandos(ast, ts, cod)
  cod.append("PARA")
  return cod

def gerar_cmds(cmds, ts, cod):
  for c in cmds:
    gerar_comando(c, ts, cod)

def gerar_cmd(c, ts, cod):
  if c[0] == 'decl':
    return
  if c[0] == 'atrib':
    gerar_expr(c[2], ts, cod)
    cod.append(f"ARMZ {ts[c[1]]]}")
  elif c[0] == 'print':
    cod.append(f"CRVL {ts[c[1]]}")
    cod.append("IMPR")
  elif c[0] == 'while':
    inicio = len(cod)
    gerar_cond(c[1], ts, cod)
    sf = len(cod); cod.append("DSVF 0")
    gerar_cmds(c[2], ts, cod)
    cod.append(f"DSVI {inicio}")
    cod[sf] = f"DSVF {len(cod)}"
  elif c[0] == 'if':
    gerar_cond(c[1], ts, cod)
    sf = len(cod); cod.append("DSVF 0")
    gen_cmds(c[2], ts, cod)
    if c[3]:
      si = len(cod); cod.append("DSVI 0")
      cod[sf] = f"DSVF {len(cod)}"
      gen_cmds(c[3], ts, cod)
      cod[si] = f"DSVI {len(cod)}"
    else:
      cod[sf] = f"DSVF {len(cod)}"

def gerar_expr(e, ts, cod):
  if e[0] == 'num':
    cod.append(f"CRCT {e[1]}")
  elif e[0] == 'id':
    cod.append(f"CRVL {tabela[e[1]]}"})
  elif e[0] == 'leit':
    cod.append(f"LEIT")
  elif e[0] == 'neg':
    gerar_expr(e[1], ts, cod)
    cod.append(f"INVE")
  elif e[0] == 'bin':
    gerar_expr(e[2], tabela, cod)   # esquerda
    gerar_expr(e[3], tabela, cod)   # direita
    cod.append({'+': 'SOMA', '-': 'SUBT', '*': 'MULT', '/': 'DIVI'}[e[1]])

def gerar_cond(c, ts, cod):
  gerar_exp(c[1], ts, cod)
  gerar_exp(c[3], ts, cod)
  cod.append({'==': 'CPIG', '!=': 'CDES', '>': 'CPMA', '<': 'CPME', '>=': 'CMAI', '<=': 'CPMI}[c[2]])
      

