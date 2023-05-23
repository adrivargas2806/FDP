# Lista equipos locales 


equi_locales = ["Atlético Nacional", "Independiente Medellín", "Deportivo Cali", "América de Cali", "Millonarios", "Santa Fe", "Junior", "Once Caldas"]

#lista equipos visitantes 
equi_visitantes = ["atletico bucaramanga","deportivo pereira","union magdalena","envigado FC","Atletico huila","la equidad", "jaguares de cordoba"," Alianza Petrolera "]

# lista equipos locales 2 
equi_locales2=  ["atletico bucaramanga","deportivo pereira","union magdalena","envigado FC","Atletico huila","la equidad", "jaguares de cordoba"," Alianza Petrolera "]

#lista equipos visitantes 2 
equi_visitantes2=["Atlético Nacional", "Independiente Medellín", "Deportivo Cali", "América de Cali", "Millonarios", "Santa Fe", "Junior", "Once Caldas"]

#•	Lista Goles Equipo local 
goles_equi_locales = []
for i in range(16):
    import random
    goles_equi_locales.append (random.randint(0, 5))

# Imprimir la lista de goles del equipo local
print(goles_equi_locales)

#•	Lista Goles Equipo Visitante 
goles_equi_visitantes = []
for i in range(16):
    import random
    goles_equi_visitantes.append (random.randint(0, 5))
 
 # calcular numero de partidos 
partidos_jugados = 0
for equipo in equi_locales + equi_visitantes:
    partidos_jugados += 2
print("Número total de partidos jugados:", partidos_jugados)

# Crear lista de resultados
resultados = []
for i in range(len(goles_equi_locales)):
    resultados.append((goles_equi_locales[i], goles_equi_visitantes[i]))


    # Calcular cantidad de partidos ganados y perdidos por equipo
partidos_ganados = {}
partidos_perdidos = {}
for equipo in equi_locales + equi_visitantes:
    partidos_ganados[equipo] = 0
    partidos_perdidos[equipo] = 0

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

# Imprimir cantidad de partidos ganados y perdidos por equipo
for equipo in equi_locales: 
    print ("El equipo " + equipo + " ganó " + str(partidos_ganados[equipo]) + " y perdió " + str(partidos_perdidos[equipo]))

# Imprimir cantidad de partidos ganados y perdidos por equipo
for equipo in equi_visitantes: 
   print ("El equipo " + equipo + " ganó " + str(partidos_ganados[equipo]) + " y perdió " + str(partidos_perdidos[equipo]))



