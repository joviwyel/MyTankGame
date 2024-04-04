import pygame
# 设置通用的属性
BG_COLOR = pygame.Color(0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
TEXT_COLOR = pygame.Color(255, 0, 0)


class Tank:
    '''
    坦克类
    '''

    def __init__(self) -> None:
        pass

    def display_tank(self):
        '''
        显示坦克
        '''
        pass

    def move(self):
        '''
        显示移动
        '''
        pass

    def shot(self):
        '''
        坦克射击
        '''
        pass


class MyTank(Tank):
    '''
    我方坦克类
    '''

    def __init__(self) -> None:
        pass


class EnemyTank(Tank):
    '''
    敌方坦克
    '''

    def __init__(self) -> None:
        pass


class Bullet:
    '''
    子弹类
    '''

    def __init__(self) -> None:
        pass

    def display_bullet(self):
        '''
        显示子弹
        '''
        pass

    def move_bullet(self):
        '''
        子弹移动
        '''
        pass


class Wall:
    def __init__(self) -> None:
        '''
        墙壁类
        '''
        pass

    def display_wall(self):
        '''
        显示墙壁
        '''
        pass


class Explosion:
    def __init__(self) -> None:
        '''
        爆炸类
        '''
        pass

    def display_explosion(self):
        '''
        显示爆炸
        '''
        pass


class Music:
    def __init__(self) -> None:
        '''
        音乐类
        '''
        pass

    def play_music(self):
        '''
        播放音乐
        '''
        pass


class MainGame:
    # 主窗口对象
    window = None

    def __init__(self) -> None:
        '''
        主窗口类
        '''
        pass

    def start_game(self):
        '''
        开始游戏
        '''
        # 初始化游戏窗口
        pygame.init()
        # 创建一个窗口
        MainGame.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
        # 设置窗口标题
        pygame.display.set_caption("坦克大战")
        # 刷新窗口
        while True:
            # 给窗口设置颜色
            MainGame.window.fill(BG_COLOR)
            # 添加提示文字
            # 1 要添加的提示文字
            num = 6
            text = self.get_text_surface(f'敌方坦克剩余数量{num}')
            # 2 如何把文字加上去

            pygame.Surface.blit(MainGame.window, text, (10, 10))
            MainGame.window.blit(text, (10, 10))
            # 刷新显示窗口
            pygame.display.update()

    def get_text_surface(self, text: str) -> None:
        ''''
        提取文字图片
        '''
        # 初始化字体模块
        pygame.font.init()
        # 创建字体
        font = pygame.font.SysFont('kaiti', 30)
        # 绘制文字信息
        text_surface = font.render(text, True, TEXT_COLOR)
        # 将绘制的文体信息返回
        return text_surface

    def end_game(self):
        '''
        结束游戏
        '''
        pass


# 调用
if __name__ == '__main__':
    MainGame().start_game()
