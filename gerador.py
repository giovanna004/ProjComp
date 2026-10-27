def gen_cmd(c, ts, cod):
  if c[0] == 'atrib':
    gen_expr(c[2], ts, cod); cod.append(f"ARMZ {ts[c[1]]]}")
  elif c[0] == 'print':
    cod.append(f"CRVL {ts[c[1]]}"); cod.append("IMPR")
  elif c[0] == 'while':
    inicio = len(cod)
    gen_cond(c[1], ts, cod)
    sf = len(cod); cod.append("DSVF 0")
    gen_cmds(c[2], ts, cod)
    cod.append(f"DSVI {inicio}")
    cod[sf] = f"DSVF {len(cod)}"
  elif c[0] == 'if':
    gen_cond(c[1], ts, cod)
    sf = len(cod); cod.append("DSVF 0")
    gen_cmds(c[2], ts, cod)
    if c[3]:
      si = len(cod); cod.append("DSVI 0")
      cod[sf] = f"DSVF {len(cod)}"
      gen_cmds(c[3], ts, cod)
      cod[si] = f"DSVI {len(cod)}"
    else:
      cod[sf] = f"DSVF {len(cod)}"
