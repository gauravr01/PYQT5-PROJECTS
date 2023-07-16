
from PyQt5.QtWidgets import QMainWindow,QApplication,QComboBox,QLabel,QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import random

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        uic.loadUi("deck.ui",self)
        self.dealerLabel = self.findChild(QLabel,"Delearlabel")
        self.playerLabel = self.findChild(QLabel,"Playerlabel")
        self.dealerHeaderLabel = self.findChild(QLabel,"label")
        self.playerHeaderLabel = self.findChild(QLabel,"label_2")
         
        self.shuffleButton = self.findChild(QPushButton,"pushButton")
        self.dealButton = self.findChild(QPushButton,"pushButton_2")

        #shuffle cards
        self.shuffle()

        self.shuffleButton.clicked.connect(self.shuffle)
        self.dealButton.clicked.connect(self.dealCards)
            

        self.show()

    def shuffle(self):
        #define our deck
        suits = ["diamonds", "clubs" , "hearts","spades"]
        values = range(2,15)
        #11 jack, 12 queen, 13 king, 14 Ace

        #Create a deck
        global deck
        deck = []
        for suit in suits:
            for value in values:
                deck.append(f"{value}_of_{suit}")

        # print(deck)
        # print(len(deck))        
        #creat our players
        global dealer,player
        dealer = []
        player = []
        #Keep track of scores
        self.dealer_score = 0
        self.player_score = 0
        #Grab a random card for a dealer
        self.dealer_card = random.choice(deck)
        #remove the card from the deck
        deck.remove(self.dealer_card)
        #add the card to dealers list
        dealer.append(self.dealer_card)
        #Output card to screen
        pixmap = QPixmap(f'C:\\Users\\Kush-PC\\Downloads\\PNG-cardss\\PNG-cards\\{self.dealer_card}.png')
        self.dealerLabel.setPixmap(pixmap)
        
        #Grab a random card for a player
        self.player_card = random.choice(deck)
        #remove the card from the deck
        deck.remove(self.player_card)
        #add the card to dealers list
        player.append(self.player_card)
        #Output card to screen
        pixmap = QPixmap(f'C:\\Users\\Kush-PC\\Downloads\\PNG-cardss\\PNG-cards\\{self.player_card}.png')
        self.playerLabel.setPixmap(pixmap)

        self.setWindowTitle(f"{len(deck)} CARD left in deck...")

        #determine score
        self.score()
    def dealCards(self):
        try:
            
            #Grab a random card for a dealer
            self.dealer_card = random.choice(deck)
            #remove the card from the deck
            deck.remove(self.dealer_card)
            #add the card to dealers list
            dealer.append(self.dealer_card)
            #Output card to screen
            pixmap = QPixmap(f'C:\\Users\\Kush-PC\\Downloads\\PNG-cardss\\PNG-cards\\{self.dealer_card}.png')
            self.dealerLabel.setPixmap(pixmap)
            
            #Grab a random card for a player
            self.player_card = random.choice(deck)
            #remove the card from the deck
            deck.remove(self.player_card)
            #add the card to dealers list
            player.append(self.player_card)
            #Output card to screen
            pixmap = QPixmap(f'C:\\Users\\Kush-PC\\Downloads\\PNG-cardss\\PNG-cards\\{self.player_card}.png')
            self.playerLabel.setPixmap(pixmap)
            self.setWindowTitle(f"{len(deck)} CARD left in deck...")
            
            #determine score
            self.score()
        except:
            #Tie
            if self.dealer_score == self.player_score:

                self.setWindowTitle(f"Game Over || TIE || {self.dealer_score} to {self.player_score}")
            #Dealer wins
            elif self.dealer_score > self.player_score:
                self.setWindowTitle(f"Game Over || DEALER WINS || {self.dealer_score} to {self.player_score}")

            #Player wins
            else:
                self.setWindowTitle(f"Game Over || PLAYER WINS || {self.player_score} to {self.dealer_score}")
          

    def score(self):
        #Strip out the card number
        self.dealer_card = int(self.dealer_card.split("_",1)[0])
        self.player_card = int(self.player_card.split("_",1)[0])

        #compare the card num
        #Tie
        if self.dealer_card == self.player_card:
            self.dealerHeaderLabel.setText("Tie")
            self.playerHeaderLabel.setText("Tie")
            self.setWindowTitle(f"{len(deck)} CARD left in deck...  ||  Dealer:{self.dealer_score} Player:{self.player_score}")
        #Dealer Wins
        elif self.dealer_card > self.player_card:
            self.dealerHeaderLabel.setText("Dealer Wins")
            self.playerHeaderLabel.setText("Player Loses")
            #Update score
            self.dealer_score += 1
            self.setWindowTitle(f"{len(deck)} CARD left in deck...  ||  Dealer:{self.dealer_score} Player:{self.player_score}")
        
        else:
            self.dealerHeaderLabel.setText("Dealer Loses")
            self.playerHeaderLabel.setText("Player Wins")
            #Update score
            self.player_score += 1
            self.setWindowTitle(f"{len(deck)} CARD left in deck...  ||  Dealer:{self.dealer_score} Player:{self.player_score}")
        

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()