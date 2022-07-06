import numpy as np
Barcos_creados_user=[]                          #       LISTA DE BARCOS EXISTENTES DEL USUARIO CON POSICIONES
Barcos_hundidos_user=[]                         #       ES UNA LISTA DONDE PASAN LOS BARCOS HUNDIDOS DEL USUARIO CON POSICIONES
Disparos_user=[()]                              #       LISTA CON LOS DISPAROS HECHOS
Tocados_user=[()]                               #       LISTA DE POSICIONES TOCADAS DEL USUARIO (NO SE SI HACE FALTA)
posiciones_barcos_user=[]                    #      LISTA DE COORDENADAS DE LOS BARCOS DEL USUARIO, NO SE SI SERA BARCOS_CREADOS_COMPUTER


Barcos_creados_computer=[]                       #       LISTA DE BARCOS EXISTENTES DEL ORDENAR
Barcos_hundidos_computer=[]                      #       ES UNA LISTA DONDE PASAN LOS BARCOS HUNDIDOS DEL ORDENADOR
Disparos_computer=[()]                           #       LISTA CON LOS DISPAROS HECHOS POR EL ORDENADOR
Tocados_computer=[()]                            #       LISTA DE POSICIONES TOCADAS DEL USUARIO (NO SE SI HACE FALTA)


#for coordenada in posiciones_barcos_computer:
#    count=0
#    for a in coordenada:
#        p=list(a)
#        count=count+1
#        print(a)
#        print(count)
#        print(type(p))
#        for p in a:
#            print(p)
#            count+=1
#            print(b)

#print(len(posiciones_barcos_computer))

lista_barcos=[("portaaviones", 4),("acorazado",3),("destructor",3),("fragata",2),("crucero",2),("submarino",2),("lancha",1),("remolcador",1),("fueraborda",1),("corbeta",1)]

tablero_local=np.full((10,10),fill_value=" ")
tablero_computer=np.full((10,10),fill_value=" ")
tablero_computer_oculto=np.full((10,10),fill_value=" ")