
from random import randint

class Die():
    """
    This is the class which is responsible for representing a dice and to get a value when it is rolled.


    Attributes
    -----------
    value : int
       the dice value when it is rolled

    Methods
    -------
    get_value():
        this function returns the dice value

    roll():
        it gives a random dice value.
   """

    def __init__(self,val=1):
        """
        it is the constructor of this class which constructs all the required for the die object

        """
        self._value = 1
        self.roll()

    #setter and getter methods for attribute value.
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value

    def get_value(self) -> int:

        return self._value

    def roll(self):

        self._value = randint(1, 6)

    def __str__(self):
        return str(self._value)

    def __add__(self,other):
        return self._value+other._value



class DiceCup():

    """
    This class handles five objects of class Die,
    and it is responsible for bank and release of dice individually.

    parameter :
        no_dice(int): number of dices a player plays.

    """

    def __init__(self, no_dice: int):
        """
        this constructor constructs the dice attribute with the objects of Die.

        """

        self._vardice = []
        for _ in range(no_dice):
            self._vardice.append(Die())
        self._checking=[]
        for _ in range(no_dice):
            self._checking.append(False)
        

    def roll(self):
        """
        this is responsible for the rolling of dice if it isn't banked.

        parameter
        ------
        None

        returns : None
        """

        for j in range(len(self._checking)):
            if self._checking[j] == False:
                self._vardice[j].roll()

    def value(self, position:int)->int :
        """
        this method returns the value at the given index position .

        parameter:
        ---------------
        position : int
            required index

        returns :  int
            returns dice value
        """
        return self._vardice[position].get_value()

    def bank(self, position:int):
        """
        this function banks the given position
        """
        self._checking[position] = True

    def is_banked(self,position:int)->bool:
        """
        this function checks whether the given die is banked or not.

        """
        return self._checking[position]

    def release(self,position:int):
        """
        this function is used for releasing dice.
        """
        self._checking[position] = False

    def release_all(self):
        """
        this function is un-banks all the banked dices.
        """
        for j in range(len(self._checking)):
            self._checking[j]=False


class ShipOfFoolsGame():

    """
    This class is responsible for the game logic ,and it has the
    ability to play a round  of the game resulting in a score.
    There is a property for this class that it tells what accumulated score results in a winning state,for example 21.

    parameters:
    ----------
    cup : dicecup object
        This object is initialized in this parameters
    Methods:

    round():
        In this function all the constraints are taken after the roll of dice.

    """

    def __init__(self):
        """
        This constructor constructs the cup parameter with the dicecup object.

        parameters:
            None
        """
        self._cup = DiceCup(5)
        self._final_score = 21
    def round(self)->int:

        self._winning_score=0
        ship = False
        captain = False
        crew = False
        self._cup._checking=[False for _ in range(len(self._cup._checking))]
        for _ in range(3):

            self._cup.roll()
                 
            if not ship:
                for dice_value in range(len(self._cup._vardice)):
                    if self._cup.value(dice_value)==6:
                        self._cup.bank(dice_value)
                        ship=True
                        break
            if not captain:
                for dice_value in range(len(self._cup._vardice)):
                    if self._cup.value(dice_value)==5:
                        self._cup.bank(dice_value)
                        captain=True
                        break
            if not crew:
                for dice_value in range(len(self._cup._vardice)):
                    if self._cup.value(dice_value)==4:
                        self._cup.bank(dice_value)
                        crew=True
                        break
            if ship and captain and crew:
                for dice_value in range(len(self._cup._vardice)):
                    if self._cup.value(dice_value)>3:
                        self._cup.bank(dice_value)
            rolled_dices=[]
            for dice in range(len(self._cup._vardice)):
                rolled_dices.append(self._cup.value(dice))
            print(f"rolled values {rolled_dices} ")
        rounds_list_values=[]
        for r_l in range(len(self._cup._vardice)):
            rounds_list_values.append(self._cup.value(r_l))
        print(f"after 3 rolls {rounds_list_values}")
        if ship  and captain and crew:
            for ref in range(len(self._cup._vardice)):
                self._winning_score+=self._cup.value(ref)
            self._winning_score-=15
        return self._winning_score



class Player():
    """
    This class is responsible for handling players info.

    parameters:
    ----------
    name : string
        player name
    start_score: int
        individual score of each player
    Methods:
    -------
    set_name():
    play_round():
    current_score():
    reset_score():
    """
    def __init__(self, namestring:str):
        """
        This constructor constructs name and the score of the each player.

        parameters:
            namestring:
                it will create a new string.
        """
        self._name = str()
        self._start_score = 0
        self.set_name(namestring)

    def set_name(self, namestring):
        """
        sets the player name.

        paremeters:
            namestring : player name
        """
        self._name = namestring

    def play_round(self,game:object):
        """
        This function plays a round of games for each player.
        parameters:
            game : object of ship of fools game.
        """
        self.object_game = game.round()

    @property
    def current_score(self):
        """
        This function displayes current scores of a player.

        """
        self._start_score += self.object_game

    def reset_score(self):
        """
        This function makes the player score to zero.

        """
        self._start_score = 0


class PlayRoom():
    """
    This class is responsible for handling a number of players and a game.
    Every round the room lets each player play and afterwards it checks if any of the player has reached the winning score

    Parameters:
            players : objects of list
            game : object

    Methods:
          set_game():
          add_player():
          reset_scores():
          play_round():
          game_finished():
          print_scores():
          print_winner():

    """

    def __init__(self):
        """
        This constructor constructs the game and player parameters.

        parameters:
            None
        """
        self._players = []

    def set_game(self,game):

        """This function constructs game as the object of class ship of fools."""
        self._game = game


    def add_player(self,player:list):

        """
        This function adds the player info.
        """
        self._players.append(player)

    def reset_scores(self):
        """
        This function makes the scores of all the players as zero.

        """
        i=0
        while i < len(self._players):
            self._players[i].play_round(self._game)
            i+=1

    def play_round(self):
        """
        this function is used to play a round of game for all the players.
        """
        for i in range(len(self._players)):
            self._players[i].play_round(self._game)
            self._game._cup.release_all()


    def game_finished(self)->bool:
        """
        This function checks whether any one of the player has reached the
        winning score or not.
        returns : boolean
            True/False
        """
        for player in self._players:
            if player._start_score >= self._game._final_score:
                return True
        else:
            return False

    def print_scores(self):
        """
        This function prints the scores of every player after the
        completion of every round.
        """
        for i in range(len(self._players)):
            self._players[i].current_score
            print("the {} _start_score:{}".format(self._players[i]._name,self._players[i]._start_score))

    def print_winner(self):
        """
        This function announces the winner of the game who scored
        more points among all the players.

        """

        winners_of_round = []
        winner=self._players[0]
        for player in self._players:
            if winner._start_score<player._start_score:
                winner=player
        for player in self._players:
            if winner._start_score == player._start_score:
                winners_of_round.append(player)
        if len(winners_of_round)==len(self._players):
            print("draw match")
        else:   
            for player in winners_of_round:
                print("winner is ",player._name)


if __name__ == "__main__":
    room = PlayRoom()
    room.set_game(ShipOfFoolsGame())
    room.add_player(Player("ching"))
    room.add_player(Player("chang"))
    room.add_player(Player("fung"))
    room.reset_scores()
    while not room.game_finished():
        room.play_round()
        room.print_scores()
    room.print_winner()



