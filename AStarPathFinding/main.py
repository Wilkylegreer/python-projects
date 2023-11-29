import pygame
import math
from queue import PriorityQueue

width = 800
SCR = pygame.display.set_mode((width, width))
pygame.display.set_caption("A* Path FInding Algorithm")

RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
GREY = pygame.Color(128, 128, 128)
BLUE = pygame.Color(0, 0, 255)
DARKBLUE = pygame.Color(0, 0, 128)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
ORANGE = pygame.Color(255, 165, 0)
PINK = pygame.Color(255, 192, 203)
YELLOW = pygame.Color(255, 255, 0)


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def GetPos(self):
        return self.row, self.col

    def IsClosed(self):
        return self.color == RED

    def IsOpen(self):
        return self.color == GREEN

    def IsBarrier(self):
        return self.color == BLACK

    def IsStart(self):
        return self.color == ORANGE

    def IsEnd(self):
        return self.color == PINK

    def Reset(self):
        self.color = WHITE

    def MakeClosed(self):
        self.color = RED

    def MakeStart(self):
        self.color = ORANGE

    def MakeOpen(self):
        self.color = GREEN

    def MakeBarrier(self):
        self.color = BLACK

    def MakeEnd(self):
        self.color = PINK

    def MakePath(self):
        self.color = DARKBLUE

    def Draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.width))

    def UpdateNeighbors(self, grid):
        self.neighbors = []
        # Down
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].IsBarrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].IsBarrier():  # Up
            self.neighbors.append(grid[self.row - 1][self.col])

        # Right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].IsBarrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].IsBarrier():  # Left
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


def H(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def ReconstructPath(cameFrom, current, draw):
    while current in cameFrom:
        current = cameFrom[current]
        current.MakePath()
        draw()


def algorithm(draw, grid, start, end):
    count = 0
    openSet = PriorityQueue()
    openSet.put((0, count, start))
    cameFrom = {}
    gScore = {node: float("inf") for row in grid for node in row}
    gScore[start] = 0
    fScore = {node: float("inf") for row in grid for node in row}
    fScore[start] = H(start.GetPos(), end.GetPos())

    openSetHash = {start}

    while not openSet.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = openSet.get()[2]
        openSetHash.remove(current)

        if current == end:
            ReconstructPath(cameFrom, end, draw)
            end.MakeEnd()
            return True

        for neighbor in current.neighbors:
            tempGScore = gScore[current] + 1

            if tempGScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tempGScore
                fScore[neighbor] = tempGScore + \
                    H(neighbor.GetPos(), end.GetPos())
                if neighbor not in openSetHash:
                    count += 1
                    openSet.put((fScore[neighbor], count, neighbor))
                    openSetHash.add(neighbor)
                    neighbor.MakeOpen()
        draw()

        if current != start:
            current.MakeClosed()

    return False


def MakeGrid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


def DrawGrid(screen, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(screen, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(screen, GREY, (i * gap, 0), (i * gap, width))


def Draw(screen, grid, rows, width):
    screen.fill(WHITE)

    for row in grid:
        for node in row:
            node.Draw(screen)

    DrawGrid(screen, rows, width)
    pygame.display.update()


def GetClickedPos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(screen, width):
    ROWS = 50
    grid = MakeGrid(ROWS, width)

    start = None
    end = None

    run = True

    while run:
        Draw(screen, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # Left Click
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.MakeStart()

                elif not end and node != start:
                    end = node
                    end.MakeEnd()

                elif node != end and node != start:
                    node.MakeBarrier()
            elif pygame.mouse.get_pressed()[2]:  # Right Click
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos, ROWS, width)
                node = grid[row][col]
                node.Reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.UpdateNeighbors(grid)
                    algorithm(lambda: Draw(screen, grid,
                              ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = MakeGrid(ROWS, width)

    pygame.quit()


main(SCR, width)
