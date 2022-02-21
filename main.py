import pygame
import os
import random

pygame.init()

# Constants
SCREEN_H = 600
SCREEN_W = 1100
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))

IDLE = pygame.image.load(os.path.join("runner/idle", "Idle__000.png"))
IDLE = pygame.transform.scale(IDLE, (80, 120))

RUN = [pygame.image.load(os.path.join("runner/run", "Run__000.png")),
       pygame.image.load(os.path.join("runner/run", "Run__001.png")),
       pygame.image.load(os.path.join("runner/run", "Run__002.png")),
       pygame.image.load(os.path.join("runner/run", "Run__003.png")),
       pygame.image.load(os.path.join("runner/run", "Run__004.png")),
       pygame.image.load(os.path.join("runner/run", "Run__005.png")),
       pygame.image.load(os.path.join("runner/run", "Run__006.png")),
       pygame.image.load(os.path.join("runner/run", "Run__007.png")),
       pygame.image.load(os.path.join("runner/run", "Run__008.png")),
       pygame.image.load(os.path.join("runner/run", "Run__009.png"))]

JUMP = [pygame.image.load(os.path.join("runner/jump", "Jump__000.png")),
        pygame.image.load(os.path.join("runner/jump", "Jump__001.png")),
        pygame.image.load(os.path.join("runner/jump", "Jump__002.png")),
        pygame.image.load(os.path.join("runner/jump", "Jump__003.png")),
        pygame.image.load(os.path.join("runner/jump", "Jump__004.png")),
        pygame.image.load(os.path.join("runner/jump", "Jump__005.png")),
        pygame.image.load(os.path.join("runner/jump", "Jump__006.png")),
        pygame.image.load(os.path.join("runner/jump", "Jump__007.png")),
        pygame.image.load(os.path.join("runner/jump", "Jump__008.png")),
        pygame.image.load(os.path.join("runner/jump", "Jump__009.png"))]

SLIDE = [pygame.image.load(os.path.join("runner/slide", "Slide__000.png")),
         pygame.image.load(os.path.join("runner/slide", "Slide__001.png")),
         pygame.image.load(os.path.join("runner/slide", "Slide__002.png")),
         pygame.image.load(os.path.join("runner/slide", "Slide__003.png")),
         pygame.image.load(os.path.join("runner/slide", "Slide__004.png")),
         pygame.image.load(os.path.join("runner/slide", "Slide__005.png")),
         pygame.image.load(os.path.join("runner/slide", "Slide__006.png")),
         pygame.image.load(os.path.join("runner/slide", "Slide__007.png")),
         pygame.image.load(os.path.join("runner/slide", "Slide__008.png")),
         pygame.image.load(os.path.join("runner/slide", "Slide__009.png"))]

DEAD = [pygame.image.load(os.path.join("runner/dead", "Dead__000.png")),
        pygame.image.load(os.path.join("runner/dead", "Dead__001.png")),
        pygame.image.load(os.path.join("runner/dead", "Dead__002.png")),
        pygame.image.load(os.path.join("runner/dead", "Dead__003.png")),
        pygame.image.load(os.path.join("runner/dead", "Dead__004.png")),
        pygame.image.load(os.path.join("runner/dead", "Dead__005.png")),
        pygame.image.load(os.path.join("runner/dead", "Dead__006.png")),
        pygame.image.load(os.path.join("runner/dead", "Dead__007.png")),
        pygame.image.load(os.path.join("runner/dead", "Dead__008.png")),
        pygame.image.load(os.path.join("runner/dead", "Dead__009.png"))]

FLY = [pygame.image.load(os.path.join("runner/fly", "fly1.png")),
       pygame.image.load(os.path.join("runner/fly", "fly2.png"))]
FLY[0] = pygame.transform.scale(FLY[0], (90, 60))
FLY[1] = pygame.transform.scale(FLY[1], (90, 60))

BIG_SPIKE = [pygame.image.load(os.path.join("runner/spikes", "spike A.png")),
             pygame.image.load(os.path.join("runner/spikes", "spike B.png"))]
BIG_SPIKE[0] = pygame.transform.scale(BIG_SPIKE[0], (90, 90))
BIG_SPIKE[1] = pygame.transform.scale(BIG_SPIKE[1], (90, 90))

SMALL_SPIKE = [pygame.image.load(os.path.join("runner/spikes", "spike C.png")),
               pygame.image.load(os.path.join("runner/spikes", "spike D.png"))]
SMALL_SPIKE[0] = pygame.transform.scale(SMALL_SPIKE[0], (40, 80))
SMALL_SPIKE[1] = pygame.transform.scale(SMALL_SPIKE[1], (40, 80))

