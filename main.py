import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720]) # Tamanho da tela do jogo

title = pygame.display.set_caption("Footbal Pong") # titulo do jogo

field = pygame.image.load("assets/field.png") # Adicionando imagem de background no jogo

player1 = pygame.image.load("assets/player1.png") # adicionando imagem do player
player1_y = 310
player1_moveup = False
player1_movedown = False

player2 = pygame.image.load("assets/player2.png")# add player 2
player2_x = 1130

ball = pygame.image.load("assets/ball.png")
ball_x = 617
ball_y = 340

def move_ball():
    global ball_x
    global ball_y

    ball_x += 5

def draw():
    window.blit(field, (0, 0))  # Carregando imagem e alinhado a mesma na janela
    window.blit(player1, (50, player1_y))  # carregando player
    window.blit(player2, (player2_x, 310))  # Carregando Plyer 2
    window.blit(ball, (ball_x, ball_y)) # Carrega a bola do Jogo


loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_moveup = True
            if event.key == pygame.K_s:
                player1_movedown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_moveup = False
            if event.key == pygame.K_s:
                player1_movedown = False

    draw()
    move_ball()
    pygame.display.update()  # Atualiza a tela no loop

