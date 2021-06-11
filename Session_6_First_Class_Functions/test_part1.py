import pytest
import random
import string
import part1 
import math
import inspect
import re 
import os

README_CONTENT_CHECK_FOR = [
    'create cards',
    'royal flush',
    'straight flush',
    'four of a kind',
    'full house',
    'flush',
    'straight',
    'three of a kind',
    'two pair',
    'one pair',
    'high card',
    'game'
]

def test_part1_readme_exists():
    """ Checks if readme.md file exists    """    
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_part1_readme_100_words():
    """ Checks if Readme contains atleast 500 words """    
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 500 words"


def test_part1_readme_proper_description():
    """ Checks if important contents are being convered in readme    """    
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_part1_readme_file_for_more_than_10_hashes():
    """ Checks if we have done proper formating  """    
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_part1_function_name_had_cap_letter():
    """ Checks if all function in session5 has used any captial letters    """    
    functions = inspect.getmembers(part1, inspect.isfunction)
    for function in functions:        
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"



task1_ans = [(('spades', '2'),),
 (('spades', '3'),),
 (('spades', '4'),),
 (('spades', '5'),),
 (('spades', '6'),),
 (('spades', '7'),),
 (('spades', '8'),),
 (('spades', '9'),),
 (('spades', '10'),),
 (('spades', 'jack'),),
 (('spades', 'queen'),),
 (('spades', 'king'),),
 (('spades', 'ace'),),
 (('clubs', '2'),),
 (('clubs', '3'),),
 (('clubs', '4'),),
 (('clubs', '5'),),
 (('clubs', '6'),),
 (('clubs', '7'),),
 (('clubs', '8'),),
 (('clubs', '9'),),
 (('clubs', '10'),),
 (('clubs', 'jack'),),
 (('clubs', 'queen'),),
 (('clubs', 'king'),),
 (('clubs', 'ace'),),
 (('hearts', '2'),),
 (('hearts', '3'),),
 (('hearts', '4'),),
 (('hearts', '5'),),
 (('hearts', '6'),),
 (('hearts', '7'),),
 (('hearts', '8'),),
 (('hearts', '9'),),
 (('hearts', '10'),),
 (('hearts', 'jack'),),
 (('hearts', 'queen'),),
 (('hearts', 'king'),),
 (('hearts', 'ace'),),
 (('diamonds', '2'),),
 (('diamonds', '3'),),
 (('diamonds', '4'),),
 (('diamonds', '5'),),
 (('diamonds', '6'),),
 (('diamonds', '7'),),
 (('diamonds', '8'),),
 (('diamonds', '9'),),
 (('diamonds', '10'),),
 (('diamonds', 'jack'),),
 (('diamonds', 'queen'),),
 (('diamonds', 'king'),),
 (('diamonds', 'ace'),)]
task2_ans = [('spades', '2'),
 ('spades', '3'),
 ('spades', '4'),
 ('spades', '5'),
 ('spades', '6'),
 ('spades', '7'),
 ('spades', '8'),
 ('spades', '9'),
 ('spades', '10'),
 ('spades', 'jack'),
 ('spades', 'queen'),
 ('spades', 'king'),
 ('spades', 'ace'),
 ('clubs', '2'),
 ('clubs', '3'),
 ('clubs', '4'),
 ('clubs', '5'),
 ('clubs', '6'),
 ('clubs', '7'),
 ('clubs', '8'),
 ('clubs', '9'),
 ('clubs', '10'),
 ('clubs', 'jack'),
 ('clubs', 'queen'),
 ('clubs', 'king'),
 ('clubs', 'ace'),
 ('hearts', '2'),
 ('hearts', '3'),
 ('hearts', '4'),
 ('hearts', '5'),
 ('hearts', '6'),
 ('hearts', '7'),
 ('hearts', '8'),
 ('hearts', '9'),
 ('hearts', '10'),
 ('hearts', 'jack'),
 ('hearts', 'queen'),
 ('hearts', 'king'),
 ('hearts', 'ace'),
 ('diamonds', '2'),
 ('diamonds', '3'),
 ('diamonds', '4'),
 ('diamonds', '5'),
 ('diamonds', '6'),
 ('diamonds', '7'),
 ('diamonds', '8'),
 ('diamonds', '9'),
 ('diamonds', '10'),
 ('diamonds', 'jack'),
 ('diamonds', 'queen'),
 ('diamonds', 'king'),
 ('diamonds', 'ace')]

def check_task1():
    vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
    suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]
    #print(part1.DeckSingleLine(vals,suits))
    assert list(part1.decksingleline(vals,suits)) == task1_ans , 'Please check task1 function'


def check_task2():
    vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
    suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]
    assert list(part1.create_deck(vals,suits)) == task2_ans , 'Please check task2 function'

