'''
Function:
    游戏结束界面
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import pygame
from .....utils import QuitGame


'''游戏结束界面'''
def GameEndIterface(screen, sounds, showScore, score, number_images, bird, pipe_sprites, backgroud_image, other_images, base_pos, cfg):
    sounds['die'].play()
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                QuitGame()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_SPACE, pygame.K_UP]:
                    return
        boundary_values = [0, base_pos[-1]]
        bird.update(boundary_values, float(clock.tick(cfg.FPS))/1000.)
        screen.blit(backgroud_image, (0, 0))
        pipe_sprites.draw(screen)
        screen.blit(other_images['base'], base_pos)
        showScore(cfg, screen, score, number_images)
        bird.draw(screen)
        pygame.display.update()
        clock.tick(cfg.FPS)