class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm,weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


while True:

    print("\nINTRODUZCA LA INFORMACION DEL JUGADOR DE BALONCESTO O FUTBOL:")

    nombre = input("Introduzca el nombre del jugador: ")
    apellidos = input("Introduzca el apellido del jugador: ")
    altura = input("Introduzca la altura del jugador: ").replace(",", ".")
    peso = input("Introduzca el peso del jugador: ").replace(",", ".")

    seleccion = input("""

    ¿Jugador de futbol o baloncesto? Selecciona la opcion correspondiente (A / B / C):

    [A] - Jugador de Baloncesto
    [B] - Jugador de Futbol.
    [C] - Salir
    """)

    if seleccion == "A" or seleccion == "a":
        puntos = input("Introduzca los puntos del jugador: ")
        rebotes = input("Introduzca los rebotes del jugador: ")
        asistencias = input("Introduzca las asistencias del jugador: ")

        jugador = BasketballPlayer(first_name=nombre, last_name=apellidos, height_cm=float(altura),
                                   weight_kg=float(peso),
                                   points=int(puntos), rebounds=int(rebotes), assists=int(asistencias))

        with open("BasketballPlayer.txt", "a") as basketball_file:
            basketball_file.write(str(jugador.__dict__))

        print("\ninformacion del jugador registrada:", jugador.__dict__)

    elif seleccion == "B" or seleccion == "b":
        goles = input("Introduzca los goles totales: ")
        tarjetas_amarillas = input("Introduzca las tajetas amarillas del jugador: ")
        tarjetas_rojas = input("Introduzca las tarjetas rojas: ")

        jugador = FootballPlayer(first_name=nombre, last_name=apellidos, height_cm=float(altura), weight_kg=float(peso),
                                 goals=int(goles), yellow_cards=int(tarjetas_amarillas), red_cards=int(tarjetas_rojas))

        with open("footballplayer.txt", "a") as footballplayer_file:
            footballplayer_file.write(str(jugador.__dict__))

        print("\ninformacion del jugador registrada:", jugador.__dict__)

    elif seleccion == "C" or seleccion == "c":
        print("SALIENDO DE LA APLICACION...")

        break

    else:
        print("ERROR!! NO EXISTE LA OPCION INTRODUCIDA!! INTRODUZCA LA OPCION CORRECTA")