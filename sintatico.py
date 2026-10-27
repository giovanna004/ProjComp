from tabela_m import tabela_M as M

class No:
	def __init__(self, simbolo):
		self.simbolo = simbolo
		self.token = None
		self.filhos = []

def error(msg, tokens, ip):
	cat, lex, linha, pos = tokens[ip]
	raise SyntaxError(f"Erro sintático na linha {linha}: {msg} (token '{lex}')")

nao_terminais = {"PROG","CMDS","MAIS_CMDS","CMD","ID_CONT","VARS","MAIS_VAR",
                 "PFALSA","RESTO_IDENT","EXP_IDENT","CONDICAO","RELACAO",
                 "EXPRESSAO","TERMO","OP_UN","FATOR","OUTROS_TERMOS",
                 "OP_AD","MAIS_FATORES","OP_MUL"}

def analisa(w, tokens):
	raiz = No('PROG')
	pilha = [('$', None), ('PROG', raiz)]
	ip = 0
	a = w[ip]
	X = pilha[-1]

	while X != '$':
		if X not in nao_terminais:
			if X == a:
				if no: no.token = tokens[ip]
				pilha.pop()
				ip += 1
				a = w[ip]
			else:
				error(f"esperado '{X}', encontrado '{a}'", tokens, ip)
		else:
			producao = M.get((X,a))
			no.filhos = [No(s) for s in producao]
			for f in reversed(no.filhos):
				pilha.append((f.simbolo, f))
			if producao is None:
				error(f"token '{a}' inesperado em {X}", tokens, ip)
			print(X, "->", " ".join(producao) or "ε")
			pilha.pop()
			for simbolo in reversed(producao):
				pilha.append(simbolo)
		X = pilha[-1]

	if a != '$':
		error("entrada sobrando", tokens, ip)
	print("Aceito")

	return raiz
