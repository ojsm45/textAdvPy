import random

seccionActual = 0
sec = {}
visitados = []

muertes = [
    " ahogado en su propia sangre.",
    " como el animal que era",
    " la pudrición de su boca por fin descansa.",
    " sería justo."
]

enemigo1 = {
        'nombre':'Jim',
	'vida':100,
	'ataque':30,
	'agilidad':10

}

jugador = {
        'nombre':'',
	'vida':150,
	'ataque':40,
	'agilidad':50
	
}

atArmas = {
        'pala':20   

}


def atacar(atacante, victima):
    print(atacante.get('nombre'),"ataca a ",victima.get('nombre'))
    print(victima.get('nombre')," recibió ",atacante.get('ataque')," de daño.")
    victima['vida'] = victima['vida'] - atacante.get('ataque')

def huir(args):
    print("huyes")

def equipa(args):
    global jugador
    #print("args = ",args)
    # print("args = ",args[0])
    if not args:
        print("Debes decirme que equipar.")
    elif args[0] in objetos:
        objNum = objetos[args[0]]
        if not objNum in inventario:
            print("No tienes eso.")
        else:
            print(args[0],"equipada.")
            print("Ataque original: ",jugador['ataque'])
            jugador['ataque'] = jugador['ataque'] + atArmas.get(args[0])
            print("Nuevo ataque: ",jugador.get('ataque'))
    else:
        print("No entiendo qué es eso.")
    

secciones = [
    (
"""Estás en el frente de la casa de Rut, si vas hacia adelante encontrarás la sala.""",
    "Frente de la casa de Rut"), #0 (número de tupla)
    (
"""Ahora estás en la sala, ella se está vistiendo. Nada fuera de lugar...""",
    "Sala de la casa de Rut"), #1
    (
"""Estás en la cocina, no se ve nadie...""",
    "Cocina de la casa de Rut"), #2
    
#Continua con los lugares...
#Dar direciones en las descripciones y guiños para la busqueda de objetos
]

for i in enumerate(secciones):
    indice = i[0]
    nombreLargo = i[1][1] # i[1][0] es la descripción
    nombreCorto = ''
    for car in nombreLargo:
        if car in ' ':
            nombreCorto = nombreCorto + '-'
        elif not car in ".'":
            nombreCorto = nombreCorto + car.lower() #Hacer minúculas cada carácter
    sec[nombreCorto] = indice

dirs ={
'norte': 0, 'n': 0, 'arriba': 0, 'delante': 0,
'noreste': 1, 'ne' : 1,
'este': 2, 'e': 2, 'derecha' : 2,
'sureste': 3, 'se': 3,
'sur' : 4, 's': 4, 'abajo': 4, 'atras': 4,
'suroeste': 5, 'so': 5,
'oeste': 6, 'o': 6, 'izquierda': 6,
'noroeste': 7, 'no': 7,
'adentro': 8, 'entrar': 8,
'afuera': 9, 'salir': 9, 'escapar': 9,
'subir': 10,
'bajar':11
    }

#Hacer lista de listas para representar un mapa.
#Cada lista de la lista mayor es el mapa de la sección.
#Cada elemento de la sublista es el resultado de ir en esa dirección.
mapa = [
#     n  ne   e  se   s  so   o  no  den fue sub baj
    [ 1, -1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1], #0
    [ 2, -1, -1, -1,  0, -1, -1, -1,  2,  0, -1, -1], #1
    [-1,  1, -1, -1,  1, -1, -1, -1, -1,  1, -1, -1], #2
    
# Continúa...
]

#Diccionario con objetos
#Los objetos "recogibles" tienen valores NO negativos
#Los objetos NO "recogibles" tienen valores negativos
objetos = {
    'pala': 0

    #Objetos no recogibles:(<0)
    
    }

#Lista de tuplas para objetos con indicación y nombre

objRec = [
    #Indicaciones       ,   Nombre corto
    ("Aquí hay una pala.", "Una pala común y corriente")

    ]

#Acorde al indice de objetos, descripciones para objetos.
desObjRec = [
    "Una pala que sirve de pala. daa"

    ]

objNoRec = [

    ]

#Acorde al índice de objetos, descripciones para objetos inamovibles.
#DEJAR EL PRIMER ESPACIO VACIO(NONE)

descObjNoRec = [
    None,
    
    ]

#Crear inventario e items para cada sección
#El inventario es una lista de lo que tienes en tu inventario(lista de índices
#a los objetos

inventario = [

    ]

elementos = [
    [],
    [],
    [objetos['pala']] #2 
    
    ]