BG = pygame.image.load(os.path.join("runner/bg", "Desert_BG.png"))
BG = pygame.transform.scale(BG, (1200, 600))


# Main character
class Hero:
    X_POS = 80
    Y_POS = 390
    Y_POS_SLIDE = 420
    JUMP_V = 9

    def __init__(self):
        self.run_img = RUN
        self.jump_img = JUMP
        self.slide_img = SLIDE
        self.idle_img = IDLE
        self.dead_img = DEAD

        self.hero_run = True
        self.hero_jump = False
        self.hero_slide = False

        self.step_index1 = 0
        self.step_index2 = 0
        self._index = 0
        self.jump_tick = 0
        self.jump_v = self.JUMP_V
        self.image = self.run_img[0]
        self.image = pygame.transform.scale(self.image, (100, 130))
        self.hero_rect = self.image.get_rect()
        self.hero_rect.x = self.X_POS
        self.hero_rect.y = self.Y_POS

    def update(self, userInput):
        if self.hero_run:
            self.run()
        if self.hero_jump:
            self.jump()
        if self.hero_slide:
            self.slide()

        if self.step_index1 >= 20:
            self.step_index1 = 0

        if userInput[pygame.K_UP] and not self.hero_jump and self.hero_rect.y >= 390:
            self.hero_run = False
            self.hero_jump = True
            self.hero_slide = False
        elif userInput[pygame.K_DOWN] and not self.hero_jump:
            self.hero_run = False
            self.hero_jump = False
            self.hero_slide = True
        elif not (self.hero_jump or userInput[pygame.K_DOWN]):
            self.hero_run = True
            self.hero_jump = False
            self.hero_slide = False

    def run(self):
        self.image = self.run_img[self.step_index1 // 2]
        self.image = pygame.transform.scale(self.image, (100, 130))
        self.hero_rect = self.image.get_rect()
        self.hero_rect.x = self.X_POS
        self.hero_rect.y = self.Y_POS
        self.step_index1 += 1

    def jump(self):
        self.image = self.jump_img[self.step_index2 // 3]
        self.image = pygame.transform.scale(self.image, (100, 130))
        self.step_index2 += 1
        if self.hero_jump:
            self.hero_rect.y -= self.jump_v * 4
            self.jump_v -= 0.8
        if self.jump_v <= self.JUMP_V * -1:
            self.hero_jump = False
            self.jump_v = self.JUMP_V
            self.step_index2 = 0

    def slide(self):
        self.image = self.slide_img[self.step_index1 // 2]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.hero_rect = self.image.get_rect()
        self.hero_rect.x = self.X_POS
        self.hero_rect.y = self.Y_POS_SLIDE
        self.step_index1 += 1

    def draw(self, screen):
        screen.blit(self.image, (self.hero_rect.x, self.hero_rect.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_W

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallSpike(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 440


class BigSpike(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 430


class Fly(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 350
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, run
    run = True
    clock = pygame.time.Clock()
    player = Hero()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    obstacles = []
    deaths = 0
    font = pygame.font.Font('freesansbold.ttf', 20)

    def score():
        global points, game_speed
        points += 0.25
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(int(points)), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg < -image_width:
            x_pos_bg = 0
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        clock.tick(30)
        userInput = pygame.key.get_pressed()

        background()

        player.draw(SCREEN)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallSpike(SMALL_SPIKE))
            elif random.randint(0, 2) == 1:
                obstacles.append(BigSpike(BIG_SPIKE))
            elif random.randint(0, 2) == 2:
                obstacles.append(Fly(FLY))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.hero_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                deaths += 1
                menu(deaths)

        score()
        player.update(userInput)

        pygame.display.update()


def menu(deaths):
    global points, run
    run = True
    SCREEN.fill((255, 255, 255))
    while run:
        font = pygame.font.Font('freesansbold.ttf', 20)

        if deaths == 0:
            text = font.render("Press any key to start.", True, (0, 0, 0))
        elif deaths > 0:
            text = font.render("Press any key to restart.", True, (0, 0, 0))
            scr = font.render("Your score: " + str(int(points)), True, (0, 0, 0))
            s_rect = scr.get_rect()
            s_rect.center = (SCREEN_W // 2, SCREEN_H // 2 + 50)
            SCREEN.blit(scr, s_rect)
        t_rect = text.get_rect()
        t_rect.center = (SCREEN_W // 2, SCREEN_H // 2)
        SCREEN.blit(text, t_rect)
        SCREEN.blit(IDLE, (SCREEN_W // 2 - 40, SCREEN_H // 2 - 160))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                main()

menu(deaths=0)



