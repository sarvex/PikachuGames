'''
Function:
    游戏开始界面
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import pygame
from ..sprites import Dinosaur
from .....utils import QuitGame


'''游戏开始界面'''
def GameStartInterface(screen, sounds, cfg, resource_loader):
    dino = Dinosaur(resource_loader.images['dino'])
    ground = resource_loader.images['ground'].subsurface((0, 0), (83, 19))
    rect = ground.get_rect()
    rect.left, rect.bottom = cfg.SCREENSIZE[0]/20, cfg.SCREENSIZE[1]
    clock = pygame.time.Clock()
    press_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_SPACE, pygame.K_UP]:
                    press_flag = True
                    dino.jump(sounds)
        dino.update()
        screen.fill(cfg.BACKGROUND_COLOR)
        screen.blit(ground, rect)
        dino.draw(screen)
        pygame.display.update()
        clock.tick(cfg.FPS)
        if (not dino.is_jumping) and press_flag:
            return True