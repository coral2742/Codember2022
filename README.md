# Codember 2022
![image](https://github.com/coral2742/Codember2022/blob/5a8c57a7f70f56160c5a07fd97ab5b60478273f8/Codember2022.png)

[Codember.dev](https://codember.dev/) es una página web creada por [Midudev](https://github.com/midudev) en la que cada semana durante el mes de Noviembre se publican retos de programación con un ranking. Además, hay comandos ocultos en la web que se pueden descubrir superando pequeños retos.

En este repositorio se encuentran mis soluciones a estos retos realizados con Python🐍.

## 🐦 Challenge 01: ¡Arregla Twitter!
| [Ver mi solución](https://github.com/coral2742/Codember2022/tree/main/challenge01) |
| ---------------- |

Twitter ha sido comprado y quieren eliminar los bots. Te han pedido ayuda para detectar el número de usuarios en su base de datos que tienen datos corruptos.

La base de datos es muy antigua y está en un formato extraño. Los perfiles requieren tener los siguientes datos:

- usr: nombre de usuario
- eme: email
- psw: contraseña
- age: edad
- loc: ubicación
- fll: número de seguidores

Todo está en un fichero donde los datos de usuario son una secuencia de pares key:value, que pueden estar en la misma línea o separado por líneas, y cada usuario está separado por un salto de línea. ¡Ojo porque puede estar todo desordenado!

## 🕵️ Challenge 02: ¡Atrapa a esos ciber criminales!
| [Ver mi solución](https://github.com/coral2742/Codember2022/tree/main/challenge02) |
| ---------------- |

Un grupo de ciber criminales están usando mensajes encriptados para comunicarse. El FBI nos ha pedido ayuda para descifrarlos.

Los mensajes son cadenas de texto que incluyen números enteros muy largos y espacios en blanco. Aunque los números no parecen tener sentido... una chica llamada Alice ha descubierto que podrían usar el código ASCII de las letras en minúscula.

## 🦓 Challenge 03: La zebra de colores
| [Ver mi solución](https://github.com/coral2742/Codember2022/tree/main/challenge03) |
| ---------------- |

TMChein ya se está preparando para las fiestas y quiere empezar a decorar la casa con las luces de navidad.

Quiere comprar una pero sus favoritas son las que tienen dos colores que se van alternando. Como una zebra de dos colores.

Ha hecho que las luces sean Arrays y cada posición un color. Y quiere saber qué luces tienen las zebras más largas y cuál es el último color de esa sucesión de colores.

Recuerda que una zebra de colores es cuando dos colores se alternan una y otra vez. Si se repite un color en la posición siguiente o es un tercer color, entonces se deja de contar. Lo que queremos calcular es la tira de colores más larga en forma de zebra y el último color de esa tira de colores.

## 🪙 Challenge 04: Encuentra la contraseña de tu amigo
| [Ver mi solución](https://github.com/coral2742/Codember2022/tree/main/challenge04) |
| ---------------- |

Un amigo compró 5 BitCoins en 2008. El problema es que lo tenía en un monedero digital... ¡y no se acuerda de la contraseña!

Nos ha pedido ayuda. Y nos ha dado algunas pistas:

- Es una contraseña de 5 dígitos.
- La contraseña tenía el número 5 repetido como mínimo dos veces.
- El número a la derecha siempre es mayor o igual que el que tiene a la izquierda.

Dice que el password está entre los números 11098 y 98123. ¿Le podemos decir cuantos números cumplen esas reglas dentro de ese rango?

## ⚔️ Challenge 05: Battle Royale de frameworks y bibliotecas
| [Ver mi solución](https://github.com/coral2742/Codember2022/tree/main/challenge05) |
| ---------------- |

Hay tanto framework y biblioteca que ya no sabemos qué usar. Así que un comité ha decidido hacer una especie de Los Juegos del Hambre para decidir qué tecnología se queda.

Ha puesto todas las tecnologías en círculo de forma aleatoria. La tecnología en el índice 0 empieza matando a la que tiene justo a la derecha (índice + 1).

El siguiente turno es para la tecnología que esté viva que queda a la derecha de la que se acaba de morir. Y así sucesivamente hasta que sólo quede una. Mira este ejemplo de un grupo de 10 tecnologías, paso a paso:


         5
      6     4
   7           3
   8           2
      9     1
         0

0 mata a 1
2 mata a 3
4 mata a 5
6 mata a 7
8 mata a 9

         X
     6      4
   X           X
   8           2
      X     X
         0

0 mata a 2
4 mata a 6
8 mata a 0

         X
     X      4
   X           X
   8           X
      X     X
         X

4 mata a 8

         X
     X      4
   X           X
   X           X
      X     X
         X
La tecnología en el índice 4 es la que ha sobrevivido.

Ahora, para probar que somos capaces de crear un algoritmo que funcione, tenemos la lista de mecenas de la comunidad de midudev: https://codember.dev/mecenas.json

Tienes que crear un algoritmo que nos diga qué usuario sobreviviría usando el mismo sistema.