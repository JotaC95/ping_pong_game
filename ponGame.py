"""
Juego de Arcade Pong
Reproduce el clásico juego de arcade Pong. Para ello puedes usar el módulo "turtle" para
crear los componentes del juego y detectar las colisiones de la pelota con las paletas de los
jugadores.También puedes definir una serie de asignaciones de teclas para establecer los
controles del usuario para las paletas de los jugadores izquierda y derecha.

Use el modulo de turtle para el dibujo de figuras como las paletas de juego 
"""

# Instrucciones:
# comenzar el juego con la tecla espacio
# el juego se puede pausar con la misma tecla espacio
# puedes ajustar el numero de puntos con el que se gana el juego
# con la tecla r re reinicia el juego y puedes volver a empezar
# una vez que el jugador alcanza el numero acordado de puntos se declara al ganador y el juego para hasta reiniciarlo


import turtle

# Declaracion de variables de inicio
puntos_derecha = 0
puntos_izquierda = 0
partido = False

# Para configurar la  ventana y el texto de guia del juego
ventana = turtle.Screen()  # Crea un objeto de la clase turtle
ventana.title("Juego de pong")
ventana.bgcolor("#DDC4C4")
ventana.setup(width=800, height=600)
ventana.tracer(0)

texto = turtle.Turtle()
texto.speed(0)
texto.color("#000000")
texto.penup()
texto.hideturtle()
texto.goto(0, 280)
texto.write(
    "Inicio y pausa el juego con la tecla espacio y reinicio con tecla r",
    align="center",
    font=("courier", 12, "normal"),
)

# Para configurar la PALETA DERECHA
paleta_derecha = turtle.Turtle()
paleta_derecha.speed(0)
paleta_derecha.shape("square")
paleta_derecha.color("#3889D1")
paleta_derecha.penup()
paleta_derecha.goto(360, 0)
paleta_derecha.shapesize(stretch_wid=7, stretch_len=1.2)

# Configuracion de PALETA IZQUIERDA
paleta_izquierda = turtle.Turtle()
paleta_izquierda.speed(0)
paleta_izquierda.shape("square")
paleta_izquierda.color("#E26565")
paleta_izquierda.penup()
paleta_izquierda.goto(-360, 0)
paleta_izquierda.shapesize(stretch_wid=7, stretch_len=1.2)

# Configuracion de la PELOTA
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.9
pelota.dy = -0.9

# Configuracion de MARCADOR
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.goto(0, 240)
marcador.write("Rojos: 0  Azules:0", align="center", font=("courier", 24, "normal"))
marcador.hideturtle()


# Funcion para iniciar el juego
def inicio_juego():
    global partido
    if partido:
        partido = False
    else:
        partido = True


# Funcion de reinicio del juego
def reinicio_juego():
    global puntos_derecha, puntos_izquierda
    puntos_derecha = 0
    puntos_izquierda = 0
    marcador.clear()
    marcador.write(
        "Rojos:{}  Azules:{}".format(puntos_izquierda, puntos_derecha),
        align="center",
        font=("courier", 24, "normal"),
    )
    pelota.goto(0, 0)


# Movimiento de paletas


# PALETA IZQUIERDA desplazamiento para ARRIBA
def paleta_izquierda_arriba():
    y = paleta_izquierda.ycor()
    if y < 230:
        y += 20
    paleta_izquierda.sety(y)


# PALETA IZQUIERDA desplazamiento para ABAJO
def paleta_izquierda_abajo():
    y = paleta_izquierda.ycor()
    if y > -220:
        y -= 20
    paleta_izquierda.sety(y)


# PALETA DERECHA desplazamiento para ARRIBA
def paleta_derecha_arriba():
    y = paleta_derecha.ycor()
    if y < 240:
        y += 20
    paleta_derecha.sety(y)


# PALETA DERECHA desplazamiento para ABAJO
def paleta_derecha_abajo():
    y = paleta_derecha.ycor()
    if y > -220:
        y -= 20
    paleta_derecha.sety(y)


# Asignacion de botones
ventana.listen()
ventana.onkeypress(paleta_izquierda_arriba, "w")
ventana.onkeypress(paleta_izquierda_abajo, "s")
ventana.onkeypress(paleta_derecha_arriba, "Up")
ventana.onkeypress(paleta_derecha_abajo, "Down")

ventana.onkeypress(inicio_juego, "space")
ventana.onkeypress(reinicio_juego, "r")

# Bucle principal del juego

while True:
    ventana.update()

    # El juego inicia solo si un jugador aplasta la tecla espacio
    if partido:
        # Movimiento de la pelota
        pelota.setx(pelota.xcor() + pelota.dx)
        pelota.sety(pelota.ycor() + pelota.dy)

        # Limitar movimientos pelota a bordes de la ventana

        # Limite del borde superior
        if pelota.ycor() > 290:
            pelota.sety(290)
            pelota.dy *= -1

        # Limite del borde inferior
        if pelota.ycor() < -290:
            pelota.sety(-290)
            pelota.dy *= -1

        # Limite borde derecho y contador de puntos para el equipo rojo
        if pelota.xcor() > 390:
            pelota.goto(0, 0)
            pelota.dx *= -1
            puntos_derecha += 1
            marcador.clear()
            marcador.write(
                "Rojo: {} | Azul: {}".format(puntos_derecha, puntos_izquierda),
                align="center",
                font=("courier", 24, "normal"),
            )
            pelota.color("#E26565")

        # Limite borde izquierdo y contador de puntos para el equipo azul
        if pelota.xcor() < -390:
            pelota.goto(0, 0)
            pelota.dx *= -1
            puntos_izquierda += 1
            marcador.clear()
            marcador.write(
                "Rojo: {} Azul: {}".format(puntos_derecha, puntos_izquierda),
                align="center",
                font=("courier", 24, "normal"),
            )
            pelota.color("#3889D1")

        # Marcador de puntos
        puntos_ganador = 2

        if puntos_derecha == puntos_ganador:
            marcador.clear()
            marcador.write(
                "Fin del juego! El ganador es el Rojo\n ",
                align="center",
                font=("courier", 24, "normal"),
            )
            marcador.write(
                "Rojo: {} | Azul: {}".format(puntos_derecha, puntos_izquierda),
                align="center",
                font=("courier", 24, "normal"),
            )
            pelota.dx = 0
            pelota.dy = 0
        elif puntos_izquierda == puntos_ganador:
            marcador.clear()
            marcador.write(
                "Fin del juego! El ganador es el Azul\n ",
                align="center",
                font=("courier", 22, "normal"),
            )
            marcador.write(
                "Rojo: {} | Azul: {}".format(puntos_derecha, puntos_izquierda),
                align="center",
                font=("courier", 24, "normal"),
            )
            pelota.dx = 0
            pelota.dy = 0

        # Control de colisiones paletas y pelota
        if (
            pelota.dx > 0
            and 345 < pelota.xcor() < 350
            and paleta_derecha.ycor() - 70 < pelota.ycor() < paleta_derecha.ycor() + 70
        ):
            pelota.setx(340)
            pelota.dx *= -1

        if (
            pelota.dx < 0
            and -350 < pelota.xcor() < -340
            and paleta_izquierda.ycor() - 90
            < pelota.ycor()
            < paleta_izquierda.ycor() + 90
        ):
            pelota.setx(-340)
            pelota.dx *= -1
