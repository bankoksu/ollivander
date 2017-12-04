def Is_string_or_number(lista):
    lista_conver = []
    position = 0
    for string in lista:
        try:
            string = string.replace(" ","")
            change = int(string)
            lista_conver.append(string)
        
            position += 1
        except:
            lista_conver.append(string)
            position += 1
            continue
        else:
            pass
   
   
    return lista_conver