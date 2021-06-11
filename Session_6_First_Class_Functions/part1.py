## Task 1
decksingleline = lambda vals,suits: zip(map(lambda pair: pair , [(eVal,eSuit) for eVal in suits for eSuit in vals] ))
## Task 2
def create_deck(vals : 'list' , suits : 'list' ) -> 'list of tuples':
    ''' 
    Creating a deck of 52 cards 
    vals: list of values
    suits: list of suit names
    return: list of 52 tuples 
    '''
    n = len(vals)
    m = len(suits)
    Deck = []
    for x in range(m):
      for y in range(n):
        Deck.append((suits[x],vals[y]))
    return Deck
## Task 3
## Imports
from collections import Counter 
## static stores
markKey = {'A':14,'K':13,'Q':12,'J':11, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
markKeyTwo = {'A':1,'K':13,'Q':12,'J':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
## Utility functions
def split_list(n :'int') -> 'returns list indexs':
    """
    Will return the list index
    """
    return [(x+1) for x,y in zip(n, n[1:]) if y-x != 1]

def get_sub_list(my_list :'list'):
    """
    Will split the list base on the index
    my_list: sorted list of values
    return: list of list containg consecutive numbers
    """
    my_index = split_list(my_list)
    output = list()
    prev = 0
    for index in my_index:
        new_list = [ x for x in my_list[prev:] if x < index]
        output.append(new_list)
        prev += len(new_list)
    output.append([ x for x in my_list[prev:]])
    return output

def evaluate_cards(valList: 'list') -> 'Score of cards':
    '''
    valList: input list of  string values
    return: summation of values
    '''
    marks = 0
    for each in valList:
      if each.isdigit():
        marks+=int(each)
      else:
        marks+= markKey[each]
    return marks

def evaluate_cards_int(valList: 'list') -> 'Score of cards':
    '''
    valList: input list of int values
    return: summation of values
    '''
    marks = 0
    for each in valList:    
        marks+=int(each)    
    return marks


# Poker Hands - Total 10

def royal_flush(cards: 'list') -> 'result':
    '''
    In Royal flush all the cards would belong to same suite
    and it will contain [A,K,Q,J,10]
    cards: players cards
    return: status,Name,priority,marks
    '''
    suitCheck = []
    valsCheck = []
    for each in cards:
        suitCheck.append(each[0])
        valsCheck.append(each[1])
    if len(set(suitCheck)) == 1 and (valsCheck == ['A','K','Q','J','10']):
        return {"status":1,"Name":"RoyalFlush","Priority":1,"Marks":1}
    else:
        return {"status":0,"Name":"RoyalFlush","Priority":1,"Marks":0}

def straight_flush(cards: 'list') -> 'result':
    '''
    In straight flush all the cards would belong to same suite
    and it will contain consecutive numbers
    cards: players cards
    return: status,Name,priority,marks
    '''
    suitCheck = []
    valsCheck1 = []
    valsCheck2 = []
    for each in cards:
        suitCheck.append(each[0])        
        valsCheck1.append(markKey[each[1]])
        valsCheck2.append(markKeyTwo[each[1]])    
    valsCheck1.sort()
    valsCheck2.sort()
    consecutive_list1 = get_sub_list(valsCheck1)    
    if len(set(suitCheck)) == 1:
      for each in consecutive_list1:
        if len(each) == 5:
          mark = evaluate_cards_int(each)
          return {"status":1,"Name":"StraightFlush","Priority":2,"Marks":mark}  
      consecutive_list2 = get_sub_list(valsCheck2)      
      for each in consecutive_list2:
        if len(each) == 5:
          mark = evaluate_cards_int(each)
          return {"status":1,"Name":"StraightFlush","Priority":2,"Marks":mark}      
    return {"status":0,"Name":"StraightFlush","Priority":2,"Mark":0}


def four_of_a_kind(cards: 'list') -> 'result':
    '''
    In four of a kind , four of the cards  would have same value    
    cards: players cards
    return: status,Name,priority,marks
    ''' 
    valsCheck = []
    for each in cards:        
        valsCheck.append(each[1])
    valcount =  dict(Counter(valsCheck))
    for key,items in valcount.items():
      if items == 4:
        return {"status":1,"Name":"FourOfAKind","Priority":3,"Marks":(markKey[key]*4)}
    return {"status":0,"Name":"FourOfAKind","Priority":3,"Marks":0}

def full_house(cards: 'list') -> 'result':
    '''
    Contains 3 of a kind and 2 of another kind    
    cards: players cards
    return: status,Name,priority,marks
    '''     
    valsCheck = []
    for each in cards:        
        valsCheck.append(each[1])
    valcount =  dict(Counter(valsCheck))
    if (3 in valcount.values()) and (2 in valcount.values()):   
        mark = evaluate_cards(valsCheck)
        return {"status":1,"Name":"FullHouse","Priority":4,"Marks":mark}
    return {"status":0,"Name":"FullHouse","Priority":4, "Marks":0}



def flush(cards: 'list') -> 'result':
    '''
    All the numbers would be of same kind   
    cards: players cards
    return: status,Name,priority,marks
    ''' 
    suitCheck = []
    valsCheck = []
    for each in cards:
        suitCheck.append(each[0])
        valsCheck.append(each[1])    
    if len(set(suitCheck)) == 1:
        mark = evaluate_cards(valsCheck)
        return {"status":1,"Name":"Flush","Priority":5,"Marks":mark}
    else:
        return {"status":0,"Name":"Flush","Priority":5,"Marks":0}

def straight(cards: 'list') -> 'result':
    '''
    Contains consecutive cards in different Suite    
    cards: players cards
    return: status,Name,priority,marks
    '''     
    valsCheck1 = []
    valsCheck2 = []
    for each in cards:        
        valsCheck1.append(markKey[each[1]])
        valsCheck2.append(markKeyTwo[each[1]])    
    valsCheck1.sort()
    valsCheck2.sort()
    consecutive_list1 = get_sub_list(valsCheck1)    
    for each in consecutive_list1:
      if len(each) == 5:
        mark = evaluate_cards_int(each)
        return {"status":1,"Name":"Straight","Priority":6,"Marks":mark}
    consecutive_list2 = get_sub_list(valsCheck2)    
    for each in consecutive_list2:
      if len(each) == 5:
        mark = evaluate_cards_int(each)
        return {"status":1,"Name":"Straight","Priority":6,"Marks":mark}      
    return {"status":0,"Name":"Straight","Priority":6,"Marks":0}


def three_of_a_kind(cards: 'list') -> 'result':    
    '''
    Three values would be of same kind   
    cards: players cards
    return: status,Name,priority,marks
    ''' 
    valsCheck = []
    for each in cards:        
        valsCheck.append(each[1])
    valcount =  dict(Counter(valsCheck))
    if (3 in valcount.values()) :   
        mark = evaluate_cards(valsCheck)
        return {"status":1,"Name":"ThreeOfAKind","Priority":7,"Marks":mark}
    return {"status":0,"Name":"ThreeOfAKind","Priority":7,"Marks":0}

def two_pair(cards: 'list') -> 'result':  
    '''
    Contains two pairs of same value   
    cards: players cards
    return: status,Name,priority,marks
    '''  
    valsCheck = []
    for each in cards:        
        valsCheck.append(each[1])
    valcount =  dict(Counter(valsCheck))
    countOfPairs = 0
    mark = 0
    for key,value in valcount.items():
      if value == 2:
        countOfPairs += 1
        mark += evaluate_cards(key)
    if countOfPairs == 2:
      return {"status":1,"Name":"Twopair","Priority":8,"Marks":mark*2}    
    return {"status":0,"Name":"Twopair","Priority":8,"Marks":0}

def one_pair(cards: 'list') -> 'result':   
    '''
    Contains one pair of a values    
    cards: players cards
    return: status,Name,priority,marks
    '''  
    valsCheck = []
    for each in cards:        
        valsCheck.append(each[1])
    valcount =  dict(Counter(valsCheck))
    countOfPairs = 0
    mark = 0
    for key,value in valcount.items():
      if value == 2:
        countOfPairs += 1
        mark += evaluate_cards(key)
    if countOfPairs == 1:
      return {"status":1,"Name":"onepair","Priority":9,"Marks":mark*2}    
    return {"status":0,"Name":"onepair","Priority":9,"Marks":0}

def high_card(cards: 'list') -> 'result':
    '''
    All values are different and suits are also different   
    cards: players cards
    return: status,Name,priority,marks
    '''     
    valsCheck = []
    suitsCheck = []
    mark = 0
    for each in cards:        
        valsCheck.append(each[1])
        mark += evaluate_cards(each[1])    
        suitsCheck.append(each[0])
    if len(set(valsCheck)) == 5 and len(set(suitsCheck)) >=2:           
        return {"status":1,"Name":"highcard","Priority":10,"Marks":mark}    
    return {"status":0,"Name":"highcard","Priority":10,"Marks":0}




# Main function
def poker_game(player1Cards: 'listoftuple', player2Cards: 'listoftuple') -> 'ResultofGame':
  '''
  Poker Game, Five cards per player, Two player mode  
  Gets two players cards and analyzes it       
  cards: players cards
  return: status,Name,priority,marks  
  '''
  for each in player1Cards:
    if len(each)!=2:
      return "Please check the inputs"
  for each in player2Cards:
    if len(each)!=2:
      return "Please check the inputs"

  if len(player1Cards) != 5 or len(player2Cards) != 5:
    return "Please check the inputs"
  player1Result = []
  player2Result = []
  pokerHands = [royal_flush,straight_flush, four_of_a_kind,full_house,
                     flush, straight, three_of_a_kind, two_pair, 
                        one_pair, high_card]
  for each in pokerHands:
    player1Result = each(player1Cards)
    if player1Result["status"] == 1:
      break 
  for each in pokerHands:
    player2Result = each(player2Cards)
    if player2Result["status"] == 1:
      break   
  if player1Result["Priority"] < player2Result["Priority"]:      
    return "Player1 WON"
  elif player1Result["Priority"] > player2Result["Priority"]:
    return "Player2 WON"
  else:
    if player1Result["Marks"] > player2Result["Marks"]:
        return "Player1 WON"
    elif player1Result["Marks"] < player2Result["Marks"]:
        return "Player2 WON"
    else:
        return "Match Draw"
