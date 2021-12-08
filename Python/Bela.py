N, B = input().split()

normal = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'J': 2,
    'T': 10,
    '9': 0,
    '8': 0,
    '7': 0
}

dominant = {
  'A': 11,
  'K': 4,
  'Q': 3,
  'J': 20,
  'T': 10,
  '9': 14,
  '8': 0,
  '7': 0
}

count = 0

def solver(card, suit, dominant_suit):
    if suit == dominant_suit:
        return dominant[card]
    return normal[card]

for i in range(int(N)*4):
    x = input()
    count += solver(x[0],x[1],B)
##    print(x, count)
print(count)
