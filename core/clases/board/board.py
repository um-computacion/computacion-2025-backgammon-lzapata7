from ficha import ficha

class Board:
    
    def __init__(self):
        
        # Crear 24 puntos vacíos (listas)
        self.__points__ = []
        for i in range(24):
            self.__points__.append([])
        
        # Configurar posición inicial del juego
        self._setup_initial_position()
    
    def _setup_initial_position(self):
        
        # Limpiar el tablero
        for point in self.__points__:
            point.clear()