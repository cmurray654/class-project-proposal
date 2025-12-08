import pygame
import random
from collections import deque
from dataclasses import dataclass


# ==========================
# Configuration
# ==========================
CELL_SIZE = 28 # pixels per cell
COLS = 25 # maze width in cells
ROWS = 19 # maze height in cells
MARGIN = 20 # outer padding for drawing
LINE_WIDTH = 2 # wall thickness
PLAYER_RADIUS = CELL_SIZE // 3
FPS = 60


BG_COLOR = (18, 18, 20)
WALL_COLOR = (230, 230, 235)
START_COLOR = (0, 160, 120)
GOAL_COLOR = (220, 80, 90)
PLAYER_COLOR = (90, 170, 255)
HINT_COLOR = (255, 215, 0)
TEXT_COLOR = (235, 235, 240)
WIN_OVERLAY = (0, 0, 0, 180)


WIDTH = COLS * CELL_SIZE + MARGIN * 2
HEIGHT = ROWS * CELL_SIZE + MARGIN * 2


DIRS = {
'N': (-1, 0),
'S': (1, 0),
'W': (0, -1),
'E': (0, 1)
}
OPPOSITE = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}


@dataclass
class Cell:
r: int
c: int
walls: dict


@staticmethod
def with_all_walls(r: int, c: int):
return Cell(r, c, {'N': True, 'S': True, 'W': True, 'E': True})




class Maze:
def __init__(self, rows: int, cols: int):
self.rows = rows
self.cols = cols
self.grid = [[Cell.with_all_walls(r, c) for c in range(cols)] for r in range(rows)]
self._generate()


def _in_bounds(self, r: int, c: int) -> bool:
return 0 <= r < self.rows and 0 <= c < self.cols


def _neighbors(self, r: int, c: int):
for d, (dr, dc) in DIRS.items():
nr, nc = r + dr, c + dc
if self._in_bounds(nr, nc):
yield d, self.grid[nr][nc]


def _remove_wall(self, a: Cell, b: Cell, direction: str):
a.walls[direction] = False
b.walls[OPPOSITE[direction]] = False


Game().run()