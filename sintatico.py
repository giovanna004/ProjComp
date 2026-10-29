from tabela_m import tabela_M as M

class No:
	def __init__(self, simbolo):
		self.simbolo = simbolo
		self.token = None
		self.filhos = []

def error(msg, tokens, ip):
	cat, lex, linha = tokens[ip]
	raise SyntaxError(f"Erro sintático na linha {linha}: {msg})")

nao_terminais = {"PROG","CMDS","MAIS_CMDS","CMD","ID_CONT","VARS","MAIS_VAR",
                 "PFALSA","RESTO_IDENT","EXP_IDENT","CONDICAO","RELACAO",
                 "EXPRESSAO","TERMO","OP_UN","FATOR","OUTROS_TERMOS",
                 "OP_AD","MAIS_FATORES","OP_MUL"}

def sintaxe(w, tokens):
	raiz = No('PROG')
	pilha = [('$', None), ('PROG', raiz)]
	ip = 0
	a = w[ip]

	while pilha[-1][0] != '$':
		X, no = pilha[-1]

		if X not in nao_terminais:	           #Se x é terminal...
			if X == a:				           #Se casou...
				no.token = tokens[ip]
				pilha.pop()
				ip += 1
				a = w[ip]
			else:
				error(f"esperado '{X}', encontrado '{a}'", tokens, ip)
		else:
			producao = M.get((X,a))
			if producao is None:
				error(f"token '{a}' inesperado em {X}", tokens, ip)
			pilha.pop()
			no.filhos = [No(s) for s in producao]
			for f in reversed(no.filhos):
				pilha.append((f.simbolo, f))

	if a != '$':
		error("entrada sobrando", tokens, ip)

	return raiz
