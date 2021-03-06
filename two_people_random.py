poker = ['2S','2C','2D','2H',
        '3S','3C','3D','3H',
        '4S','4C','4D','4H',
        '5S','5C','5D','5H',
        '6S','6C','6D','6H',
        '7S','7C','7D','7H',
        '8S','8C','8D','8H',
        '9S','9C','9D','9H',
        'OS','OC','OD','OH',
        'JS','JC','JD','JH',
        'QS','QC','QD','QH',
        'KS','KC','KD','KH',
        'AS','AC','AD','AH']
import random
hand1 = random.sample(poker,5)
hand2 = random.sample(poker,5)
hand11 = ' '.join(hand1)
hand22 = ' '.join(hand2)
def card_ranks(cards):
   ranks = ['0123456789OJKLA'.index(r) for r,s in cards.split()]
   ranks.sort(reverse=True)
   return ranks
def judge_straight(cards):
   ranks = card_ranks(cards)
   return (max(ranks)-min(ranks))==4 and len(set(ranks))==5
def judge_suit(cards):
   suit = [s for r,s in cards.split()]
   return len(set(suit))==1
def judge_same(n,ranks):
   for r in ranks:
      if ranks.count(r)==n:
         return r
def doubletwo(ranks):
   first = judge_same(2,ranks)
   second = judge_same(2,list(reversed(ranks)))
   if first and second != first:
      return (first,second)
def hand_rank(hand):
   ranks = card_ranks(hand)
   if judge_straight(ranks) and judge_suit(ranks):
      return (9,max(ranks))
   elif judge_same(4,ranks):
      return (8,judge_same(4,ranks),judge_same(1,ranks))
   elif judge_same(3,ranks) and judge_same(2,ranks):
      return (7,judge_same(3,ranks),judge_same(2,ranks))
   elif judge_suit(hand):
      return (6,ranks)
   elif judge_straight(hand):
      return (5,max(ranks))
   elif judge_same(3,ranks):
      return (4,judge_same(3,ranks),ranks)
   elif doubletwo(ranks):
      return (3,doubletwo(ranks),ranks)
   elif judge_same(2,ranks):
      return (2,judge_same(2,ranks),ranks)
   else:
      return (1,ranks)
def compare(hands):
   return max(hands,key=hand_rank)
print(compare([hand11,hand22]))
