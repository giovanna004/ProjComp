from tabela_m import tabela_M as M

def error(msg):
	raise SyntaxError(msg)

nao_terminais = {"PROG","CMDS","MAIS_CMDS","CMD","ID_CONT","VARS","MAIS_VAR",
                 "PFALSA","RESTO_IDENT","EXP_IDENT","CONDICAO","RELACAO",
                 "EXPRESSAO","TERMO","OP_UN","FATOR","OUTROS_TERMOS",
                 "OP_AD","MAIS_FATORES","OP_MUL"}

def analisa(w):
	pilha = ['$', 'PROG']
	ip = 0
	a = w[ip]
	X = pilha[-1]

	while X != '$':
		if X not in nao_terminais:
			if X == a: 
				pilha.pop()
				ip += 1
				a = w[ip]
			else:
				error(f"esperado '{X}', encontrado '{a}'")
		else:
			producao = M.get((X,a))
			if producao is None:
				error(f"token '{a}' inesperado em {X}")
			print(X, "->", " ".join(producao) or "ε")
			pilha.pop()
			for simbolo in reversed(producao):
				pilha.append(simbolo)
		X = pilha[-1]
