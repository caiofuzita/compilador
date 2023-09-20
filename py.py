import re
#abrindo código para leitura
def open_input():
    input_txt = open('input.txt')
    return input_txt.readlines()

# tok1 - Operador
# tok 100 - :=
# tok 101 - /
# tok 102 - ^
# tok 103 - >>
# tok 104 - **
# tok 105 - <<
def is_operador(test):
    if(re.match(r':=', test)):
        return 100
    elif(re.match(r'\/', test)):
        return 101
    elif(re.match(r'\^', test)):
        return 102
    elif(re.match(r'>>', test)):
        return 103
    elif(re.match(r'\*\*', test)):
        return 104
    elif(re.match(r'<<', test)):
        return 105

# tok2 - Delimitador
# tok200 - :
# tok201 - ;
# tok202 - (
# tok203 - )
def is_delimitador(test):
    if(re.match(r':', test)):
        return 200
    elif(re.match(r';', test)):
        return 201
    elif(re.match(r'(', test)):
        return 202
    elif(re.match(r')', test)):
        return 203



# tok3 - Numero
# tok300 - Numero Inteiro
# tok301 - Numero Real

# tok4 - Palavra reservada
# tok400 - DEFINICOES
# tok401 - INICIO
# tok402 - FIM
# tok403 - LEIA
# tok405 - IF
# tok406 - ELSE
# tok407 - PRINT


def main():
    input_txt = open_input()
    line_number = 1
    for line in input_txt:
        words = line.split()
        for word in words:
            #print(word)
            if (is_delimitador(word)):
                print(f'line: {line_number} {word} {is_delimitador(word)}')
            if (is_operador(word)):
                print(f'line: {line_number} {word} {is_operador(word)}')
        line_number += 1

main()