'''
Function:
    Python小游戏合集
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import sys
import warnings
from PyQt5.QtWidgets import QApplication
if __name__ == '__main__':
    from core import *
else:
    from .core import *
warnings.filterwarnings('ignore')


'''Python实用工具集'''
class CPGames():
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.supported_games = self.initialize()
    '''执行对应的小程序'''
    def execute(self, game_type=None, config={}):
        assert game_type in self.supported_games, f'unsupport game_type {game_type}...'
        qt_games = ['tetris', 'gobang']
        if game_type in qt_games:
            app = QApplication(sys.argv)
            client = self.supported_games[game_type](**config)
            client.show()
            sys.exit(app.exec_())
        else:
            client = self.supported_games[game_type](**config)
            client.run()
    '''初始化'''
    def initialize(self):
        return {
            'ski': SkiGame,
            'maze': MazeGame,
            'gobang': GobangGame,
            'tetris': TetrisGame,
            'pacman': PacmanGame,
            'gemgem': GemGemGame,
            'tankwar': TankWarGame,
            'sokoban': SokobanGame,
            'pingpong': PingpongGame,
            'trexrush': TRexRushGame,
            'bomberman': BomberManGame,
            'whacamole': WhacAMoleGame,
            'catchcoins': CatchCoinsGame,
            'flappybird': FlappyBirdGame,
            'angrybirds': AngryBirdsGame,
            'magictower': MagicTowerGame,
            'aircraftwar': AircraftWarGame,
            'bunnybadger': BunnyBadgerGame,
            'minesweeper': MineSweeperGame,
            'greedysnake': GreedySnakeGame,
            'puzzlepieces': PuzzlePiecesGame,
            'towerdefense': TowerDefenseGame,
            'bloodfootball': BloodFootballGame,
            'alieninvasion': AlienInvasionGame,
            'breakoutclone': BreakoutcloneGame,
            'twentyfourpoint': TwentyfourPointGame,
            'flipcardbymemory': FlipCardByMemoryGame,
            'twozerofoureight': TwoZeroFourEightGame,
            'voicecontrolpikachu': VoiceControlPikachuGame,
        }
    '''获得所有支持的游戏信息'''
    def getallsupported(self):
        return {value.game_type: key for key, value in self.supported_games.items()}
    '''str'''
    def __str__(self):
        return 'Welcome to use CPGames!\nYou can visit https://github.com/CharlesPikachu/Games for more details.'


'''run'''
if __name__ == '__main__':
    import random
    games_client = CPGames()
    all_supports = games_client.getallsupported()
    games_client.execute(random.choice(list(all_supports.values())))