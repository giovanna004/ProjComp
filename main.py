import sys

from lexico import scan
from sintatico import sintaxe
from semantico import analisar, ErroSemantico
from conversor import converter
from gerador import gerar

tokens = []

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py entrada.txt")
        return
    with open(sys.argv[1], 'r', encoding='utf-8') as arquivo:
            entrada = arquivo.read()
            tokens = scan(entrada)
            w = [t[0] for t in tokens]
            arvore = sintaxe(w, tokens)       #arvore concreta
            ast = converter(arvore)           #arvore limpa
            try:                              #confere erros, atribui enderecos
                tabela = analisar(ast)
            except ErroSemantico as e:
                print(f"Erro semantico: {e}")
                sys.exit(1)
            codigo = gerar(ast, tabela)       #lista de instrucoes
            with open(sys.argv[1], 'w', encoding='utf-8') as f:
                for instrucao in codigo:
                    f.write(instrucao + '\n')
main()
