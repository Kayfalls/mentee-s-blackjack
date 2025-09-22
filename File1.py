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
# •create a class cards
# •create 50 card items and check if there isnt a module specifically for cards 
# •randomise a set of cards before dealing
