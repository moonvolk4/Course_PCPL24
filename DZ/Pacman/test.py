import pygame
import random
pygame.font.init()


class Pacman:
    def __init__(self, field, x, y):
        self.moving_way = "None"
        self.px = x
        self.py = y
        self.last_known_pos_x = 0
        self.last_known_pos_y = 0
        self.field = field
        self.score = 0
        self.lives = 3

        self.r_first_stage = pygame.image.load("pacman_first_stage.png")
        self.d_right_frst = pygame.transform.scale(self.r_first_stage, (25, 25))
        self.r_middle_stage = pygame.image.load("pacman_middle_stage.png")
        self.d_right_mdl = pygame.transform.scale(self.r_middle_stage, (25, 25))
        self.r_final_stage = pygame.image.load("pacman_final_stage.png")
        self.d_right_fnl = pygame.transform.scale(self.r_final_stage, (25, 25))

    def start_pacman_pos_x(self):
        start_x = self.px
        return start_x

    def start_pacman_pos_y(self):
        start_y = self.py
        return start_y

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.moving_way = "Up"
            if event.key == pygame.K_s:
                self.moving_way = "Down"
            if event.key == pygame.K_d:
                self.moving_way = "Right"
            if event.key == pygame.K_a:
                self.moving_way = "Left"

    def pacman_process_movements(self):
        if self.moving_way == "Up":
            if self.field[self.py - 1][self.px] != 1:
                if self.field[self.py - 1][self.px] == 2:
                    self.field[self.py][self.px] = 0
                    self.py = self.py - 1
                    self.score += 1
                    self.field[self.py][self.px] = 4
                else:
                    self.field[self.py][self.px] = 0
                    self.py = self.py - 1
                    self.field[self.py][self.px] = 4
            else:
                self.moving_way = "None"
        if self.moving_way == "Down":
            if self.field[self.py + 1][self.px] != 1:
                if self.field[self.py + 1][self.px] == 2:
                    self.field[self.py][self.px] = 0
                    self.py = self.py + 1
                    self.score += 1
                    self.field[self.py][self.px] = 4
                else:
                    self.field[self.py][self.px] = 0
                    self.py = self.py + 1
                    self.field[self.py][self.px] = 4
            else:
                self.moving_way = "None"
        if self.moving_way == "Right":
            if self.field[self.py][self.px + 1] != 1:
                if self.field[self.py][self.px + 1] == 2:
                    self.field[self.py][self.px] = 0
                    self.px = self.px + 1
                    self.score += 1
                    self.field[self.py][self.px] = 4
                else:
                    self.field[self.py][self.px] = 0
                    self.px = self.px + 1
                    self.field[self.py][self.px] = 4
            else:
                self.moving_way = "None"
        if self.moving_way == "Left":
            if self.field[self.py][self.px - 1] != 1:
                if self.field[self.py][self.px - 1] == 2:
                    self.field[self.py][self.px] = 0
                    self.px = self.px - 1
                    self.score += 1
                    self.field[self.py][self.px] = 4
                else:
                    self.field[self.py][self.px] = 0
                    self.px = self.px - 1
                    self.field[self.py][self.px] = 4
            else:
                self.moving_way = "None"


