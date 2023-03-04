# O nome dos patinhos são: Jack, Kack, Lack, Mack, Nack, Ouack, Pack e Quack. Vamos escrever um programa (com Test Case) em que a função receba os prefixos 'JKLMNOPQ' e adicione o sufixo correto.

duckNames = "JKLMNOPQ"

def addNameSuffix(duckNames):
    duckFullNameList = ""
    for duckName in duckNames:
        if(duckName != "O" and duckName != "Q" and duckName != "P"):
            duckFullName = duckName + "ack"
            duckFullNameList += duckFullName + ", "
        elif(duckName == "P"):
            duckFullName = duckName + "ack"
            duckFullNameList += duckFullName + " e "
        elif(duckName == "Q"):
            duckFullName = duckName + "uack"
            duckFullNameList += duckFullName + "."
        else:
            duckFullName = duckName + "uack"
            duckFullNameList += duckFullName + ", "
    return duckFullNameList

duckFullNameList = addNameSuffix(duckNames)

print(addNameSuffix(duckNames))