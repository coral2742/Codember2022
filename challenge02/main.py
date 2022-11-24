import re

def traduce (wordinASCII):
    word = wordinASCII
    # Puede haber dos casos:
        # ASCII formado por dos dígitos
            # a -> 97
            # b -> 98
            # c -> 99
        # ASCII formado por tres dígitos
    result = ""
    while (word != ""):
        # Comprobamos que empieza por 9
        if (word[:1] == "9"):
            # Separar los dos primeros
            result += chr(int(word[:2]))
            #print(chr(int(word[:2])))
            word = word[2:]
        else:
            # Separar los tres primeros
            #print(chr(int(word[:3])))
            result += chr(int(word[:3]))
            #print(chr(int(word[:3])))
            word = word[3:]
    return result

finalMessage = ""

with open("encrypted.txt", "r") as f:
    file = f.readlines()

for line in range (len(file)):
    message  = (file[line].split())
    for word in message:
        finalMessage += traduce(word) + " "

print(finalMessage)