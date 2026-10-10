import sys

from analisador_lexico import scan
from tabela_m import tabela_M 
from analisador_sintatico import analisa

tokens = []
ts = {}

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py entrada.txt")
        return
    with open(sys.argv[1], 'r', encoding='utf-8') as arquivo:
            entrada = arquivo.read()
            tokens, ts = scan(entrada)
            w = [t[0] for t in tokens]
            analisa(w, tokens)

main()