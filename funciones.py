import numpy as np
import variables as v

# def inicializa_tablero (tablero_local,tablero_computer):

#     v.tablero_local = np.full((10,10), full_value=" ")
    
#     v.tablero_computer= np.full((10,10), full_value=" ")

def inicializa_tablero(tablero_local,tablero_computer):
    print("VAMOS A GENERAR TU TABLERO\n\n")
    print ("OESTE               ESTE")
    print(tablero_local)
    print ("-"*50)
    print("VAMOS A GENERAR EL TABLERO DE TU SUPEROPONENTE'\n'\n")
    print ("OESTE               ESTE")
    print(tablero_computer)
    return 

#print(type(tablero_local))
# print(tablero_local)
# print("-"*50)
# print (tablero_computer)


def bienvenida ():
    print("BIENVENIDO A ESTE SIMULADOR ESPECIAL DE BATTLESHIT,'\n VAMOS A VER COMO SE TE DA, CAMPEON!!")


def barco_coordenada_manual (barco):
    """
    CREACION COORDENADAS INICIALES DE UN BARCO INDIVIDUAL

    LA VARIABLE ES UN BARCO EN FORMA DE LISTA, CON NOMBRE Y ESLORA
    """

    x=int(input("Introduce una posición de columna de 0 a 9, por favor: "))

    y=int(input("Introduce una posición de columna de 0 a 9, por favor: "))

    orientacion=input("Introduce una orientacion del barco "'\n'"norte"",""sur"",""este"",""oeste"": ").lower()
    
    eslora=int(barco[1])
    nombre_barco=barco[0]

    if orientacion=="norte":
        if x-eslora<0:
            print("El barco no se puede poner ahi, se sale del tablero."'\n'"Coloquelo en otra posición, gracias")
            barco_coordenada_manual (barco) 
    if orientacion=="sur":
        if x+eslora>9:
            print("El barco no se puede poner ahi, se sale del tablero."'\n'"Coloquelo en otra posición, gracias")
            barco_coordenada_manual (barco) 
    if orientacion=="oeste":
        if y-eslora<0:
            print("El barco no se puede poner ahi, se sale del tablero."'\n'"Coloquelo en otra posición, gracias")
            barco_coordenada_manual (barco) 
    if orientacion=="este":
        if y+eslora>9:
            print("El barco no se puede poner ahi, se sale del tablero."'\n'"Coloquelo en otra posición, gracias")
            barco_coordenada_manual (barco) 
    
    coordenadas_barco=[(x,y)]

    print ("La orientacion es :",orientacion)
    print("El Barco es: ",nombre_barco)
    print("La eslora es: ", eslora)
#   print (coordenadas_barco)

    while len(coordenadas_barco)<eslora:
        if coordenadas_barco in v.posiciones_barcos_user:
           print("No se puede colocar el barco, ya hay uno en esta posicion.")
           barco_coordenada_manual (barco)
        else:
            if orientacion=="norte":
                x=x-1
                coordenadas_barco.append((x,y))
            if orientacion=="sur":
                x=x+1
                coordenadas_barco.append((x,y))
            if orientacion=="oeste":
                y=y-1
                coordenadas_barco.append((x,y))
            if orientacion=="este":
                y=y+1
                coordenadas_barco.append((x,y))


    print(coordenadas_barco)
    for elem in coordenadas_barco:
        v.tablero_local[elem]="="
    #    Barcos_creados_computer.append(coordenadas_barco)           ## ESTA INCLUYENDO TANTOS LOS QUE ESTAN BIEN POSICIONADOS COMO LOS MAL POSICIONADOS
    v.posiciones_barcos_user.append(coordenadas_barco)        ## ESTA INCLUYENDO TANTOS LOS QUE ESTAN BIEN POSICIONADOS COMO LOS MAL POSICIONADOS
   # v.tablero_local=barco_coordenada_manual(barco)

    #return v.posiciones_barcos_computer
                                   ## ESTA INCLUYENDO TANTOS LOS QUE ESTAN BIEN POSICIONADOS COMO LOS MAL POSICIONADOS
    #    return Barcos_creados_computer                              ## ## ESTA INCLUYENDO TANTOS LOS QUE ESTAN BIEN POSICIONADOS COMO LOS MAL POSICIONADOS            

#def opcion_posicion():
#    a=input("QUIERES COLOCAR TU LOS BARCOS? DI (SI/NO)").upper()
#    if a=="SI":
#        barco_coordenada_manual (barco)
#    else:
#        print("ESTA BIEN")
#    return

