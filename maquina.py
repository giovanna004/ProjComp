import sys

def carregar(caminho):
    C = []
    with open(caminho, encoding='utf-8') as arquivo:
        for linha in arquivo:
            partes = linha.split()
            if not partes:               # ignora linha vazia
                continue
            instrucao = partes[0]
            argumento = partes[1] if len(partes) > 1 else None
            C.append((instrucao, argumento))
    return C

def executar(C):
    pilha = []
    i = 0

    while True:
        instrucao, argumento = C[i]
        i +=1

        if instrucao == 'INPP':                     #Inicia programa
            pilha.clear()
        elif instrucao == 'CRCT':                   #Carrega constante k no topo da pilha
            pilha.append(int(argumento))
        elif instrucao == 'CRVL':                   #Carrega valor de endereco n no topo da pilha
            pilha.append(pilha[int(argumento)])
        elif instrucao == 'SOMA':                   
            topo = pilha.pop()
            antecessor = pilha.pop()
            pilha.append(topo + antecessor)
        elif instrucao == 'SUBT':                   
            topo = pilha.pop()
            antecessor = pilha.pop()
            pilha.append(antecessor - topo)         
        elif instrucao == 'MULT':                   
            topo = pilha.pop()
            antecessor = pilha.pop()
            pilha.append(topo * antecessor)
        elif instrucao == 'DIVI':                   
            topo = pilha.pop()
            antecessor = pilha.pop()
            pilha.append(antecessor / topo)
        elif instrucao == 'INVE':                   
            topo = pilha.pop()
            pilha.append(topo * -1)
        elif instrucao == 'CPME':
            topo = pilha.pop()
            antecessor = pilha.pop()
            if antecessor < topo : pilha.append(1) 
            else : pilha.append(0)
        elif instrucao == 'CPIG':
            topo = pilha.pop()
            antecessor = pilha.pop()
            if antecessor == topo : pilha.append(1) 
            else : pilha.append(0)
        elif instrucao == 'CDES':
            topo = pilha.pop()
            antecessor = pilha.pop()
            if antecessor != topo : pilha.append(1) 
            else : pilha.append(0)            
        elif instrucao == 'CPMA':
            topo = pilha.pop()
            antecessor = pilha.pop()
            if antecessor > topo : pilha.append(1) 
            else : pilha.append(0)            
        elif instrucao == 'CPMI':
            topo = pilha.pop()
            antecessor = pilha.pop()
            if antecessor <= topo : pilha.append(1) 
            else : pilha.append(0)            
        elif instrucao == 'CMAI':
            topo = pilha.pop()
            antecessor = pilha.pop()
            if antecessor >= topo : pilha.append(1) 
            else : pilha.append(0)            
        elif instrucao == 'ARMZ':                       #Armazena o topo da pilha no endereço n
            pilha[int(argumento)] = pilha.pop()
        elif instrucao == 'DSVI':
            i = int(argumento)
        elif instrucao == 'DSVF':
            if pilha.pop() == 0: i = int(argumento)
        elif instrucao == 'LEIT':                       #Lê um lado da entrada para o topo da pilha
            pilha.append(input())
        elif instrucao == 'IMPR':
            print(pilha.pop())
        elif instrucao == 'ALME':                       #Reserva m posições na pilha; m depende do tipo da variável
            pilha.extend([0.0] * int(argumento))
        if instrucao == 'PARA':   
            break
    
def main():
    if len(sys.argv) != 2:
        print("Uso: python maquina.py arquivo.obj")
        return
    try:
        C = carregar(sys.argv[1])
        executar(C)
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)

main()