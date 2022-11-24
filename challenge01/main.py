f = open("users.txt","r",)
lines = f.readlines()
validUsers = 0

for i in range(len(lines)):
    dic = {}
    for line in lines[i].split():
        tag,value = (line.split(":"))
        dic[tag] = value
    # Comprobamos si tiene todos los campos
        # Los datos necesarios son
            # usr: nombre de usuario
            # eme: email
            # psw: contraseña
            # age: edad
            # loc: ubicación
            # fll: número de seguidores
    if (dic.get("usr") and dic.get("eme") and dic.get("psw") and dic.get("age") and dic.get("loc") and dic.get("fll")):
        validUsers += 1
        lastValidUsername = dic.get("usr")

print("El número de usuarios válidos es: " + str(validUsers))
print("El último usuario válido es: " + lastValidUsername)