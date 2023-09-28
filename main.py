import re

#abrindo arquivo de entrada
def open_input():
    arquivo =  open('input.txt', 'r')
    return arquivo.readlines()

def save(entrada, nome_saida):
    file = open(nome_saida, 'w')
    for linha in entrada:
        file.write(linha)

### TOKENS ###

# tok1 - Operador
# tok 100 - :=
# tok 101 - /
# tok 102 - ^
# tok 103 - >>
# tok 104 - **
# tok 105 - <<
# tok 106 - +
# tok 107 - -
def is_operador(test): #conta apenas 1 dígito
    if (re.match(r'^:=$', test)):
        return 100
    elif (re.match(r'^\/$', test)):
        return 101
    elif (re.match(r'^\^$', test)):
        return 102
    elif (re.match(r'^>>$', test)):
        return 103
    elif (re.match(r'^\*\*$', test)):
        return 104
    elif (re.match(r'^<<$', test)):
        return 105
    elif (re.match(r'^\+$', test)):
        return 106
    elif (re.match(r'^-$', test)):
        return 107

# tok2 - Delimitador
# tok200 - :
# tok201 - ;
# tok202 - (
# tok203 - )
def is_delimitador(test):
    if (re.match(r'^:$',test)):
        return 200
    elif (re.match(r'^;$',test)):
        return 201
    elif (re.match(r'^\($',test)):
        return 202
    elif (re.match(r'^\)$',test)):
        return 203

# tok3 - Numero
# tok300 - Numero Inteiro
# tok301 - Numero Real
def is_numbero(test):
    if (re.match(r'\d', test)): #verifica se tem número
        if(not(re.match(r'\D', test))): #verifica se tem algo além de número
            return 300
        elif (re.match(r'\b-?\d+\.\d+\b', test)): # verifica se é um ponto
            return 301
        
# tok4 - Palavra reservada
# tok400 - DEFINICOES
# tok401 - INICIO
# tok402 - FIM
# tok403 - LEIA
# tok404 - IF
# tok405 - ELSE
# tok406 - PRINT
def is_reservada(test):
    if (re.match(r'[^"]', test)): #verifica se não é uma string
        if (re.match(r'DEFINICOES', test)):
            return 400
        elif (re.match(r'^INICIO', test)):
            return 401
        elif (re.match(r'^FIM', test)):
            return 402
        elif (re.match(r'^LEIA', test)):
            return 403
        elif (re.match(r'^IF', test)):
            return 404
        elif (re.match(r'^ELSE', test)):
            return 405
        elif (re.match(r'^PRINT', test)):
            return 406

# tok5 erros
# tok500 - nome de variável não começa com var + tipo + nome
# tok501 - nome tem mais que 12 dígitos
# tok502 - caracteres especiais
# tok503 - operador matemático primário com mais de 1 dígito
# tok504 - operadores secundários que precisam ser 
# tok505 - palavras reservadas 
# tok506 - falta de abertura de parênteses
# tok507 - falta de fechamento de parênteses
def is_erro(test):
    output = []
    new_str = test.replace("\n", "")
    
    if (re.search(r":=", new_str)): #testa é uma variável
        if (not(re.match(r'^varINT|^varFLT|^varSTR', new_str))): #testa se está inicializada de forma correta
            output.append(f'{new_str} -> 500')

        if(len(new_str.split(' := ')[0]) > 12): #testa se é maior que 12 caracteres
            output.append(f'{new_str} -> 501')

        name_variable = new_str.split(' := ')[0] #pega apenas o nome da variável
        if (re.match('\W\D', name_variable)): #compara se tem algum caractere não número e não letra
            output.append(f'{new_str} -> 502')
    

    if (re.match(r'\+\+.*|\/\/.*|--.*|\^\^.*', new_str)): #pega símbolos duplicados
        output.append(f'{new_str} -> 503')
    
    if (re.match(r'=|<|>|&|\|', new_str)): #verifica se utiliza caracteres de operação
        if(not(re.match(r'==|<<|>>|&&|\|\|', new_str))):
            output.append(f'{new_str} -> 504')

    if (re.match(r'(?i)definicoes|inicio|fim|leia|if|else|print', new_str)):
        if(not(re.match(r'DEFINICOES|INICIO|FIM|LEIA|IF|ELSE|PRINT', new_str))):
            output.append(f'{new_str} -> 505')

    #parenteses
    contador_1 = 0
    contador_2 = 0
    for letter in new_str:
        if (re.match('\(', letter)):
            contador_1 += 1
            print(contador_1)
        elif (re.match('\)', letter)):
            contador_2 += 1
            print(contador_2)
    if (contador_1 > contador_2):
        output.append(f'{new_str} -> 507')
    elif (contador_1 < contador_2):
        output.append(f'{new_str} -> 506')
        
    return output

#
def matching_brackets(s):
    stack = []
    open_brackets = ["("]
    close_brackets = [")"]
    for i in s:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            pos = close_brackets.index(i)
            if ((len(stack) > 0) and
                (open_brackets[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

def main():
    input_txt = open_input()
    line_number = 1
    output_txt = []
    error_log = []

    for line in input_txt:

        words = line.split()

        for word in words:
            
            if(is_operador(word)):
                output_txt.append(f'line {line_number} {word} -> {is_operador(word)}\n')
            
            if(is_delimitador(word)):
                output_txt.append(f'line {line_number} {word} -> {is_delimitador(word)}\n')

            if(is_numbero(word)):
                output_txt.append(f'line {line_number} {word} -> {is_numbero(word)}\n')

            if(is_reservada(word)):
                output_txt.append(f'line {line_number} {word} -> {is_reservada(word)}\n')

        #print(line)
        if(is_erro(line)):
            error_log.append(f'line {line_number} {is_erro(line)}\n')

        line_number += 1

    save(output_txt, 'output.txt')
    save(error_log, 'error_log.txt')

    

main()