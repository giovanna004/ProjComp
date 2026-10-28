import sys

from lexico import scan
from sintatico import analisa
from semantico import analisar
from conversor_ast import converter
from gerador import gerar

from tabela_m import tabela_M 

tokens = []
ts = {}

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py entrada.txt")
        return
    with open(sys.argv[1], 'r', encoding='utf-8') as arquivo:
            entrada = arquivo.read()
            tokens, ts = scan(entrada)
            arvore = analisa(w, tokens)       #arvore concreta
            ast = converter(arvore)           #arvore limpa
            try:                              #confere erros, atribui enderecos
                tabela = analisar(ast)
            except ErroSemantico as e:
                print(f"Erro semantico: {e}")
                sys.exit(1)
            codigo = gerar(ast, tabela)       #lista de instrucoes

main()
