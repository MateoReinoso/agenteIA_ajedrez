# Cerebro de la maquina el cual permite y evalua los movimientos del usuario para jugar contra la maquina

import chess
import math

class AgenteMinimax:
    def __init__(self, profundidad=2):
        self.profundidad = profundidad  # Qué tan lejos puede "ver" el robot

    def evaluar_tablero(self, tablero):
        # Asignamos puntos a cada pieza
        valores = {
            chess.PAWN: 1,    # Peón
            chess.KNIGHT: 3,  # Caballo
            chess.BISHOP: 3,  # Alfil
            chess.ROOK: 5,    # Torre
            chess.QUEEN: 9,   # Reina
            chess.KING: 0     # Rey (no se cuenta en puntos aquí)
        }

        puntuacion = 0

        # Sumamos puntos por cada pieza en el tablero
        for pieza in tablero.piece_map().values():
            valor = valores.get(pieza.piece_type, 0)
            if pieza.color == chess.WHITE:
                puntuacion += valor
            else:
                puntuacion -= valor

        return puntuacion

    def minimax(self, tablero, profundidad, maximizando):
        # Si ya vimos suficiente o el juego terminó
        if profundidad == 0 or tablero.is_game_over():
            return self.evaluar_tablero(tablero), None

        jugadas_posibles = list(tablero.legal_moves)
        mejor_jugada = None

        if maximizando:
            mejor_valor = -math.inf
            for jugada in jugadas_posibles:
                tablero.push(jugada)  # Hacemos la jugada
                valor, _ = self.minimax(tablero, profundidad - 1, False)
                tablero.pop()  # Deshacemos la jugada
                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_jugada = jugada
            return mejor_valor, mejor_jugada

        else:  # El jugador contrario
            peor_valor = math.inf
            for jugada in jugadas_posibles:
                tablero.push(jugada)
                valor, _ = self.minimax(tablero, profundidad - 1, True)
                tablero.pop()
                if valor < peor_valor:
                    peor_valor = valor
                    mejor_jugada = jugada
            return peor_valor, mejor_jugada

    def obtener_jugada(self, tablero):
        # Aquí usamos todo lo anterior para elegir la mejor jugada
        _, mejor_jugada = self.minimax(tablero, self.profundidad, tablero.turn == chess.WHITE)
        return mejor_jugada
