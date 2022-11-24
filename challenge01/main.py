validUsers = 0
lastValidUsername = ""

# Un usuario válido tiene:
    # usr: nombre de usuario
    # eme: email
    # psw: contraseña
    # age: edad
    # loc: ubicación
    # fll: número de seguidores
def isValidUser(dic):
    return ( dic.get("usr") and dic.get("eme") and dic.get("psw") and dic.get("age") and dic.get("loc") and dic.get("fll") )

# Abrimos el fichero
with open("users.txt","r",) as f:
    lines = f.read()

# Separamos los usuarios por párrafo
users = lines.split('\n\n')

for i in range(len(users)):
    dic = {}
    user = users[i].split()
    for user in users[i].split():
        tag,value = (user.split(":"))
        dic[tag] = value
    if ( isValidUser(dic) ):
        validUsers += 1
        lastValidUsername = dic.get("usr")

print("El número de usuarios válidos es: " + str(validUsers))
print("El último usuario válido es: " + lastValidUsername)
print(str(validUsers) + lastValidUsername)