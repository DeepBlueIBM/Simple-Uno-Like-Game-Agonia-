number = int(input("Δώσε αριθμό παικτών:"))
if number<1 or number>7:#elegxei an oi paiktes einai apo 1-7 an oxi ksanazhtaei ton ari8mo twin paikwn
    flag=False
    while flag==False:
        number = int(input("Ξαναδώσε αριθμό παικτών:"))
        if number>=1 and number<=7:
            flag=True
def gamers(number):  # """!!ΠΑΙΚΤΕΣ!!"""
    """taksinomei alfabhtika tous paixtes se pinaka kai ton epistrefei"""
    
    players = []
    for i in range(number):
        player = input("Δώσε όνομα παίκτη:")
        players += [player]
    players.sort()
    return players

def create_deck():  # """!!ΤΡΑΠΟΥΛΑ!!"""
    """ftiaxnei mia trapoula apo 52 fylla+to doctest elegxei an exoume 52 fylla
    
    >>> boby=create_deck()
    >>> len(boby)
    52
    """
    import random
    k = ["♥", "♣", "♦", "♠"]
    eid = ["A", "K", "J", "Q"]
    list = []
    lista = []
    for i in k:
        for j in range(2, 11):
            list += [(str(j), i, j)]
    for i in eid:
        for j in k:
            if i == "A":
                lista += [(i, j, 11)]
            else:
                lista += [(i, j, 10)]
    list += lista
    random.shuffle(list)
    return list
    
kwstas=create_deck()
    
def arxh(playboy,kwstas):  # """!!ΧΩΡΙΣΜΟΣ ΦΥΛΛΩΝ ΣΕ ΠΑΙΚΤΕΣ+ΑΝΟΙΧΤΟ ΦΥΛΛΟ!!"""
    """to doctest elegxei an ola ta xartia einai diaforetika metaksi tous anamesa sth trapoula,to anoixto fyllo kai ta fylla pou moirazontai stous paixtes
    
    >>> cards=arxh(1,kwstas)
    >>> open_card=arxh(2,kwstas)
    >>> trapoula = arxh(3,kwstas)
    >>> done=False
    >>> for i in cards:
    ...     for y in trapoula:
    ...         for x in i:
    ...             if x == y:
    ...                 done = 1
    ...                 print("kapoio xarti einai idio")
    ...             elif x == open_card:
    ...                 done = 1
    ...                 print("kapoio xarti einai idio")
    ...             elif x == open_card:
    ...                 done = 1
    ...                 print("kapoio xarti einai idio")
    ...
    >>> if done==False:
    ...     print("ola ta xartia einai diaforetika")
    ...
    ola ta xartia einai diaforetika
    """
    mike = []
    cards = []
    k = 0
    open_card=kwstas[51]
    kwstas=[x for x in kwstas if x!=open_card]
    for i in kwstas:
        if k == 7 * number:
            break;
        mike += [i]
        k += 1
        if k % 7 == 0:
            cards += [mike]
            mike = []
        kwstas = [x for x in kwstas if x != i]
    if playboy == 1:
        return cards
    if playboy == 2:
        return open_card
    if playboy == 3:
        return kwstas
        
        
def trap_cards(trap, katw):#to "trap" einai h kleisth trapoula to "katw" 
    import random          #gyrnaei pisw thn kleisth trapoula anakatemenh ap ta fylla ths anoixths trapoulas
    katw.pop(-1)
    trap = [x for x in katw[::-1]]
    random.shuffle(trap)
    return trap