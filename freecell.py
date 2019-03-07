from deck import Deck

class Freecell(object):

    selection = None

    def __init__(self):
        self.deck = Deck()
        self.board = {
            '1':[],
            '2':[],
            '3':[],
            '4':[],
            '5':[],
            '6':[],
            '7':[],
            '8':[],
            'F1':[],
            'F2':[],
            'F3':[],
            'F4':[],
            'C':[],
            'H':[],
            'D':[],
            'S':[],
            }
        i = 1
        while self.deck.deck:
            if i > 8:
                i = 1
            self.board[str(i)].append(self.deck.deck.pop(0))
            i+=1

    def __str__(self):
        gameState = str(self.board['F1'][0]) if self.board['F1'] else '[]'
        gameState+='  '
        gameState+=str(self.board['F2'][0]) if self.board['F2'] else '[]'
        gameState+='  '
        gameState+=str(self.board['F3'][0]) if self.board['F3'] else '[]'
        gameState+='  '
        gameState+=str(self.board['F4'][0]) if self.board['F4'] else '[]'
        gameState+= '                 '
        gameState+= str(self.board['C'][-1]) if self.board['C'] else '[]'
        gameState+='  '
        gameState+=str(self.board['H'][-1]) if self.board['H'] else '[]'
        gameState+='  '
        gameState+=str(self.board['D'][-1]) if self.board['D'] else '[]'
        gameState+='  '
        gameState+=str(self.board['S'][-1]) if self.board['S'] else '[]'
        gameState+='\n\n'

        for i in range(1,9):
            gameState+=str(i)+': '
            for card in self.board[str(i)]:
                gameState+=card.shortPrint()+', '
            gameState+='\n'
        return gameState


game = Freecell()

def move(fro,to):
    if type(fro) is int:
        fro = str(fro)
    if type(to) is int:
        to = str(to)
    if not game.board[fro]:
        return None
    moving = game.board[fro][-1]
    if to == top:
        to = moving.suit
        if not game.board[to] and moving.number is 1:
            game.board[to].append(game.board[fro].pop(-1))
        elif game.board[to][-1].number == moving.number-1:
            game.board[to].append(game.board[fro].pop(-1))
        else:
            return None
    elif to == free:
        for cell in ['F1','F2','F3','F4']:
            if not game.board[cell]:
                game.board[cell].append(game.board[fro].pop(-1))
                break
    elif to in list('12345678'):
        print(to)
        if not game.board[to]:
            game.board[to].append(game.board[fro].pop(-1))
        elif game.board[to][-1].colour != moving.colour and game.board[to][-1].number == moving.number+1:
            game.board[to].append(game.board[fro].pop(-1))
        else:
            return None
    else:
        return None
    print(game)

free = 'free'
top = 'top'
