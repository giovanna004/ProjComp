RESERVADAS = {"puts","if","then","else","end","while","do"}

def lexica(entrada):
    tokens = []
    i = 0
    linha = 1
    n = len(entrada)
    while i < n:
        c = entrada[i]
        if c == '\n' : linha += 1; i += 1
        elif c in ' \t\r' : i += 1
        elif c.isdigit():
            inicio = i
            while i < n and entrada[i].isdigit(): i += 1
            if i + 1 < n and entrada[i] == '.' and entrada[i+1].isdigit():
                i += 1
                while i < n and entrada[i].isdigit(): i += 1
            tokens.append(("numero_real", entrada[inicio:i], linha))
        elif c.isalpha() or c == '_' :
            inicio = i
            while i < n and (entrada[i].isalnum() or entrada[i] == '_'): i += 1
            lex = entrada[inicio:i]
            if lex == "gets" and entrada.startswith(".to_f", i):
                i += 5
                tokens.append(("gets.to_f", "gets.to_f", linha))
            elif lex in RESERVADAS:
                tokens.append((lex, lex, linha))
            else:
                tokens.append(("id", lex, linha))
        elif c in "=!<>":
            if i + 1 < n and entrada[i + 1] == '=':
                tokens.append((c+"=", c+"=", linha)); i += 2
            elif c == '!':
                raise SyntaxError(f"Linha {linha}: '!' isolado")
            else:
                tokens.append((c, c, linha)); i += 1
        elif c in "+-=*/(),;":
            tokens.append((c, c, linha)); i += 1
        else: 
            raise SyntaxError(f"Linha {linha}: carcatere inválido '{c}'")
    tokens.append(("$", "$", linha))
    return tokens
                        
