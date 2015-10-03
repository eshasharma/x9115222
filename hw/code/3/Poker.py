"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *
from operator import or_
"""from prettytable import *"""


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
    
                  
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        #print self.suits
        for val in self.suits.values():
            if val >= 5:
                return "True"
        return "False"
    
            
    def has_pair(self):
        count=0
        self.rank_hist()
        #print self.ranks
        for key in self.ranks.keys():
            if self.ranks[key] == 2:
                count=count+1
            if count==1:
                return "True"
        return "False"
  
    def has_twopair(self):
        count=0
        self.rank_hist()
        for key in self.ranks.keys():
            if self.ranks[key] == 2:
                count=count+1
            if count==2:
                return "True"
        return "False"
 
    def has_threeofakind(self):
        self.rank_hist()
        for key in self.ranks.keys():
            if self.ranks[key]== 3:
                for key1 in self.ranks.keys():
                    if self.ranks[key1]==2:
                        return "False"
                return "True"   
        return "False"

    def has_fourofakind(self):
        self.rank_hist()
        for key in self.ranks.keys():
            if self.ranks[key]== 4:
                for key1 in self.ranks.keys():
                    if self.ranks[key1]==2 or self.ranks[key1]==3:
                        return "False"
                return "True"
        return "False"
    
    def has_full_House(self):
        self.rank_hist()
        flag1=0
        flag2=0
        for key in self.ranks.keys():
            if (self.ranks[key]==3):
                flag1=1 
            if (self.ranks[key]==2):
                flag2=1
        if ((flag1==1) and (flag2==1)):   
            return "True"
        return "False"
    
    def has_straight(self):
        count=0
        ranks=[]
        for card in self.cards:
           ranks.append(card.rank)
        ranks.sort() 
        if ranks[0]==1 and ranks[len(ranks)-1]==13:
            ranks[0]=14
            ranks.sort()
        
        for i in range(len(ranks)-1):
            if ranks[i+1]==ranks[i]+1:
                count=count+1
            if (count>=4):  
               return "True"
        return "False"
            
    def has_straight_flush(self):
        flag1=self.has_flush()
        flag2=self.has_straight()
        if (flag1=="True" and flag2=="True"):
            return "True"
        return "False"   

    def classify(self):
        results=[]
        results.append(hand.has_straight_flush()+" " +"straight_flush")
        results.append(hand.has_straight()+" " +"straight")
        results.append(hand.has_full_House()+" " +"full_house")
        results.append(hand.has_flush()+" " +"flush")
        results.append(hand.has_fourofakind()+" " +"four")
        results.append(hand.has_threeofakind()+" " +"three")
        results.append(hand.has_twopair()+" " +"twopair")
        results.append(hand.has_pair()+" " +"pair")
        #print results
        for j in results:
            #print j
            a=j[0:4]
            if (a=='True'):
                #print j
                return j[5:]
        return None   
    def count_classify(self,i,n):
        #deck = Deck()
       # deck.shuffle()
        classify_result=[]
        #print i,n
        for j in range(i):
           deck = Deck()
           deck.shuffle()
           deck.move_cards(self, n)
           self.sort()
           a= self.classify()
          # print a
          # print
           
           #print a
           classify_result.append(a)
           self.remove_all_card()
       # print classify_result
        classify_hist=dict() 
        for a in classify_result:
            if a not in classify_hist:
               classify_hist[a]=1
            else:
               classify_hist[a]+=1  
        #print classify_hist
        for key in classify_hist.keys():
            classify_hist[key]= (float(classify_hist[key])/float(i))*100.0
            
        #print classify_hist
       # print total
        
        for key in classify_hist.keys():
            if(key !=None):
                print "Probabality of " + key +" happening is " + repr(classify_hist[key]) + "% when a hand of " +repr(n) +" cards is dealt "+ repr(i)+" times"
            
       
        return classify_result
 

if __name__ == '__main__':
    # make a deck
   # """deck = Deck()
   # deck.shuffle()

    # deal the cards and classify the hands
    #for i in range(17,18):
       
      #deck.move_cards(hand, i)
     # hand.sort()
     # print hand"""
      """ hand = PokerHand()"""
       #print  hand.classify()
       #print ' '
"""deck = Deck()
deck.shuffle()

for i in range(1):
           hand = PokerHand()
           card=Card(1,10)
           hand.add_card(card)
           card=Card(1,11)
           hand.add_card(card)
           card=Card(1,12)
           hand.add_card(card)
           card=Card(1,13)
           hand.add_card(card)
           card=Card(1,1)
           hand.add_card(card)
           #hand.sort()
           print hand
           print hand.has_straight_flush()
           print ''
           deck.move_cards(hand, 7)
           hand.sort()
           print hand
           print hand.has_threeofakind()
           print ''   
           """       
hand=PokerHand()
hand.count_classify(100,7)
      