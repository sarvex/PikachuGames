'''
Function:
    工具函数
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''


'''导入关卡文件'''
def loadLevel(levelpath):
    brick_positions = []
    fp = open(levelpath, 'r', encoding='utf-8')
    y = -1
    for line in fp:
        if line.strip() and not (line.startswith('#')):
            y += 1
            brick_positions.extend([x, y] for x, c in enumerate(line) if c == 'B')
    return brick_positions