# check gamer
def check_poker_game():
    player1 = [('spades', 'A'),  ('spades', 'K'),  ('spades', 'Q'),  ('spades', 'J'), ('spades', '10'),]
    player2 = [('spades', 'A'),  ('hearts', 'K'),  ('diamonds', '2'),  ('spades', '4'), ('clubs', '3')]
    assert part1.poker_game(player1,player2) == 'Player1 WON' , 'Please Check you gamer function'
    

# check 10 functions
def check_royal_flush():
    player1 = [('spades', 'A'),  ('spades', 'K'),  ('spades', 'Q'),  ('spades', 'J'), ('spades', '10'),]
    assert part1.royal_flush(player1)['status'] == 1, 'Please Check you validity of royal flush'
    assert part1.royal_flush(player1)['Marks'] == 1 , 'Please Check you evaluation of royal flush'

def check_straight_flush():
    player1 = [('hearts', '10'),  ('hearts', '9'),  ('hearts', '8'),  ('hearts', '7'), ('hearts', '6')]
    assert part1.straight_flush(player1)['status'] == 1, 'Please Check you validity of straight_flush'
    assert part1.straight_flush(player1)['Marks'] == 40, 'Please Check you evaluation of straight_flush'

def check_four_of_a_kind():
    player1 = [('clubs', 'A'),  ('clubs', '7'),  ('hearts', '7'),  ('diamonds', '7'), ('spades', '7')]
    assert part1.four_of_a_kind(player1)['status'] == 1, 'Please Check you validity of four_of_a_kind'
    assert part1.four_of_a_kind(player1)['Marks'] == 28, 'Please Check you evaluation of four_of_a_kind'


def check_full_house():
    player1 = [('spades', 'A'),  ('hearts', 'A'),  ('diamonds', 'A'),  ('spades', 'J'), ('hearts', 'J')]
    assert part1.full_house(player1)['status'] == 1, 'Please Check you validity of full_house'
    assert part1.full_house(player1)['Marks'] == 64, 'Please Check you evaluation of full_house'

def check_flush():
    player1 = [('spades', 'A'),  ('spades', 'K'),  ('spades', '8'),  ('spades', '3'), ('spades', '5')]
    assert part1.flush(player1)['status'] == 1, 'Please Check you validity of flush'
    assert part1.flush(player1)['Marks'] == 43, 'Please Check you evaluation of flush'

def check_straight():
    player1 = [('spades', '8'),  ('diamonds', '7'),  ('hearts', '6'),  ('clubs', '5'), ('spades', '4')]
    assert part1.straight(player1)['status'] == 1, 'Please Check you validity of straight'
    assert part1.straight(player1)['Marks'] == 30, 'Please Check you evaluation of straight'

def check_three_of_a_kind():
    player1 = [('spades', '7'),  ('spades', '2'),  ('hearts', 'Q'),  ('clubs', 'Q'), ('spades', 'Q')]
    assert part1.three_of_a_kind(player1)['status'] == 1, 'Please Check you validity of three_of_a_kind'
    assert part1.three_of_a_kind(player1)['Marks'] == 45, 'Please Check you evaluation of three_of_a_kind'

def check_two_pair():
    player1 = [('spades', 'A'),  ('hearts', 'A'),  ('spades', '4'),  ('clubs', '4'), ('spades', '3')]
    assert part1.two_pair(player1)['status'] == 1, 'Please Check you validity of two_pair'
    assert part1.two_pair(player1)['Marks'] == 36, 'Please Check you evaluation of two_pair'


def check_one_pair():
    player1 = [('spades', 'A'),  ('hearts', 'A'),  ('spades', '2'),  ('clubs', '4'), ('spades', '3')]
    assert part1.one_pair(player1)['status'] == 1, 'Please Check you validity of one_pair'
    assert part1.one_pair(player1)['Marks'] == 28, 'Please Check you evaluation of one_pair'

def check_high_card():
    player1 = [('spades', 'A'),  ('hearts', 'K'),  ('diamonds', '2'),  ('spades', '4'), ('clubs', '3')]
    assert part1.high_card(player1)['status'] == 1, 'Please Check you validity of high_card'
    assert part1.high_card(player1)['Marks'] == 36, 'Please Check you evaluation of high_card'

def input_validation_poker():
    player1 = [('spades', 'A'),   ('spades', '4'), ('clubs', '3')]
    player2 = [('spades', 'A'),  ('hearts', 'K'),  ('diamonds', '2'),  ('spades', '4'), ('clubs', '3')]
    assert part1.poker_game(player1,player2) == "Please check the inputs", 'Please check the input validity'

def input_tuple_validation_poker():
    player1 = [('spades', 'A'),   ('spades'), ('clubs', '3')]
    player2 = [('spades', 'A'),  ('hearts'),  ('diamonds', '2'),  ('spades'), ('clubs', '3')]
    assert part1.poker_game(player1,player2) == "Please check the inputs", 'Please check the input validity'








