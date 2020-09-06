import numpy as np

# define some colors (R, G, B)
WHITE = np.array((255, 255, 255))
BLACK = np.array((0, 0, 0))
DARKGREY = np.array((40, 40, 40))
LIGHTGREY = np.array((100, 100, 100))
GREEN = np.array((0, 255, 0))
RED = np.array((255, 0, 0))
BLUE = np.array((0, 0, 255))
YELLOW = np.array((255, 255, 0))

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 10
TITLE = "Quantum Shenanigans"
BGCOLOR = DARKGREY

TILESIZE = 64
GRIDWIDTH = WIDTH // TILESIZE
GRIDHEIGHT = HEIGHT // TILESIZE