class Ghost:
    def __init__(self, field, x, y, pacman):
        self.dirs = {"up" : False,
                     "down" : False,
                     "left" : False,
                     "right" : False}
        self.field = field
        self.moving_way = {"up": False,
                     "down": False,
                     "left": False,
                     "right": False}
        self.gx = x
        self.gy = y
        self.pacman = pacman

    def ghost_possible_dirs(self):
        if self.field[self.gy - 1][self.gx] != 1:
            self.dirs["up"] = True
        else:
            self.dirs["up"] = False
        if self.field[self.gy + 1][self.gx] != 1:
            self.dirs["down"] = True
        else:
            self.dirs["down"] = False
        if self.field[self.gy][self.gx - 1] != 1:
            self.dirs["left"] = True
        else:
            self.dirs["left"] = False
        if self.field[self.gy][self.gx + 1] != 1:
            self.dirs["right"] = True
        else:
            self.dirs["right"] = False

    def guess(self):
        self.ghost_possible_dirs()
        ran_dir = random.randint(1, 4)
        if ran_dir == 1:
            self.moving_way["up"] = True
        else:
            self.moving_way["up"] = False
        if ran_dir == 2:
            self.moving_way["down"] = True
        else:
            self.moving_way["down"] = False
        if ran_dir == 4:
            self.moving_way["left"] = True
        else:
            self.moving_way["left"] = False
        if ran_dir == 3:
            self.moving_way["right"] = True
        else:
            self.moving_way["right"] = False

    def ghost_process_movements(self):
        # Ghost movement
        self.guess()
        if self.moving_way["up"]:
            if self.field[self.gy - 1][self.gx] != 1:
                if self.field[self.gy - 1][self.gx] == 2:
                    self.field[self.gy][self.gx] = 2
                    self.gy = self.gy - 1
                    self.field[self.gy][self.gx] = 3
                elif self.field[self.gy - 1][self.gx] == 4:
                    self.field[self.gy][self.gx] = 0
                    self.gy = self.gy - 1
                    self.field[self.gy][self.gx] = 3
                else:
                    self.field[self.gy][self.gx] = 0
                    self.gy = self.gy - 1
                    self.field[self.gy][self.gx] = 3
            else:
                self.moving_way["up"] = False
        if self.moving_way["down"]:
            if self.field[self.gy + 1][self.gx] != 1:
                if self.field[self.gy + 1][self.gx] == 2:
                    self.field[self.gy][self.gx] = 2
                    self.gy = self.gy + 1
                    self.field[self.gy][self.gx] = 3
                elif self.field[self.gy + 1][self.gx] == 4:
                    self.field[self.gy][self.gx] = 0
                    self.gy = self.gy - 1
                    self.field[self.gy][self.gx] = 3
                else:
                    self.field[self.gy][self.gx] = 0
                    self.gy = self.gy + 1
                    self.field[self.gy][self.gx] = 3
            else:
                self.moving_way["down"] = False
        if self.moving_way["right"]:
            if self.field[self.gy][self.gx + 1] != 1:
                if self.field[self.gy][self.gx + 1] == 2:
                    self.field[self.gy][self.gx] = 2
                    self.gx = self.gx + 1
                    self.field[self.gy][self.gx] = 3
                elif self.field[self.gy][self.gx + 1] == 4:
                    self.field[self.gy][self.gx] = 0
                    self.gy = self.gy - 1
                    self.field[self.gy][self.gx] = 3
                else:
                    self.field[self.gy][self.gx] = 0
                    self.gx = self.gx + 1
                    self.field[self.gy][self.gx] = 3
            else:
                self.moving_way["right"] = False
        if self.moving_way["left"]:
            if self.field[self.gy - 1][self.gx] != 1:
                if self.field[self.gy][self.gx - 1] == 2:
                    self.field[self.gy][self.gx] = 2
                    self.gx = self.gx - 1
                    self.field[self.gy][self.gx] = 3
                elif self.field[self.gy][self.gx - 1] == 4:
                    self.field[self.gy][self.gx] = 0
                    self.gy = self.gy - 1
                    self.field[self.gy][self.gx] = 3
                else:
                    self.field[self.gy][self.gx] = 0
                    self.gx = self.gx - 1
                    self.field[self.gy][self.gx] = 3
            else:
                self.moving_way["left"] = False


class Field:
    def __init__(self, field):
        file = open(field)
        lines = file.readlines()
        self.field = []
        for line in lines:
            lst = list(map(int, line.split(" ")))
            self.field.append(lst)
        print(self.field)
        self.height = len(self.field)
        self.width = len(self.field[0])
        for y in range(self.height):
            for x in range(self.width):
                if self.field[y][x] == 4:
                    self.pacman = Pacman(self.field, x, y)
                if self.field[y][x] == 3:
                    self.ghost = Ghost(self.field, x, y, self.pacman)

    def draw(self, sc):
        for y in range(self.height):
            for x in range(self.width):
                if self.field[y][x] == 0:
                    color = (100, 100, 100)
                    pygame.draw.rect(sc, color,
                                     (x * 30, y * 30, 30, 30))
                if self.field[y][x] == 1:
                    color = (0, 0, 0)
                    pygame.draw.rect(sc, color,
                                     (x * 30, y * 30, 30, 30))
                if self.field[y][x] == 4:
                    color = (100, 100, 100)
                    pygame.draw.rect(sc, color,
                                     (x * 30, y * 30, 30, 30))
                    color = (255, 255, 0)
                    pygame.draw.circle(sc, color,
                                     (x * 30 + 15, y * 30 + 15), 15)
                if self.field[y][x] == 2:
                    color = (100, 100, 100)
                    pygame.draw.rect(sc, color,
                                     (x * 30, y * 30, 30, 30))
                    color = (250, 250, 250)
                    pygame.draw.circle(sc, color,
                                     (x * 30 + 15, y * 30 + 15), 5)
                if self.field[y][x] == 3:
                    color = (100, 100, 100)
                    pygame.draw.rect(sc, color,
                                     (x * 30, y * 30, 30, 30))
                    color = (0, 255, 0)
                    pygame.draw.circle(sc, color,
                                     (x * 30 + 15, y * 30 + 15), 15)

                myfont = pygame.font.SysFont('Comic Sans MS', 30)
                textsurface = myfont.render(f"Score: {str(self.pacman.score)}", False, (255, 255, 255))
                sc.blit(textsurface, (0, 0))


pygame.init()
field = Field("field.txt")
sc = pygame.display.set_mode((field.width * 30,
                              field.height * 30))
clock = pygame.time.Clock()
is_on = True
while is_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           is_on = False
        field.pacman.process_events(event)
    sc.fill((255, 255, 255))
    field.pacman.pacman_process_movements()
    field.ghost.ghost_process_movements()
    field.draw(sc)
    pygame.display.flip()
    clock.tick(5)
