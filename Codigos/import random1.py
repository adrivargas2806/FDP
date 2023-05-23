import random

# Crear lista con los equipos de la liga colombiana
equipos = ["América de Cali", "Atlético Bucaramanga", "Atlético Huila", "Atlético Nacional", "Boyacá Chicó", "Deportes Quindío", 
           "Deportivo Cali", "Deportivo Pasto", "Deportivo Pereira", "Envigado FC", "Independiente Medellín", "Jaguares de Córdoba",
           "Junior FC", "La Equidad", "Millonarios FC", "Once Caldas"]

# Crear listas vacías para los equipos locales, visitantes y goles
equipos_locales = []
equipos_visitantes = []
goles_locales = []
goles_visitantes = []

# Generar datos para el juego del partido
for i in range(len(equipos)):
    for j in range(len(equipos)):
        if i != j:  # Los equipos deben ser diferentes 
            equipos_locales.append(equipos[i])
            equipos_visitantes.append(equipos[j])
            goles_locales.append(random.randint(0, 5)) #Los goles son marcados aleatoriamente entre 0 y 5
            goles_visitantes.append(random.randint(0, 5))

# Crear diccionario para almacenar los datos de cada equipo
datos_equipos = {}
for equipo in equipos:
    datos_equipos[equipo] = [0, 0, 0, 0]  # Partidos jugados, ganados, perdidos, empatados

# Actualizar los datos de cada equipo según los resultados de los partidos
for i in range(len(equipos_locales)):
    equipo_local = equipos_locales[i]
    equipo_visitante = equipos_visitantes[i]
    goles_local = goles_locales[i]
    goles_visitante = goles_visitantes[i]
    
    datos_equipos[equipo_local][0] += 1  # Sumar uno al número de partidos jugados
    datos_equipos[equipo_visitante][0] += 1
    
    if goles_local > goles_visitante:
        datos_equipos[equipo_local][1] += 1  # Sumar uno al número de partidos ganados
        datos_equipos[equipo_visitante][2] += 1  # Sumar uno al número de partidos perdidos
    elif goles_local < goles_visitante:
        datos_equipos[equipo_local][2] += 1  # Sumar uno al número de partidos perdidos
        datos_equipos[equipo_visitante][1] += 1  # Sumar uno al número de partidos ganados
    else:
        datos_equipos[equipo_local][3] += 1  # Sumar uno al número de partidos empatados
        datos_equipos[equipo_visitante][3] += 1

# Imprimir los datos de cada equipo
print("IMPRIMIR PARTIDOS JUGADOS, GANADOS, PERDIDOS Y EMPATADOS")
for equipo, datos in datos_equipos.items():
    partidos_jugados, partidos_ganados, partidos_perdidos, partidos_empatados = datos
    print(f"{equipo}: {partidos_jugados} partidos jugados, {partidos_ganados} partidos ganados, {partidos_perdidos} partidos perdidos, {partidos_empatados} partidos empatados")

# Calcular la cantidad de goles de los equipos locales
goles_locales_totales = {}
for equipo in equipos:
    goles_locales_totales[equipo] = sum([goles_locales[i] for i in range(len(equipos_locales)) if equipos_locales[i] == equipo])

# Imprimir la cantidad de goles de los equipos locales
print("IMPRIMIR LA CANTIDAD DE GOLES LOCALES")
for equipo, goles in goles_locales_totales.items():
    print(f"{equipo}: {goles} goles como locales")

# Calcular la cantidad de goles de los equipos visitantes
goles_visitantes_totales = {}
for equipo in equipos:
    goles_visitantes_totales[equipo] = sum([goles_visitantes[i] for i in range(len(equipos_visitantes)) if equipos_visitantes[i] == equipo])

# Imprimir la cantidad de goles de los equipos visitantes
print("IMPRIMIR LA CANTIDAD DE GOLES VISITANTES")
for equipo, goles in goles_visitantes_totales.items():
    print(f"{equipo}: {goles} goles como visitantes")

# Gráficas
import matplotlib.pyplot as plt

# Graficar la cantidad de goles de los equipos locales
plt.bar(list(goles_locales_totales.keys()), list(goles_locales_totales.values()))
plt.title("Cantidad de goles de los equipos locales")
plt.xlabel("Equipos")
plt.ylabel("Goles")
plt.show()

# Graficar la cantidad de goles de los equipos visitantes
plt.bar(list(goles_visitantes_totales.keys()), list(goles_visitantes_totales.values()))
plt.title("Cantidad de goles de los equipos visitantes")
plt.xlabel("Equipos")
plt.ylabel("Goles")
plt.show()