#Escribir funcion para mostrar ayuda
def ayuda(args):
    print("You are alone bitch.")    


#Escribir funciones para:

#Describir sección
#Inventario
#Coger
#Soltar
#Mirar
#Mover alrededor (mov especial)
    
#Muerto (reiniciar, guardar y cargar)
#Hacer varible vivo para indicar si el jugador muere

#Lista de visitados para saber que lugar ha sido visitado
def mover(direccion):
    global seccionActual
    nuevaSeccion = mapa[seccionActual][direccion]
    if nuevaSeccion < 0:
        print("No puedes ir hacia allá.")
        
    #elif newsect == SPECIALNUMBER:
    #    special_move(direct)

    else:
        seccionActual = nuevaSeccion
        describir(nuevaSeccion)

#def atacar():
    

def casosEsp(x):
    if x == 1:
        if enemigo1.get('vida') <= 0:
            print("En el suelo yace el cuerpo de Jim jajaja.")
        else:
            valor = random.randint(0,100)
            if 20 <= valor <= 100:
                print("Está",enemigo1.get('nombre'),"(hp ese)")
                respuesta = input(">").lower().split(';') or ['']
                if respuesta[0] == 'atacar' or respuesta[0] == 'golpear' or respuesta[0] == 'a' or respuesta[0] == 'matar':
                    batalla(enemigo1)       
            

def describir(seccion):
    "give a long long johnson"
    ##This is because room 0...
    global visitados
    print(secciones[abs(seccion)][1])
    if seccion <= 0 or not seccion in visitados:
        print(secciones[abs(seccion)][0])
    if  not seccion in visitados:
        visitados.append(seccion)
    #Todo lo demas
    
    casosEsp(seccionActual)
    
    for i in elementos[abs(seccion)]:
        if i >= 0:
            print(objRec[i][0])
        else:
            if isinstance(objNoRec[abs(i)], str):
                print(objNoRec[abs(i)])


def invent(args):
    print("Actualmente tienes:")
    for i in inventario:
        print(objRec[i][1])


verbosBatalla = {
    'atacar': atacar, 'golpear': atacar, 'a': atacar, 'matar': atacar,
    'inventario':invent, 'i':invent,
    'equipar':equipa, 'e':equipa, 
    'huir': huir
        
    }

def ejecutarBatalla(x):
    linea = x.split()
    for car in ',:':
        linea = car.join(linea).split(car)
    if linea:
        print()
        if not linea[0] in verbosBatalla:
            print("No entendí eso.")
        else:
            if linea[0] == 'e' or linea[0] == 'equipar':
                if len(linea) == 0:
                    equipa(args)
                else:
                    equipa(linea[1:])
            
            else:
                func = verbosBatalla[linea[0]]
                args = linea[1:]
                func(args)


def batalla(x):
    print("MODO DE BATALLA:")
    if x.get('agilidad')+random.randint(0,100) < jugador.get('agilidad')+random.randint(0,100):
        print("Enemigo: ",x.get('nombre'))
        while x.get('vida') >= 0 or jugador.get('vida') >= 0:
            print()
            respuesta = input("Turno del jugador \n>").lower().split(';') or ['']
            if respuesta[0] == 'atacar' or respuesta[0] == 'golpear':
                atacar(jugador,x)
            else:
                ejecutarBatalla(respuesta[0])
            print()
            print("Turno del enemigo")
            atacar(x,jugador)

            if x.get('vida') <= 0:
                print(x.get('nombre')," ha muerto",muertes[random.randint(0,len(muertes))])
                print("Has ganado.")
                break
            elif jugador.get('vida') <= 0:
                print("Estás muerto.")
                exit(1)
            
    else:
        print("Turno del enemigo")
        #Ataca enemigo
        atacar(x,jugador)
        print("Enemigo: ",x.get('nombre'))
        while x.get('vida') != 0 or jugador.get('vida') != 0:
            respuesta = input("Turno del jugador \n>").lower().split(';') or ['']
            print("Resp: ", respuesta)
            if respuesta[0] == 'atacar' or respuesta[0] == 'golpear':
                atacar(jugador,x)
            else:
                ejecutarBatalla(respuesta[0])
            
            print("Turno del enemigo")
            atacar(x,jugador)
            
            if x.get('vida') <= 0:
                print(x.get('nombre')," ha muerto",muertes[random.randint(0,len(muertes))])
                print("Has ganado.")
                break
            elif jugador.get('vida') <= 0:
                print("Estás muerto.")
                exit(1)