def posicionamiento_barco_manual_user():
    print("VAMOS A COLOCAR EL PORTAAVIONES, TIENE 4 DE ESLORA")
    barco_coordenada_manual (v.lista_barcos[0])
    print("OESTE\t\t\t\t\tESTE")
    print(v.tablero_local)
    print("NO OLVIDES, ESTAS SON LAS COORDENADAS QUE HAS PUESTO DE MOMENTO.",v.posiciones_barcos_user)

    print("VAMOS A COLOCAR EL ACORAZADO, TIENE 3 DE ESLORA:")
    barco_coordenada_manual (v.lista_barcos[1])
    print("OESTE\t\t\t\t\tESTE")
    print(v.tablero_local)
    print("NO OLVIDES, ESTAS SON LAS COORDENADAS QUE HAS PUESTO DE MOMENTO.",v.posiciones_barcos_user)

    print("VAMOS MUY BIEN.'\nAHORA VAMOS A PONER EL DESTRUCTOR, QUE TAMBIÉN TIENE 3.")
    barco_coordenada_manual (v.lista_barcos[2])
    print("OESTE\t\t\t\t\tESTE")
    print(v.tablero_local)
    print("NO OLVIDES, ESTAS SON LAS COORDENADAS QUE HAS PUESTO DE MOMENTO.",v.posiciones_barcos_user)

    print("EMPEZAMOS A PONER BARCOS DE 2 DE ESLORA.'\nEL PRIMERO LA FRAGATA.")
    barco_coordenada_manual (v.lista_barcos[3])
    print("OESTE\t\t\t\t\tESTE")
    print(v.tablero_local)
    print("NO OLVIDES, ESTAS SON LAS COORDENADAS QUE HAS PUESTO DE MOMENTO.",v.posiciones_barcos_user)

    print("AHORA VAMOS A PONER EL SUBMARINO, QUE TAMBIÉN TIENE 2.")
    barco_coordenada_manual (v.lista_barcos[4])
    print("OESTE\t\t\t\t\tESTE")
    print(v.tablero_local)
    print("NO OLVIDES, ESTAS SON LAS COORDENADAS QUE HAS PUESTO DE MOMENTO.",v.posiciones_barcos_user)

    print("AHORA EL ULTIMO DE LOS DE 2 DE ESLORA,'\nEL CRUCERO.")
    barco_coordenada_manual (v.lista_barcos[5])
    print("OESTE\t\t\t\t\tESTE")
    print(v.tablero_local)
    print("NO OLVIDES, ESTAS SON LAS COORDENADAS QUE HAS PUESTO DE MOMENTO.",v.posiciones_barcos_user)

    print("YA ESTAMOS TERMINANDO, SOLO QUEDAN DE 1 DE ESLORA,'\nCOMENZAMOS CON LA LANCHA.")
    barco_coordenada_manual (v.lista_barcos[6])
    print("OESTE\t\t\t\t\tESTE")
    print(v.tablero_local)
    print("NO OLVIDES, ESTAS SON LAS COORDENADAS QUE HAS PUESTO DE MOMENTO.",v.posiciones_barcos_user)

    print("YA ESTAMOS TERMINANDO, SOLO QUEDAN DE 1 DE ESLORA,'\nSEGUIMOS CON EL FUERABORDA.")
    barco_coordenada_manual (v.lista_barcos[7])
    print("OESTE\t\t\t\t\tESTE")
    print(v.tablero_local)
    print("NO OLVIDES, ESTAS SON LAS COORDENADAS QUE HAS PUESTO DE MOMENTO.",v.posiciones_barcos_user)

    print("DOS MAS Y EMPEZAMOS. AHORA TOCA EL REMOLCADOR.")
    barco_coordenada_manual (v.lista_barcos[8])
    print("OESTE\t\t\t\t\tESTE")
    print(v.tablero_local)
    print("NO OLVIDES, ESTAS SON LAS COORDENADAS QUE HAS PUESTO DE MOMENTO.",v.posiciones_barcos_user)

    print("FINALIZAMOS CON LA CORBETA.")
    barco_coordenada_manual (v.lista_barcos[9])
    print("OESTE\t\t\t\t\tESTE")
    print(v.tablero_local)
    print("NO OLVIDES, ESTAS SON LAS COORDENADAS QUE HAS PUESTO DE MOMENTO.",v.posiciones_barcos_user)

    print("YA HEMOS COLOCADO TODOS NUESTROS BARCOS, AHORA EL ORDENADOR COLOCARÁ LOS SUYOS")



def barco_coordenada_computer (barco):
    """
    CREACION COORDENADAS INICIALES DE UN BARCO INDIVIDUAL

    LA VARIABLE ES UN BARCO EN FORMA DE LISTA, CON NOMBRE Y ESLORA
    """
    import numpy as np
    x=np.random.randint(0,10)
    y=np.random.randint(0,10)
    nombre_barco=barco[0]
    eslora=int(barco[1])
    orientacion=np.random.choice(["norte","sur","este","oeste"])
    nombre_barco=barco[0]
    
    if orientacion=="norte":
        if x-eslora<0:
            barco_coordenada_computer (barco) 
    if orientacion=="sur":
        if x+eslora>9:
            barco_coordenada_computer (barco) 
    if orientacion=="oeste":
        if y-eslora<0:
            barco_coordenada_computer (barco) 
    if orientacion=="este":
        if y+eslora>9:
            barco_coordenada_computer (barco) 
    
    coordenadas_barco=[(x,y)]

    while len(coordenadas_barco)<eslora:
        if orientacion=="norte":
            x=x-1
            coordenadas_barco.append((x,y))
        if orientacion=="sur":
            x=x+1
            coordenadas_barco.append((x,y))
        if orientacion=="oeste":
            y=y-1
            coordenadas_barco.append((x,y))
        if orientacion=="este":
            y=y+1
            coordenadas_barco.append((x,y))

    if len(coordenadas_barco)==eslora:
    #    Barcos_creados_computer.append(coordenadas_barco)           ## ESTA INCLUYENDO TANTOS LOS QUE ESTAN BIEN POSICIONADOS COMO LOS MAL POSICIONADOS
        v.posiciones_barcos_computer_oculto.append(coordenadas_barco)        ## ESTA INCLUYENDO TANTOS LOS QUE ESTAN BIEN POSICIONADOS COMO LOS MAL POSICIONADOS
        return v.posiciones_barcos_computer_oculto                          ## ESTA INCLUYENDO TANTOS LOS QUE ESTAN BIEN POSICIONADOS COMO LOS MAL POSICIONADOS
    #    return barco_coordenada_computer                              ## ## ESTA INCLUYENDO TANTOS LOS QUE ESTAN BIEN POSICIONADOS COMO LOS MAL POSICIONADOS            


