import sys


def executar(C):
    D = []
    i = 0

    while True:
        op, arg = C[i]
        i +=1

        if op == 'INPP':   D.append(arg)
        if op == 'CRCT':   
            D.append(arg)
        if op == 'CRVL':   D.append(arg)
        if op == 'SOMA':   D.append(arg)
        if op == 'SUBT':   D.append(arg)
        if op == 'MULT':   D.append(arg)
        if op == 'DIVI':   D.append(arg)
        if op == 'INVE':   D.append(arg)
        if op == 'NEGA':   D.append(arg)
        if op == 'CPME':   D.append(arg)
        if op == 'CPIG':   D.append(arg)
        if op == 'CDES':   D.append(arg)
        if op == 'CPMA':   D.append(arg)
        if op == 'CPMI':   D.append(arg)
        if op == 'CMAI':   D.append(arg)
        if op == 'ARMZ':   D.append(arg)
        if op == 'DSVI':   D.append(arg)
        if op == 'DSVF':   D.append(arg)
        if op == 'LEIT':   D.append(arg)
        if op == 'IMPR':   D.append(arg)
        if op == 'ALME':   D.append(arg)
        if op == 'PARA':   D.append(arg)
    
with open(sys.argv[1], 'r', encoding='utf-8') as arquivo:
            codigo = arquivo.read()