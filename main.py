from re import X
import variables as var
#from variables import *
import funciones as fn
import numpy as np


# var.tablero_local=np.full((10,10),fill_value=" ")
# var.tablero_computer=np.full((10,10),fill_value=" ")
fn.bienvenida ()

fn.inicializa_tablero(var.tablero_local,var.tablero_computer)

#fn.opcion_posicion()

fn.posicionamiento_barco_manual_user()
fn.posicionamiento_barco_computer()

print("VAMOS A EMPEZAR A DISPARAR. A VER QUE PUNTERIA TIENES")

fn.disparo_computer ()
