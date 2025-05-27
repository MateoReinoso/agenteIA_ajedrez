# app.py

import chess
from agente.motro_ajedrez import AgenteMinimax
from deteccion.vision import obtener_jugada_humana
from interfaz.mostrar_jugada import mostrar_jugada

# Creamos un tablero de ajedrez vacío (con todas las piezas bien puestas)
tablero = chess.Board()

# Creamos nuestro robot pensador
agente = AgenteMinimax(profundidad=2)

# Bucle: el juego sigue hasta que termine (jaque mate, empate, etc.)
while not tablero.is_game_over():
    print(tablero)  # Muestra el tablero en texto

    # Turno del humano
    jugada = obtener_jugada_humana()

    try:
        tablero.push_uci(jugada)  # Intenta aplicar la jugada escrita
    except:
        print("❌ Esa jugada no es válida. Intenta otra.")
        continue  # Vuelve a pedir jugada si está mal escrita

    # Verificamos si ya terminó el juego después de la jugada humana
    if tablero.is_game_over():
        break

    # Turno del robot
    jugada_robot = agente.obtener_jugada(tablero)
    mostrar_jugada(jugada_robot)
    tablero.push(jugada_robot)  # Aplicamos la jugada del robot

# Fuera del bucle: el juego terminó
print("🎉 El juego ha terminado.")
print("Resultado:", tablero.result())
