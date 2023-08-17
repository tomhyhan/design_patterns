from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def build_game(self):
        pass


class TextGame(Game):
    def build_game(self):
        return TextGameMode()

class ScreenGame(Game):
    def build_game(self):
        return ScreenGameMode()

class GameMode(ABC):
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def score(self):
        pass
    
class TextGameMode(GameMode):
    def play(self):
        print("playing text game")
    
    def score(self):
        print("score is: 50")

class ScreenGameMode(GameMode):
    def play(self):
        print("playing screen game")

    def score(self):
        print("score is: 90")
        
def clientcode(factory):
    game = factory.build_game()
    game.play()
    game.score()

textgame = TextGame()
clientcode(textgame)

screengame = ScreenGame()
clientcode(screengame)