# cantidad total de goles 
print("IMRPIRMI LA CANTIDAD TOTAL DE GOLES")
cantidad_total_goles = sum(goles_locales) + sum(goles_visitantes)
print("Cantidad total de goles:", cantidad_total_goles)
 
#Calcular la cantidad TOTAL de partidos por equipo
print("IMPRIMIR LA CANTIDAD TOTAL DE PARTIDOS")
for equipo, datos in datos_equipos.items():
    partidos_jugados = datos[0]
    print(f"{equipo}: {partidos_jugados} partidos jugados")

#Listado de los equipos con sus goles de local y de visitante
print("IMPRIMIR LISTADO DE EQUIPOS CON SUS GOLES COMO LOCALES Y VISITANTES")
print("Equipo\t\tGoles locales\tGoles visitantes")
for equipo in equipos:
    goles_locales_equipo = goles_locales_totales[equipo]
    goles_visitantes_equipo = goles_visitantes_totales[equipo]
    print(f"{equipo}\t\t{goles_locales_equipo}\t\t{goles_visitantes_equipo}")

# Equipo que más goles realizó

# Crear un diccionario vacío para almacenar el número total de goles de cada equipo
goles_equipo = {}

# Sumar los goles de locales y de visitantes para cada equipo
for equipo in equipos:
    goles_locales_equipo = goles_locales_totales[equipo]
    goles_visitantes_equipo = goles_visitantes_totales[equipo]
    goles_totales = goles_locales_equipo + goles_visitantes_equipo
    goles_equipo[equipo] = goles_totales
    

# Encontrar el equipo con más goles en total y el equipo con menos goles en total
# Calcular cuál fue el equipo que más y menos goles realizó en TOTAL
# Crear un diccionario vacío para almacenar el número total de goles de cada equipo
goles_equipo = {}

# Encontrar el equipo con más goles en total y el equipo con menos goles en total
mas_goles_equipo = ""
menos_goles_equipo = ""

for equipo in goles_equipo:
    if mas_goles_equipo == "":
        mas_goles_equipo = equipo
        menos_goles_equipo = equipo
    elif goles_equipo[equipo] > goles_equipo[mas_goles_equipo]:
        mas_goles_equipo = equipo
    elif goles_equipo[equipo] < goles_equipo[menos_goles_equipo]:
        menos_goles_equipo = equipo

print("EQUIPOS CON MÁS Y MENOS GOLES EN TOTAL")

# Imprimir el equipo con más goles en total y el equipo con menos goles en total
if mas_goles_equipo != "":
    print("Equipo con más goles en total:", mas_goles_equipo, "con", goles_equipo[mas_goles_equipo], "goles")
if menos_goles_equipo != "":
    print("Equipo con menos goles en total:", menos_goles_equipo, "con", goles_equipo[menos_goles_equipo], "goles")

#Lea por teclado el nombre del equipo y liste los partidos en lo que ha participado y sus marcadores

# Leer el nombre del equipo ingresado por el usuario
equipo_usuario = input("Ingrese el nombre del equipo: ")

# Buscar los partidos en los que ha participado el equipo
partidos_equipo = []
for i in range(len(equipos_locales)):
    if equipos_locales[i] == equipo_usuario or equipos_visitantes[i] == equipo_usuario:
        partidos_equipo.append(i)

# Mostrar los marcadores de los partidos en los que ha participado el equipo
if len(partidos_equipo) == 0:
    print("El equipo no ha participado en ningún partido")
else:
    print(f"El equipo ha participado en {len(partidos_equipo)} partidos:")
    for partido in partidos_equipo:
        equipo_local = equipos_locales[partido]
        equipo_visitante = equipos_visitantes[partido]
        goles_local = goles_locales[partido]
        goles_visitante = goles_visitantes[partido]
        if equipo_local == equipo_usuario:
            print(f"{equipo_local} {goles_local} - {goles_visitante} {equipo_visitante}")
        else:
            print(f"{equipo_visitante} {goles_visitante} - {goles_local} {equipo_local}")

# Arme la tabla de posiciones y cree una nueva lista con los puntos por equipo

puntos_equipos = []
for equipo in equipos:
    puntos = datos_equipos[equipo][1]*3 + datos_equipos[equipo][3]  # Calcular los puntos según el número de partidos ganados y empatados
    puntos_equipos.append((equipo, puntos))  # Añadir el equipo y sus puntos a la lista

puntos_equipos.sort(key=lambda x: x[1], reverse=True)  # Ordenar la lista de mayor a menor cantidad de puntos
