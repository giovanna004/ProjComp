import sys

from lexico import lexica
from sintatico import sintaxe
from semantico import semantica, ErroSemantico
from conversor import converter
from gerador import gerar

tokens = []

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py 'entrada.txt'")
        return
    with open(sys.argv[1], 'r', encoding='utf-8') as arquivo:
            entrada = arquivo.read()
            tokens = lexica(entrada)
            w = [t[0] for t in tokens]
            arvore = sintaxe(w, tokens)       #arvore concreta
            ast = converter(arvore)           #arvore limpa
            try:                              #confere erros, atribui enderecos
                tabela = semantica(ast)
            except ErroSemantico as e:
                print(f"Erro semantico: {e}")
                sys.exit(1)
            codigo = gerar(ast, tabela)       #lista de instrucoes
            with open("arquivo.obj", 'w', encoding='utf-8') as objeto:
                for instrucao in codigo:
                    objeto.write(instrucao + '\n')
main()
