mecenas = [
    "Gorusuke",
    "DavidFabian",
    "ItziarZG",
    "edy WOLF",
    "MarcosGaPe",
    "Jose Jimenez",
    "Borja ",
    "Jhonathan Izquierdo Higuita",
    "MiLfeR322",
    "Sebastián Espínola",
    "Matias Luna",
    "Imanol Decima",
    "MarcoCasula",
    "MaríaBohórquez",
    "Renan",
    "IvanL'olivier",
    "Shonero",
    "Luichidev",
    "Faviola Narvaez",
    "Christopher Fuentes",
    "Kuro",
    "Juan Pablo Addeo",
    "Sergio Martínez",
    "Fran Enriquez González",
    "Diana",
    "tictools",
    "ConchaAsensio",
    "Emilio_Arreaza",
    "novamix",
    "Tomas Duclos",
    "Elaya",
    "Ignacio Palominos",
    "David C.",
    "Gerardo Felipe Conrado",
    "ElXuri",
    "David Borja Martinez",
    "JaviFelices",
    "CarlesSànchez",
    "Gorusuke",
    "DavidFabian",
    "ItziarZG",
    "edy WOLF",
    "MarcosGaPe",
    "Jose Jimenez",
    "Borja ",
    "Jhonathan Izquierdo Higuita",
    "MiLfeR322",
    "Sebastián Espínola",
    "Matias Luna",
    "Imanol Decima",
    "MarcoCasula",
    "MaríaBohórquez",
    "Renan",
    "IvanL'olivier",
    "Shonero",
    "Luichidev",
    "Faviola Narvaez",
    "Christopher Fuentes",
    "Kuro",
    "Juan Pablo Addeo",
    "Sergio Martínez",
    "Fran Enriquez González",
    "Diana",
    "tictools",
    "ConchaAsensio",
    "Emilio_Arreaza",
    "novamix",
    "Tomas Duclos",
    "Elaya",
    "Ignacio Palominos",
    "David C.",
    "Gerardo Felipe Conrado",
    "ElXuri",
    "David Borja Martinez",
    "JaviFelices",
    "CarlesSànchez",
    "Gorusuke",
    "DavidFabian",
    "ItziarZG",
    "edy WOLF",
    "MarcosGaPe",
    "Jose Jimenez",
    "Borja ",
    "Jhonathan Izquierdo Higuita",
    "MiLfeR322",
    "Sebastián Espínola",
    "Matias Luna",
    "Imanol Decima",
    "MarcoCasula",
    "MaríaBohórquez",
    "Renan",
    "IvanL'olivier",
    "Shonero",
    "Luichidev",
    "Faviola Narvaez",
    "Christopher Fuentes",
    "Kuro",
    "Juan Pablo Addeo",
    "Sergio Martínez",
    "Fran Enriquez González",
    "Diana",
    "tictools",
    "ConchaAsensio",
    "Emilio_Arreaza",
    "novamix",
    "Tomas Duclos",
    "Elaya",
    "Ignacio Palominos",
    "David C.",
    "Gerardo Felipe Conrado",
    "ElXuri",
    "David Borja Martinez",
    "JaviFelices",
    "CarlesSànchez"
]

def next(vivosMecenas):
    proxAtaque = -1
    for ataque in range(0, len(vivosMecenas), 1):
        if (vivosMecenas[ataque] == True):
            print(ataque)
            return ataque
    return proxAtaque

vivos = len(mecenas)

vivosMecenas = []


for i in range (0,len(mecenas),1):
    vivosMecenas.append(True)

indice = 0
ataque = indice + 1

# Mientras haya vivos
while (vivos > 1):
    indice = next(vivosMecenas)
    vivosMecenas[indice] = False
    ataque = next(vivosMecenas)
    vivosMecenas[indice] = True


    vivos = vivos - 1
    vivosMecenas[ataque] = False

            
                

print(vivosMecenas)

print("submit " + str(indice) + "-" + mecenas[indice])