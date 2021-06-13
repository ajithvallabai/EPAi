### EPAI - Session 6 

**The Poker GAME**

**Functions convered in Testing**

- create cards 
- royal flush
- straight flush
- four of a kind
- full house
- flush
- straight
- three of a kind
- two pair
- one pair
- high card
- game

- Readme and captilization testing functions are written

### Creating Cards

- Create a deck of 52 cards from values(13) and suits(4)

**check_task1()**

    decksingleline = lambda vals,suits: list(map(lambda pair: pair[0] , zip([(eVal,eSuit) for eVal in suits for eSuit in vals])))

decksingleine - we are are creating 52 cards with for loop and zipping it . Than we are using map and lambda 

We are passing vals and suits and checking if we are getting a deck of 52 cards

**check_task2()**

    n = len(vals)
    m = len(suits)
    Deck = []
    for x in range(m):
      for y in range(n):
        Deck.append((suits[x],vals[y]))

With for loop we are iterating over vals and suits and we are creating pairs

### 10 poker Hands

**check_poker_game()**

poker_game() - we are getting input cards from player and validating the length number of cards. We are taking all the poker hands in a list and checking which category players cards belong. After checking which category a it belongs we are checking the priority and value of cards to decide who is going to win.

    player1 = [('spades', 'A'),  ('spades', 'K'),  ('spades', 'Q'),  ('spades', 'J'), ('spades', '10'),]
    player2 = [('spades', 'A'),  ('hearts', 'K'),  ('diamonds', '2'),  ('spades', '4'), ('clubs', '3')]

Test- Two input set of cards are passed which are of player 1 and player 2 and we are checking who is going to win. Player1 has got Royal flush and player two has got high card so player 1 won.

**check_royal_flush()**

Royal Flush - all five cards beling to same category with A,K,Q,J it will be royal flush.

We are passing a set of cards that belongs to royal flush and checking it its a royal flush and its marks.

**check_straight_flush()**

Straight flush - if we get same suite of cards in a straight order(10,9,8,7,6) or (2,3,4,5,6) we can call it as straight flush

    player1 = [('hearts', '10'),  ('hearts', '9'),  ('hearts', '8'),  ('hearts', '7'), ('hearts', '6')]
    

We are checking if all the cards would belong to same suite
    and it will contain consecutive numbers

### check_four_of_a_kind():

    player1 = [('clubs', 'A'),  ('clubs', '7'),  ('hearts', '7'),  ('diamonds', '7'), ('spades', '7')]
        

We are checking if four of the cards  would have same value    

### check_full_house():

    player1 = [('spades', 'A'),  ('hearts', 'A'),  ('diamonds', 'A'),  ('spades', 'J'), ('hearts', 'J')]
        

We are checking if it Contains 3 of a kind and 2 of another kind   

### check_flush():

    player1 = [('spades', 'A'),  ('spades', 'K'),  ('spades', '8'),  ('spades', '3'), ('spades', '5')]
        
We are checking if All the numbers would be of same kind   

### check_straight():

    player1 = [('spades', '8'),  ('diamonds', '7'),  ('hearts', '6'),  ('clubs', '5'), ('spades', '4')]
        
We are checking it contains consecutive cards in different Suite    

### check_three_of_a_kind():

    player1 = [('spades', '7'),  ('spades', '2'),  ('hearts', 'Q'),  ('clubs', 'Q'), ('spades', 'Q')]

We are checking if Three values would be of same kind   

### check_two_pair():

    player1 = [('spades', 'A'),  ('hearts', 'A'),  ('spades', '4'),  ('clubs', '4'), ('spades', '3')]
    

We are checking if it Contains two pairs of same value   

### check_one_pair():

    player1 = [('spades', 'A'),  ('hearts', 'A'),  ('spades', '2'),  ('clubs', '4'), ('spades', '3')]
  

We are checking if it Contains one pair of a values 

### check_high_card():

    player1 = [('spades', 'A'),  ('hearts', 'K'),  ('diamonds', '2'),  ('spades', '4'), ('clubs', '3')]
    
We are checking if All values are different 

### input_validation_poker():

    player1 = [('spades', 'A'),   ('spades', '4'), ('clubs', '3')]
    player2 = [('spades', 'A'),  ('hearts', 'K'),  ('diamonds', '2'),  ('spades', '4'), ('clubs', '3')]
    

We are checking if both player1 and player 2 passes 5 cards. There should be 5 cards for a player

### input_tuple_validation_poker():

    player1 = [('spades', 'A'),   ('spades'), ('clubs', '3')]
    player2 = [('spades', 'A'),  ('hearts'),  ('diamonds', '2'),  ('spades'), ('clubs', '3')]
    
We are checking if the tuple has correct length. There should be two tuples in each of 5 cards.
























