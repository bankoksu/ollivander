def Is_string_or_number(matrizCasosTest):
    """prepara los datos para entregarlos a la capa de lógica """
    matrizCasosTestLogic = []
    position = 0
    for string in matrizCasosTest:
        if position > 1:
            string = string.replace(" ","")
            position +=1
        else:
            position +=1
            pass
            
    for string in matrizCasosTest:
        try:
            if int(string) >=0 or int(string)<0: 
                change = int(string)
                matrizCasosTestLogic.append(change)
        except:
            matrizCasosTestLogic.append(string)
            continue
        else:
            pass
    
   
    return matrizCasosTestLogic
    
lista =[("pajaro"," 5"," -10"),("leon"," 0"," 9"),("no se tu"," -10"," 0")]

for datos in lista:
    print(Is_string_or_number(datos))

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
    
lista =[("pajaro"," 5"," -10"),("leon"," 0"," 9"),("no se tu"," -10"," 0")]

for datos in lista:
    print(Is_string_or_number(datos))





			

lista = ["hola"," 5","-10"]

for string in lista:
    #print(string)
    
    try:
        change = int(string)
        lista[position]=change
        #print(string)
        position += 1
    except:
        "no puedo transformarlo en string"
        print(string)
        position += 1
    else:
        #print(lista)

        Python 3.6
1	lista = ["hola"," 5","-10"]
2	position = 0
3	for string in lista:
4	    try:
5	        change = int(string)
6	        lista[position]=change
7	        
8	        position += 1
9	    except:
10	        "no puedo transformarlo en string"
11	        
12	        position += 1
13	    else:
14	        pass
15	
16	print (lista)