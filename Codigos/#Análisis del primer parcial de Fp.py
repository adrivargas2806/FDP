#Análisis del primer parcial de Fp

v_CanEst= 0
c_ValExaTeo= 0.40
c_ValExaPra= 0.60
v_defPriPar=0.0
v_ConCic=1
v_sumDeNotPriPar=0.0
v_notDefPriPar= 0.0
v_proExaTeoPra=0.0


#Leer cantidad de estudiante 
v_canEst= int(input("Digite cantidad de estudiante:"))


for v_ConCic in range(v_CanEst):
#Captura de los datos
 v_nomEst = input("Nombre Estudiante:")
 v_genEst= input("Genero de Estudiante:")
 v_notExtTeo= float (input("digite la nota del examen teorico:"))
 v_notExtPra= float (input("digite la nota del examen practico:"))

#Calculo de la nota del primer particial por estudiante
 v_notDePriPar= v_notExtTeo * c_ValExaTeo + v_notExtPra * c_ValExaPra 

 print ("Su nota del primer parcial es:", v_notDePriPar)
#Calcula la suma de las notas de los estudiantes para calcular 
 v_sumDeNotPriPar= v_sumDeNotPriPar + v_notDefPriPar

#Calcular promedio del grupo de las notas de primer parcial 
 v_proNotPriPar= v_sumDeNotPriPar / v_canEst
 print ("El promedio de grupo del primer parcial es:" , v_proNotPriPar) 

#Calcular promedio del examen teorico y practico
 v_proExaTeoPra= v_notExtTeo / v_notExtPra
 print ("El promedio del examen teorico y practico:" , v_proExaTeoPra )
