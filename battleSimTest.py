import random

enemigo1 = {
        'nombre':'Jim',
	'vida':100,
	'ataque':30,
	'agilidad':10

}

jugador = {
        'nombre':'jugador',
	'vida':150,
	'ataque':40,
	'agilidad':50
	
}

atArmas = {
        'pala':20   
    }

muerto = False

objetos = {
    'pala': 0

    #Objetos no recogibles:(<0)
    
    }


objRec = [
    #Indicaciones       ,   Nombre corto
    ("Aquí hay una pala.", "Una pala común y corriente")

    ]

inventario = [
    0
    ]


def invent(args):
    if len(inventario) == 0:
        print("No tienes nada en el inventario")
    else:
        print("Actualmente tienes:")
        for i in inventario:
            print(objRec[i][1])
        
def atacar(atacante, victima):
    print(atacante.get('nombre'),"ataca a ",victima.get('nombre'))
    print(victima.get('nombre')," recibió ",atacante.get('ataque')," de daño.")
    victima['vida'] = victima['vida'] - atacante.get('ataque')

def huir(args):
    print("huyes")

def equipa(args):
    global jugador
    #print("args = ",args)
   ## print("args = ",args[0])
    if not args:
        print("Debes decirme que equipar.")
    elif args[0] in objetos:
        objNum = objetos[args[0]]
        if not objNum in inventario:
            print("No tienes eso.")
        else:
            print(args,"equipada.")
            print("Ataque original: ",jugador['ataque'])
            jugador['ataque'] = jugador['ataque'] + atArmas.get(args[0])
            print("Nuevo ataque: ",jugador.get('ataque'))
    else:
        print("No entiendo qué es eso.")
    

verbosBatalla = {
    'atacar': atacar, 'golpear': atacar,
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
        print("linea:",linea)
        if not linea[0] in verbosBatalla:
            print("No entendí eso.")
        else:
            if linea[0] == 'e' or linea[0] == 'equipar':
                if len(linea) == 0:
                    equipa(args)
                else:
                    print("arma: ",linea[1:])
                    equipa(linea[1:])
            
                
            else:
                func = verbosBatalla[linea[0]]
                args = linea[1:]
                func(args)


def main(x):
    print("MODO DE BATALLA:")
    if x.get('agilidad')+random.randint(0,100) < jugador.get('agilidad')+random.randint(0,100):
        print("Enemigo: ",x.get('nombre'))
        while x.get('vida') >= 0 or jugador.get('vida') >= 0:
            respuesta = input("Turno del jugador \n>").lower().split(';') or ['']
            print("Resp: ", respuesta)
            if respuesta[0] == 'atacar' or respuesta[0] == 'golpear':
                atacar(jugador,x)
            else:
                ejecutarBatalla(respuesta[0])
            
            print("Turno del enemigo")
            atacar(x,jugador)

            if x.get('vida') <= 0:
                print(x.get('nombre')," ha muerto.")
                print("Has ganado.")
                break
            elif jugador.get('vida') <= 0:
                print("Estás muerto.")
                exit()
            
            
            
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


if __name__ == '__main__':
	main(enemigo1)
