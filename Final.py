import HCRfinal  # Importando el código HCRfinal como libreria
import pygame  # Importando pygame


def redrawGameWindow(Dir, p1, p2):  # Función que dibuja la pantalla y la actualiza
    global x, y, Side_A, Side_B  # Declarando x, y, Side_A, Side_B como variables globales

    win.blit(bg, (0, 0))  # dibujar una imagen sobre otra

    ypos = 300  # Iniciando el valor de ypos en 300
    """Por cada elemento del lado A, dibujar el elemento en la posición (x=5 , y=ypos) y disminuir en 60 ypos """
    for item in Side_A:
        win.blit(item, (5, ypos))
        ypos = ypos - 60

    ypos = 300  # Iniciando el valor de ypos en 300
    """Por cada elemento del lado B, dibujar el elemento en la posición (x=450 , y=ypos) y disminuir en 60 ypos """
    for item in Side_B:
        win.blit(item, (450, ypos))
        ypos = ypos - 60

    if p1 != 'Unknown':  # Si p1 no es desconocido
        """Si right, dibujar BoatRight el la posición (x, y) y al granjero (farmer) en la posición (x,y-50); 
           si p2 es diferente de farmer, dibujar p2 en la posición (x+50,y-50) """
        if right:
            win.blit(BoatRight, (x, y))
            win.blit(farmer, (x, y - 50))
            if p2 != farmer:
                win.blit(p2, (x + 50, y - 50))
        # left, dibujar BoatLeft el la posición (x, y) y al granjero (farmer) en la posición (x,y-50);
        #   si p2 es diferente de farmer, dibujar p2 en la posición (x+50,y-50)
        elif left:
            win.blit(BoatLeft, (x, y))
            win.blit(farmer, (x, y - 50))
            if p2 != farmer:
                win.blit(p2, (x + 50, y - 50))
    else:
        win.blit(char, (x, y))
    pygame.display.update()  # Actualizando las partes del display indicadas


def get_characters(d, p1, p2):  # Función que selecciona a los personajes siguiendo las indicaciones de la lista P
    if p2 == 'Zorro':
        character = fox
    elif p2 == 'Maiz':
        character = corn
    elif p2 == 'Ganzo':
        character = duck
    else:
        character = farmer
        return (d, farmer, character)

def Embark_characters(B, p1, p2):  # Función que sube los personajes al bote
    if p1 in B:
        B.remove(p1)
    if p2 in B:
        B.remove(p2)


def Disembark_characters(A, p1, p2):  # Función que baja del bote a los personajes
    if p1 not in A:
        A.append(p1)
    if p2 not in A:
        A.append(p2)


def HCR_animacion(P):  # Función que genera la animacion
    global x, y, left, right, vel  # Variables globales x, y, left, right, vel
    global Side_A, Side_B  # Variables globales Side_A, Side_B

    clock = pygame.time.Clock()  # Creando un reloj para gestionar tiempo
    """Declarando valores de las variables"""
    run = True
    move = 0

    while run:  # Mientras run sea cierto
        clock.tick(27)  # Estableciendo el reloj
        """Por cada evento de la cola de eventos obtenida con pygame.event.get(), si el evento el del tipo pygame.QUIT, 
           volver run = Falso para salir del ciclo while"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()  # Obteniendo el estado de todos los botones del teclado

        """Si keys pygame.K_LEFT, establecer left como verdadero y right como falso """
        if keys[pygame.K_LEFT]:  #
            left = True
            right = False
            """ Si  move es menor que el largo de P, empleando la función get_characters() seleccionar a los personajes 
                siguiendo las indicaciones de la lista P, embarcar los personajes, y por cada paso en un rango de 65, 
                restar vel a x, actualizar el display llamando la función redrawGameWindow(), poner un delay de 70, 
                aumentar move en 3, y desembarcar a los personajes en el lado a con la función Disembark_characters()"""
        if move < len(P):
            direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2])
            Embark_characters(Side_B, p1, p2)
        for step in range(65):
            x -= vel
            redrawGameWindow(direction, p1, p2)
            pygame.time.delay(70)
            move += 3
            Disembark_characters(Side_A, p1, p2)


        # Si keys pygame.K_RIGHT, establecer left como falso y right como verdadero """
        elif keys[pygame.K_RIGHT]:
            right = True
            left = False
            # Si  move es menor que el largo de P, empleando la función get_characters() seleccionar a los personajes
            # siguiendo las indicaciones de la lista P, embarcar los personajes, y por cada paso en un rango de 65,
            # aumentar vel a x, actualizar el display llamando la función redrawGameWindow(), poner un delay de 70,
            # aumentar move en 3, y desembarcar a los personajes en el lado B con la función Disembark_characters()"""
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2])
                Embark_characters(Side_A, p1, p2)
                for step in range(65):
                    x += vel
                    redrawGameWindow(direction, p1, p2)
                    pygame.time.delay(70)
                move += 3
                Disembark_characters(Side_B, p1, p2)
        else:
            redrawGameWindow('Standby', 'Unknown', 'Unknown')

    pygame.quit()  # Desinicializando todos los módulos de Pygame


def Busca_solucion():  # Función que busca la mejor solución en el menor número de movimientos (7 movimientos)
    P = HCRfinal.HCR()  # Llamando a la función HCR() del cógdigo HCRfinal
    """ Mientras la solución sea mayor a 21, es decir 7 movimientos, llamar a la función reiniciar_sistema() para reiniciar 
        el juego y volver a llamar a la función HCR() para encontrar una mejor solución """
    while len(P) > 22:
        HCRfinal.reiniciar_sistema()
        print('\nBuscando una mejor solución, Longitud del Path', len(P))
        P = HCRfinal.HCR()  # Llamando a la función HCR() del cógdigo HCRfinal.py
    """Una vez que se encuentra la solución P de 7 movimientos, se regresa y se imprime """
    print(P)
    print(len(P))
    print('\n =====> Solución encontrada:')
    return (P)


P = Busca_solucion()  # Llamando a la función Busca_solucion()
print('Aquí su animación')

pygame.init()  # Inicializando todos los módulos importados de pygame

win = pygame.display.set_mode((500, 500))  # Estableciendo el display para mostrar la animación
pygame.display.set_caption("How to Cross the River")  # Estableciendo el título de la ventana

"""Importando las imágenes que se utilizaran y declarando qué nombre tendrán en el código"""
BoatRight = pygame.image.load('BoteRight.png')
BoatLeft = pygame.image.load('BoteLeft.png')
bg = pygame.image.load('seaL.png')
char = pygame.image.load('BoteRight.png')
fox = pygame.image.load('fox.png')
corn = pygame.image.load('corn.png')
duck = pygame.image.load('duck.png')
farmer = pygame.image.load('farmer.png')
"""Declarando valores de variables"""
x = 10
y = 425
vel = 5
left = False
right = False

Side_A = [farmer, fox, duck, corn]  # Todos los personajes en el lado A
Side_B = []  # Lado B vacío

"""Llamando a la función de la HCR_animacion() con los valores P regresados por la función Busca_solucion() para 
   mostrar la animación que representa la solución final del juego."""
HCR_animacion(P)