def posicionamiento_barco_computer():
    """
    POSICIONAMIENTO AUTOMATICO DE LOS BARCOS EN EL TABLERO OCULTO DEL ORDENADOR
    """
    barco_coordenada_computer (v.lista_barcos[0])
    barco_coordenada_computer (v.lista_barcos[1])
    barco_coordenada_computer (v.lista_barcos[2])
    barco_coordenada_computer (v.lista_barcos[3])
    barco_coordenada_computer (v.lista_barcos[4])
    barco_coordenada_computer (v.lista_barcos[5])
    barco_coordenada_computer (v.lista_barcos[6])
    barco_coordenada_computer (v.lista_barcos[7])
    barco_coordenada_computer (v.lista_barcos[8])
    barco_coordenada_computer (v.lista_barcos[9])

    print("COMIENZA EL JUEGO")


def disparo_computer ():

    """
    FUNCIONES DE DISPARO DEL ORDENADOR
    """

    x=np.random.randint(0,10)
    y=np.random.randint(0,10)
    coordenada=(x,y)
    print("La coordenada  del disparo es  :", coordenada)

    if coordenada in v.Disparos_computer:
        print("MANCO!!! YA HAS REALIZADO ESTE DISPARO ANTES.'\nVUELVE A DISPARAR, ANDA!!")
        disparo_computer ()
    else:
        v.Disparos_computer.append(coordenada)
        print("Disparo registrado")

    if v.tablero_local [coordenada]=="=":                  #   LO MISMO CAMBIO POR Barcos_creados_computer=[] 
        print("TOCADO")                                         #   QUEDA PENDIENTE HACER HUNDIDO
        v.Tocados_user.append(coordenada)                        #   AÑADO LA POSICION A LA LISTA DE DISPAROS REALIZADOS 
        print(v.tablero_local)
        if len(v.Tocados_user) == "20":
            print("SE HA TERMINADO LA PARTIDA, HAS PERDIDO")
            print("Estos son los disparos que has realizado ya: ",v.Disparos_user)
            
        else:
            print("ENHORABUENA!!\n\tCOMO PREMIO, VUELVE A DISPARAR!")        
            disparo_computer ()   
#       v.posiciones_barcos_user.remove(coordenada)


    else:
        print("Agua")
        v.tablero_local [coordenada]="|"

    print("ES TU TURNO!! A VER QUE TAL SE TE DA")
    
    disparo_user(v.tablero_computer_oculto, v.tablero_computer, coordenada)
    return v.tablero_local
    

def disparo_user (tablero_computer_oculto, tablero_computer, coordenada):                ## ESTO QUEDA POR CHEQUEAR
    """
    FUNCIONES DE DISPARO DEL USUARIO
    """

    x=int(input("Introduce la columna del disparo de 0 a 9, por favor: "))

    y=int(input("Introduce la fila del disparo de 0 a 9, por favor: "))
    coordenada=(x,y)

    print("La coordenada  del disparo es  :", coordenada)

    if coordenada in v.Disparos_user:
        print("YA HA REALIZADO ESTE DISPARO ANTES.VUELVA A DISPARAR")
        disparo_user (tablero_computer_oculto, tablero_computer, coordenada)
    else:
        v.Disparos_user.append(coordenada)
        print("Disparo registrado")


    if v.tablero_computer_oculto [coordenada]=="=":        #   LO MISMO CAMBIO POR Barcos_creados_computer=[] 
        print("TOCADO")                                             #   QUEDA PENDIENTE HACER HUNDIDO
        v.Tocados_computer.append(coordenada)                        #   AÑADO LA POSICION A LA LISTA DE DISPAROS REALIZADOS 
        if len(v.Tocados_computer) == "20":
            print("ENHORABUENA!! HAS GANADO")

        tablero_computer [coordenada]="X"
        disparo_user (tablero_computer, coordenada)   


    else:
        print("Agua")
        v.tablero_computer [coordenada]="|"
    
    print(v.tablero_local)
    print(tablero_computer)
    disparo_computer ()
    return v.tablero_computer  