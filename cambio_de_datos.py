def Is_string_or_number(matrizCasosTest):
"""prepara los datos para entregarlos a la capa de lógica """
    matrizCasosTestLogic = []
    position = 0
    for string in matrizCasosTest:
        try:
        	string = string.replace(" ","")
            change = int(string)
            matrizCasosTestLogic.append(change)
            position += 1
        except:
            matrizCasosTestLogic.append(string)
            position += 1
            continue
        else:
            pass
   
   
    return matrizCasosTestLogic