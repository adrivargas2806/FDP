import random

# Lista equipos locales 
equi_locales = ["Atlético Nacional", "Independiente Medellín", "Deportivo Cali", "América de Cali", "Millonarios", "Santa Fe", "Junior", "Once Caldas"]

# Lista equipos visitantes 
equi_visitantes = ["Atlético Nacional", "Independiente Medellín", "Deportivo Cali", "América de Cali", "Millonarios", "Santa Fe", "Junior", "Once Caldas"]

# Lista Goles Equipo local 
goles_equi_locales = []
for i in range(240):
    goles_equi_locales.append(random.randint(0, 5))

# Lista Goles Equipo Visitante 
goles_equi_visitantes = []
for i in range(240):
    goles_equi_visitantes.append(random.randint(0, 3))

# Calcular numero de partidos 
partidos_jugados = 0
for equipo in equi_locales:
    partidos_jugados += 30
print("Número total de partidos jugados:", partidos_jugados)

# Crear lista de resultados
resultados = []
for i in range(len(goles_equi_locales)):
    resultados.append((goles_equi_locales[i], goles_equi_visitantes[i]))

# Calcular cantidad de partidos por equipo
partidos_jugados_equipo = {}
for equipo in equi_locales:
    partidos_jugados_equipo[equipo] = 0

for i in range(len(resultados)):
    equipo_local = equi_locales[i % len(equi_locales)]
    equipo_visitante = equi_visitantes[i % len(equi_visitantes)]

    partidos_jugados_equipo[equipo_local] += 1
    partidos_jugados_equipo[equipo_visitante] += 1

# Calcular cantidad de partidos ganados, perdidos y empatados por equipo
partidos_ganados = {}
partidos_perdidos = {}
partidos_empatados = {}
for equipo in equi_locales:
    partidos_ganados[equipo] = 0
    partidos_perdidos[equipo] = 0
    partidos_empatados[equipo] = 0

for i in range(len(resultados)):
    goles_local, goles_visitante = resultados[i]
    equipo_local = equi_locales[i % len(equi_locales)]
    equipo_visitante = equi_visitantes[i % len(equi_visitantes)]

    if goles_local > goles_visitante:
        partidos_ganados[equipo_local] += 1
        partidos_perdidos[equipo_visitante] += 1
    elif goles_visitante > goles_local:
        partidos_ganados[equipo_visitante] += 1
        partidos_perdidos[equipo_local] += 1
    else:
        partidos_empatados[equipo_local] += 1
        partidos_empatados[equipo_visitante] += 1

# Imprimir cantidad de partidos jugados, ganados, perdidos y empatados por equipo
for equipo in equi_locales:
    print(f"El equipo {equipo} jugó {partidos_jugados_equipo[equipo]} partidos, ganó {partidos_ganados[equipo]}, empató {partidos_empatados[equipo]}")