def tomarObj(x):
    global inventario, elementos
    if not x in elementos[seccionActual]:
        print("No veo eso ahí.")
    else:
        if x < 0:
            print("No puedes tomar eso.")
        else:
            print("Recogido.")
            elementos[seccionActual].remove(x)
            inventario.append(x)
            

def coger(args):
    if not args:
        print("Debes especificar un objeto.")
    else:
        if args[0] == "todo":
            primerObj = list(elementos[seccionActual])
            tomarAlgo = False
            for i in primerObj:
                if i >= 0:
                    tomarAlgo = True
                    print("%s:" % objRec[i][1],
                          tomarObj(i))
            if not tomarAlgo:
                print("Nada que tomar.")
        else:
            if not args[0] in objetos:
                print("No sé lo que es eso.")
            else:
                tomarObj(objetos[args[0]])

def soltar(args):
    global inventario, elementos
    if not args:
        print("Debes especificar un objeto")
    else:
        if not args[0]in objetos:
            print("No sé lo que es eso.")
        else:
            objNum = objetos[args[0]]
            if not objNum in inventario:
                print("No tienes eso.")
            else:
                print("Hecho.")
                inventario.remove(objNum)
                elementos[seccionActual].append(objNum)

def examinar(args):
    if not args:
        del visitados[seccionActual]
        describir(seccionActual)
    else:
        if not args[0] in objetos:
            print("No sé lo que estás haciendo.")
        else:
            objNum = objetos[args[0]]
            if not objNum in inventario and not objNum in elementos[seccionActual]:
                print("No veo eso por aquí.")
            else:
                if objNum >= 0:
                    desc = desObjRec[objNum]
                else:
                    desc = desObjNoRec[abs(objNum)]
                if isinstance (desc, str):
                    print(desc)
                else:
                    print("No veo nada especial.")

def norte(args):
    mover(0)

def noreste(args):
    mover(1)

def este(args):
    mover(2)

def sureste(args):
    mover(3)

def sur(args):
    mover(4)

def suroeste(args):
    mover(5)

def oeste(args):
    mover(6)

def noroeste(args):
    mover(7)

def entrar(args):
    mover(8)

def salir(args):
    mover(9)

def subir(args):
    mover(10)

def bajar(args):
    mover(11)

    
def ir(args):
    if not args:
        print("Debes especificar una dirección...")
    else:
        if not args[0] in dirs:
            print("No entiendo a donde quieres ir.")
        else:
            mover(dirs[args[0]])


def muerte(args):
    global muerto
    print()
    if args:
        print("Estás muerto.")
    #Si hay puntuación iría aqui
    muerto = True

def _quit(args):
    die([])


verbos = {
    'coger': coger, 'agarrar': coger, 'tomar': coger, 'recoger': coger,
    'tirar': soltar, 'soltar': soltar, 'dejar': soltar, 
    'examinar': examinar, 'x': examinar,
    'inventario':invent, 'objetos': invent, 'i': invent,
    'morir': muerte, 'suicidio': muerte,
    'ayuda': ayuda, 'help': ayuda,
    'norte': norte, 'n': norte, 'arriba': norte, 'delante': norte,
    'noreste': noreste, 'ne' : noreste,
    'este': este, 'e': este, 'derecha': este,
    'sureste': sureste, 'se': sureste,
    'sur' : sur, 's': sur, 'abajo': sur, 'atras': sur,
    'suroeste': suroeste, 'so': suroeste,
    'oeste': oeste, 'o': oeste, 'izquierda': oeste,
    'noroeste': noroeste, 'no': noroeste,
    'adentro': entrar, 'entrar': entrar,
    'afuera': salir, 'salir': salir, 'escapar': salir,
    'subir': subir,
    'bajar':bajar,
    'ayuda': ayuda
    #'atacar': atacar
        
    }
    
def ejecutar(x):
    linea = x.split()
    for car in ',:':
        linea = car.join(linea).split(car)
    if linea:
        print()
        if not linea[0] in verbos:
            print("No entendí eso.")
        else:
            func = verbos[linea[0]]
            args = linea[1:]
            func(args)

muerto = False

def correrJuego():
    print("COMIENZO DEL JUEGO:") #Presentacíon del juego e instrucciones
    jugador['nombre'] = input("Ingrese nombre del jugador: ")    
    describir(seccionActual)
    while not muerto:
        respuesta = input('>').lower().split(';') or ['']
        primero = True
        for i in respuesta:
            if not muerto:
                if not primero:
                    print('>')
                ejecutar(i)
                primero = False
    if __name__ == '__main__':
        input('\n')


if __name__ == '__main__': #IMPORTANTE
    correrJuego()
    
    
                    

    
