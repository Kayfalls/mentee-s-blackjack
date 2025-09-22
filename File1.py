# imports
import copy
import random
import pygame

#pygame initializing
pygame.init()

#game variable
cards = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 4
width = 600
height = 900
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Pygame Blackjack!')
fps = 60
timer = pygame.time.clock()
font = pygame.font.Font('freesansbold.ttf', 36)
active = False

#win,loss,draw/push
records = [0, 0, 0]
player_score = 0
dealer_score = 0
initial_deal = False
my_hand = []
dealer_hand = []
outcome = 0
reveal_dealer = False
hand_active = False
outcome = 0
add_score = False
results = ['', 'PLAYER BUSTED :(', 'Player WINS! :)', 'DEALER WINS :(', 'TIE GAME...']

#deal cards by selecting randomly from dek,and make funtion for one card at a time
def deal_cards(current_hand, current_deck):
  card = random.randint(0, len(current_deck))
  current_hand.append(current_deck[card - 1])
  current_deck.pop(card - 1)
  return current_hand, current_deck

#draw scores for player and dealer on screen
def draw_scores(player, dealer):
  screen.blit(font.render(f'score [{player}]', True, 'white'), (350, 400))
  if reveal_dealer:
  screen.blit(font.render(f'score[{dealer}]', True, 'white'), (350, 100))

#draw cards visually onto screen
def draw_cards (player, dealer,reveal):
  for i in range(len(player)):
    pygame.draw.rect(screen, "white", [70 + (70 * i), 460 + (5 * i), 120, 220]. 0,5)
    screen.blit(font.render(player[i], True, 'black'), (75 + 70 * i, 465 + 5 * i))
    screen.blit(font.render(player[i], True, 'black'), (75 + 70 * i, 465 + 5 * i))
    pygame.draw.rect(screen, 'red', [70 + (70 * i), 460 + (5 * i), 120, 220], 5, 5)
    
#if player hasn't finished turn, dealer will hide one card
for i in range(len(dealer)):
  pygame.draw.rect(screen, 'white', [70 + (70 * i), 160 + (5 * i), 120, 220], 0, 5)
  if i != 0 or reveal:
    screen.blit(font.render(dealer[i], True, 'black'), (75 + 70 * i, 165 + 5 * i))
    screen.blit(font.render(dealer[i], True, 'black'), (75 + 70 * i , 335 + 5 * i))
  else:
    screen.blit(font.render('???', True, 'black'), (75 + 70 * i, 165 + 5 * i))
    screen.blit(font.render('???', True, 'black'), (75 + 70 * i , 335 + 5 * i))
  pygame.draw.rect(screen, 'blue', [70 + (70 * i), 160 + (5 * i), 120, 220], 5, 5)

#pass in player or dealer hand and get best score possible
def calculate_score(hand):
  #calculate hand sacore fresh every time, check how many aces we have
  hand_score = 0
  aces_count = hand.count('A')
  for i in range(len(hand)):
    #for 2,3,4,5,6,7,8,9 - just add the number to total
    for j in range(8):
      if hand[i] == cards[j]:
        hand_score += int(hand[i])
      #for 10 and face cards, add 10
      if hand[i] in ['10', 'J', 'Q', 'K']:
        hand_score += 10
      #for aces start by adding 11, we'll check if we need to reduce afterwards
      elif hand[i] == 'A' :
        hand_score += 11
        
    #determine how many aces need to be 1 instead og 11 to get under 21 if possible
  if hand_score > 21 and aces_count > 0 :
    for i in range(aces_count):
      if hand_score > 21:
        hand_score -= 10

return hand_score

#draw game conditions and buttons
def draw_game(act, record, result):
  button_list = []
  #initially on startup (not active) only option is to deal new hand
  if not act:
    deal = pygame.draw.rect
# •create a class cards
# •create 50 card items and check if there isnt a module specifically for cards 
# •randomise a set of cards before dealing
