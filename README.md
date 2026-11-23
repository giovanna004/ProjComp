# Compilador para um subconjunto de Ruby

Trabalho individual da disciplina de Projeto de Compiladores.
Compilador de um subconjunto da linguagem **Ruby**, com análise sintática **descendente não recursiva** (preditiva tabular, tabela M), que traduz o programa-fonte para o código objeto de uma **máquina hipotética** e o executa em uma máquina virtual.

- **Linguagem de implementação:** Python 3 (sem bibliotecas externas)
- **Autora:** Giovanna Queiroz Salvador

> Nenhuma biblioteca de geração de analisadores (lex, yacc, ply, etc.) nem o módulo `re` foram utilizados: o analisador léxico foi escrito à mão.

---

## Uso de Inteligência Artificial

Foi utilizada IA durante o desenvolvimento deste trabalho: **Claude (Anthropic)**, usado como apoio para tirar dúvidas, revisar trechos de código e auxiliar na escrita desta documentação.

---

## Requisitos

- Python 3.8 ou superior
- Nenhuma dependência para instalar

## Estrutura do projeto

| Arquivo | Função |
|---|---|
| `lexico.py` | Analisador léxico (gera a lista de tokens) |
| `tabela_m.py` | Tabela M do analisador preditivo (construída a partir de FIRST/FOLLOW) |
| `sintatico.py` | Analisador sintático descendente não recursivo (pilha explícita + tabela M), gera a árvore concreta |
| `conversor.py` | Converte a árvore concreta em uma árvore sintática abstrata (AST) |
| `semantico.py` | Analisador semântico: tabela de símbolos, endereços e verificação de declaração/uso |
| `tradutor.py` | Tradutor: gera o código objeto a partir da AST |
| `main.py` | **Parte 1** — compilador (lê o código-fonte, grava o `.obj`) |
| `maquina.py` | **Parte 2** — máquina virtual (lê o `.obj` e executa) |
| `gramatica.txt` | Gramática, conjuntos FIRST e FOLLOW |
| `codigo_objeto.txt` | Descrição das instruções da máquina hipotética |
| `entrada.txt` | Exemplo de programa de entrada |
| `arquivo.obj` | Exemplo de código objeto gerado |

## Como executar

### Parte 1 — Compilar (código-fonte → código objeto)

```bash
python main.py entrada.txt
```

Lê o programa em `entrada.txt` e grava o código objeto no arquivo de texto **`arquivo.obj`**.
Se houver erro léxico, sintático ou semântico, a mensagem é exibida com a linha (quando disponível) e nenhum código objeto é gerado.

### Parte 2 — Executar (código objeto → execução)

```bash
python maquina.py arquivo.obj
```

Lê `arquivo.obj` e executa as instruções na máquina virtual. As saídas do programa (`puts`) aparecem no terminal; entradas (`gets.to_f`) são lidas do teclado.

### Exemplo completo

`entrada.txt`:

```ruby
a, b;
a = 2;
if a > b then puts a else puts b end
```

```bash
python main.py entrada.txt
python maquina.py arquivo.obj
```

---

## Pipeline do compilador

```
entrada.txt ─► léxico ─► sintático (LL(1) tabular) ─► conversor (AST)
            ─► semântico (tabela de símbolos) ─► tradutor ─► arquivo.obj ─► maquina.py
```

1. **Léxico** (`lexico.py`): reconhece palavras reservadas (`puts if then else end while do`), identificadores, números reais, operadores (`+ - * / == != >= <= > < =`), delimitadores (`( ) , ;`) e `gets.to_f`.
2. **Sintático** (`sintatico.py` + `tabela_m.py`): análise preditiva com pilha explícita, sem recursão, guiada pela tabela M.
3. **Semântico** (`semantico.py`): detecta variável redeclarada e variável usada antes de ser declarada; atribui um endereço a cada variável.
4. **Tradutor** (`tradutor.py`): emite as instruções da máquina hipotética, com resolução dos endereços de desvio (`DSVF`/`DSVI`).
5. **Máquina virtual** (`maquina.py`): interpreta o código objeto sobre uma pilha de dados.

## Linguagem aceita (resumo da gramática)

```
PROG          -> CMDS
CMDS          -> CMD MAIS_CMDS | λ
MAIS_CMDS     -> ; CMDS | λ
CMD           -> puts id
               | id ID_CONT
               | if CONDICAO then CMDS PFALSA end
               | while CONDICAO do CMDS end
ID_CONT       -> MAIS_VAR | RESTO_IDENT
VARS          -> id MAIS_VAR
MAIS_VAR      -> , VARS | λ
PFALSA        -> else CMDS | λ
RESTO_IDENT   -> = EXP_IDENT
EXP_IDENT     -> EXPRESSAO | gets.to_f
CONDICAO      -> EXPRESSAO RELACAO EXPRESSAO
RELACAO       -> == | != | >= | <= | > | <
EXPRESSAO     -> TERMO OUTROS_TERMOS
TERMO         -> OP_UN FATOR MAIS_FATORES
OP_UN         -> - | λ
FATOR         -> id | numero_real | ( EXPRESSAO )
OUTROS_TERMOS -> OP_AD TERMO OUTROS_TERMOS | λ
OP_AD         -> + | -
MAIS_FATORES  -> OP_MUL FATOR MAIS_FATORES | λ
OP_MUL        -> * | /
```

Os conjuntos FIRST e FOLLOW completos estão em `gramatica.txt`. O símbolo `λ` representa a cadeia vazia.

**Observações sobre a linguagem:**
- Variáveis são declaradas por uma lista de identificadores, por exemplo `a, b, c;`, e todas têm um único tipo (real).
- Comandos são separados por `;`.

## Máquina hipotética (código objeto)

Instruções implementadas pela máquina virtual (detalhes em `codigo_objeto.txt`):

| Grupo | Instruções |
|---|---|
| Controle do programa | `INPP`, `PARA` |
| Memória | `ALME m`, `CRCT k`, `CRVL n`, `ARMZ n` |
| Aritméticas | `SOMA`, `SUBT`, `MULT`, `DIVI`, `INVE` |
| Comparações | `CPME` (<), `CPMA` (>), `CPIG` (==), `CDES` (!=), `CPMI` (<=), `CMAI` (>=) |
| Desvios | `DSVI p`, `DSVF p` |
| Entrada/Saída | `LEIT`, `IMPR` |

Exemplo de código objeto gerado (`arquivo.obj`) para um laço `while` que soma `5+4+3+2+1`:

```
INPP
ALME 1
ALME 1
CRCT 5
ARMZ 0
CRCT 0
ARMZ 1
CRVL 0
CRCT 0
CPMA
DSVF 20
...
PARA
```

---

## Referências

- AHO, Alfred V.; LAM, Monica S.; SETHI, Ravi; ULLMAN, Jeffrey D. **Compiladores: Princípios, Técnicas e Ferramentas** ("Livro do Dragão"). 2. ed. São Paulo: Pearson, 2008.
- Canal do YouTube **Wilson Castello** — videoaulas de compiladores: <https://www.youtube.com/@wilsoncastello>
- Slides e vídeo da disciplina de Compiladores (material do professor).
