# O nome dos patinhos são: Jack, Kack, Lack, Mack, Nack, Ouack, Pack e Quack. Vamos escrever um programa (com Test Case) em que a função receba os prefixos 'JKLMNOPQ' e adicione o sufixo correto.

letters = "JKLMNOPQ"

# Primeiro resolução: utilizando If-Else
# def add_suffix_for_ducks_names(letters):
#     duck_name = ""
#     ducks_names_list = ""

#     for letter in letters:
#         if(letter != "O" and letter != "Q" and letter != "P"):
#             duck_name = letter + "ack"
#             ducks_names_list += duck_name + ", "
#         elif(letter == "P"):
#             duck_name = letter + "ack"
#             ducks_names_list += duck_name + " e "
#         elif(letter == "Q"):
#             duck_name = letter + "uack"
#             ducks_names_list += duck_name + "."
#         else:
#             duck_name = letter + "uack"
#             ducks_names_list += duck_name + ", "
#     return ducks_names_list

# Segunda resolução: utilizando Match-Case
def add_suffix_for_ducks_names(letters): 
    duck_name = ""
    ducks_names_list = ""
    for letter in letters:
        match letter:
            case "O":
                duck_name = letter + "uack"
                ducks_names_list += duck_name + ", "
            case "P":
                duck_name = letter + "ack"
                ducks_names_list += duck_name + " e "
            case "Q":
                duck_name = letter + "uack"
                ducks_names_list += duck_name + "."
            case other:
                duck_name = letter + "ack"
                ducks_names_list += duck_name + ", "
    return ducks_names_list


print(add_suffix_for_ducks_names(letters))