T = int(input())
for tc in range(1, T+1):
    N = int(input())
    deck = input().split()
    
    mid = N // 2
    bf_deck = deck[:mid]
    af_deck = deck[mid:]
    
    new_deck = []
    for i in range(mid):
        new_deck.append(bf_deck[i])
        new_deck.append(af_deck[i])
    
    print(' '.join(new_deck))