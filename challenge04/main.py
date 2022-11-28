# Password está entre los números 11098 y 98123
    # Es una contraseña de 5 dígitos.
    # La contraseña tenía el número 5 repetido como mínimo dos veces.
    # El número a la derecha siempre es mayor o igual que el que tiene a la izquierda.

inicio = 11098
fin = 98123

validPasswords = []

for password in range(inicio+1, fin+1, 1):
    fives = 0
    valid = False
    # Comprobamos que es de 5 dígitos
    if (len(str(password)) == 5):
        # Contar el número de cincos
        for number in str(password):
            if (number == "5"):
                fives += 1
        if (fives >= 2):
            valid = True
            # Comprobar si el número de la derecha siempre es mayor o igual al de la izquierda
            for i in range (0,len(str(password))-1,1):
                if (not((str(password)[i+1] >= str(password)[i]))):
                    valid = False
    
            if (valid):
                validPasswords.append(password)

print(str(len(validPasswords)) + "-" + str(validPasswords[55]))