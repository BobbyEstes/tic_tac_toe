class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
       
class Game:
    def __init__(self):
        self.token_pos = [" "," "," "," "," "," "," "," "," "]
        self.board = self.__draw_board()
          
    def __draw_board(self):
        tp = self.token_pos
        board = f"{tp[0]}|{tp[1]}|{tp[2]}\n"
        board += f"{tp[3]}|{tp[4]}|{tp[5]}\n"
        board += f"{tp[6]}|{tp[7]}|{tp[8]}"
        return board

    def __repr__(self):
        return self.board
       
    def move(self, x, y, player):
        index = self.__conv(x, y)
        if self.__check_move(index):
            self.token_pos[index] = player.token
            self.board = self.__draw_board()
        else:
            return False
        
    def __conv(self, x, y):
        x -= 1
        y = (y-1)*3
        index = x + y
        return index

    def __check_move(self,index):
        return True if self.token_pos[index] == " " else False

    def chk_brd(self):
        tp = self.token_pos
        wins = [(tp[0], tp[1], tp[2]), (tp[3], tp[4], tp[5]), (tp[6], tp[7], tp[8]), (tp[0], tp[3], tp[6]),\
            (tp[1], tp[4], tp[7]), (tp[2], tp[5], tp[8]), (tp[0], tp[4], tp[8]), (tp[2], tp[4], tp[6])]
        for win in wins:
            if self.__get_win(win) in ["X", "O"]:
                return win[0]

    def __get_win(self, args):
        if all(x == args[0] and x in ["X", "O"] for x in args):
            return args[0]

    def __is_full(self):
        return False if " " in self.token_pos else True
        
    def is_game_over(self):
        return True if self.__is_full() else False


while True:
    i = 0; t = ""; p = ["", ""]
    while i < 2:
        player = input(f"Enter player #{i+1} name ")
        if player != "":
            while t == "":
                t = input("Enter player #1 token X or O ").upper()
                if t not in ["X", "O"]:
                    t = ""
                                 
            p[i] = Player(player, t)
            t = "X" if t == "O" else "O"
            i+=1 
                    
    game = Game(); game_over = False
    while True:
        for x in p:
            while True:
                coordinates = []; i=0; a=["X", "Y"]
                while i < 2:
                    try:
                        c = input(f"Enter your {a[i]} coordinate for {x.name} ")
                        if c.lower() == "done":
                            game_over = True
                            break
                        c = int(c)
                        
                        if c in range(1, 4):
                            coordinates.append(c) 
                            i+=1                           
                    except:
                        continue
                if game_over:
                    break
                check = ""
                if len(coordinates) == 2:
                    check = game.move(coordinates[0], coordinates[1], x)
                    if check != False:
                        print(game)
                        break
                    else:
                        print("That slot already used")
            
            win = game.chk_brd()
            if win in ["X", "O"]:
                for x in p:
                    if x.token == win:
                        print(f"The winner is {x.name}")
                        game_over = True
                        break
            else:                    
                full = game.is_game_over()
                if full:
                    print("Tie Game")
                    game_over = True
                    break
            if game_over:
                break
        if game_over:
            break
    if game_over:
        again = ""
        while again not in ["yes", "no"]:
            again = input("Game over. Play again? ").lower()
        if again == "no":
            break
                










        








