from libr import *

players = gamers(number)

def games(players):
    terma = "ΤΙΠΟΤΑ"
    allagh_seiras = None  # δεν υπάρχει η αλλαγή σειράς ως open_card
    terma = None
    boyka = -1
    baby_yoda = 1
    t = 1
    poko = []
    popa=False
    for i in range(len(players)):# bazei se kaue 8esh tous ba8mous twn paiktwn(gia arxh einai oloi 0)
        poko += [0]
    flag = False #mas deixnei an kapoios paixths exei panw apo 50 pontous
    telos = 2 #mas deixnei posoi paixtes exoun tous ligoterous pontous(gia arxh to arxio8etoume me 2 gia na paixtei to prwto game)
    while flag == False or telos > 1: #an kanenas den exei panw apo 50 pontous kai an exoun perissotera apo 1 atoma thn mikroterh ba8mologia to game janapaizetai
        kwstas=create_deck()
        cards = arxh(1,kwstas)
        open_card = arxh(2,kwstas)
        trapoula = arxh(3,kwstas)
        katw_trapoula = []
        katw_trapoula += [open_card]
        while terma == None:  # δεν εχει μεινει κανενας χωρις κανενα φυλλο
            k = 0  # χρησιμοποειται για να μας δειχνει ποιος παιχτης παιζει π.χ.player[k]
            for i in cards:
                if t == 0:
                    t = 1
                    k += 1
                    continue;
                if k != boyka and baby_yoda == 0:
                    k += 1
                    continue;
                elif k == boyka and baby_yoda == 0:
                    baby_yoda = 1

                print("Τα φύλλα του " + players[k] + " είναι τα " + str(i))
                print("Το ανοιχτό φύλλο είναι το " + str(open_card))
                if allagh_seiras != None:
                    print("πρεπει να παιξεις με το σχεδιο " + str(allagh_seiras) + "(" + sxhma + ")")
                num = int(input("Ο παίχτης ονόματι " + players[k] + " παίζει:")) #o paikths paizei to fyllo pou 8e
                wait = False
                if num > len(i) or num < 1:
                    if num==0:      #an dwsoume to 0 o paixths paei PASO
                        if trapoula == []:
                            trapoula = trap_cards(trapoula, katw_trapoula)
                            katw_trapoula = []
                            katw_trapoula+=[open_card]
                            if trapoula==[]:
                                print("ΔΕΝ ΥΠΑΡΧΟΥΝ ΑΛΛΕΣ ΚΑΡΤΕΣ ΔΙΑΘΕΣΙΜΕΣ ΣΤΗΝ ΚΛΕΙΣΤΗ/ΤΡΑΠΟΥΛΑ")
                                popa=True
                            else:
                                popa=False
                        k+=1
                        if popa==False:#to popa einai mia metablhth pou mas deixnei an h trapoula einai kenh 
                            i += [(trapoula[0])]#an h trapoula einai kenh propspernaei th diadikasia,an h trapoula exei fylla
                            boomer = trapoula[0]#ekteleitai h diadikasia(to false mas deixnei oti exei fylla h trapoula enw to True to anti8eto)
                            trapoula = [x for x in trapoula if x != boomer]
                            
                        continue;
                    while wait == False:
                        num = int(input("Ξαναδώσε τη θέση χαρτιού:"))
                        if num >= 1 and num <= len(i):
                            wait = True
                
                selection = i[num - 1]
                if allagh_seiras == None:  # δεν υπαρχει το φυλλο της αλλαγης σειρας(sxediou)
                    if selection[0] == open_card[0] or selection[1] == open_card[1] or selection[0] == "A":
                        cards[k] = [e for e in cards[k] if e != selection]
                        open_card = selection
                        katw_trapoula += [open_card]
                        if selection[0] == "A":
                            sxhma = input("Δώσε τη νέα σειρά:")
                            if sxhma == "koupa" or sxhma == "kupa":
                                allagh_seiras = "♥"
                            elif sxhma == "spathi" or sxhma=="spa8i":
                                allagh_seiras = "♣"
                            elif sxhma == "karo":
                                allagh_seiras = "♦"
                            elif sxhma == "bastouni" or sxhma == "bastuni" or sxhma == "mpastuni" or sxhma == "mpastouni":
                                allagh_seiras = "♠"
                        if selection[0] == "7":
                            if len(trapoula)>=2:
                                for x in range(2):
                                    if k != len(cards) - 1:
                                        cards[k + 1] += [(trapoula[0])]
                                        boomer = trapoula[0]
                                        trapoula = [x for x in trapoula if x != boomer]

                                    else:
                                        cards[0] += [(trapoula[0])]
                                        boomer = trapoula[0]
                                        trapoula = [x for x in trapoula if x != boomer]
                                    if trapoula == []:
                                        trapoula = trap_cards(trapoula, katw_trapoula)
                                        katw_trapoula =[]
                                        katw_trapoula+=[open_card]
                                        if trapoula==[]:
                                            print("ΔΕΝ ΥΠΑΡΧΟΥΝ ΑΛΛΕΣ ΚΑΡΤΕΣ ΔΙΑΘΕΣΙΜΕΣ ΣΤΗΝ ΚΛΕΙΣΤΗ ΤΡΑΠΟΥΛΑ")
                                            popa=True
                                        else:
                                            popa=False
                        if selection[0] == "8" and len(cards[k]) == 0:
                            i += [(trapoula[0])]
                            boomer = trapoula[0]
                            trapoula = [x for x in trapoula if x != boomer]
                        elif selection[0] == "8" and len(cards[k]) != 0:
                            boyka = k
                            baby_yoda = 0
                        if selection[0] == "9":
                            t = 0
                    else:
                        if popa==False:#to popa einai mia metablhth pou mas deixnei an h trapoula einai kenh 
                            i += [(trapoula[0])]#an h trapoula einai kenh propspernaei th diadikasia,an h trapoula exei fylla
                            boomer = trapoula[0]#ekteleitai h diadikasia(to false mas deixnei oti exei fylla h trapoula enw to True to anti8eto)
                            trapoula = [x for x in trapoula if x != boomer]
                            # prepei na afairoume kai to sygkekrimeno fyllo
                    if trapoula == []:
                        trapoula = trap_cards(trapoula, katw_trapoula)
                        katw_trapoula = []
                        katw_trapoula+=[open_card]
                        if trapoula==[]:
                            print("ΔΕΝ ΥΠΑΡΧΟΥΝ ΑΛΛΕΣ ΚΑΡΤΕΣ ΔΙΑΘΕΣΙΜΕΣ ΣΤΗΝ ΚΛΕΙΣΤΗ/ΤΡΑΠΟΥΛΑ")
                            popa=True
                        else:
                            popa=False
                    if cards[k] == []:
                        print(True)
                        terma = "YES"  # ΚΑΠΟΙΟΣ ΒΓΗΚΕ
                        maybe_winner = k
                        break;

                else:  # το φυλλο αλλαγης σειρας παιχτηκε(Assos)
                    if selection[1] == allagh_seiras:
                        allagh_seiras = None
                        cards[k] = [e for e in i if e != selection]
                        open_card = selection
                        if selection[0] == "A":
                            sxhma = input("Δώσε τη νέα σειρά:")
                            if sxhma == "koupa" or sxhma == "kupa":
                                allagh_seiras = "♥"
                            elif sxhma == "spathi" or sxhma == "spa8i":
                                allagh_seiras = "♣"
                            elif sxhma == "karo":
                                allagh_seiras = "♦"
                            elif sxhma == "bastouni" or sxhma == "bastuni" or sxhma == "mpastuni" or sxhma == "mpastouni":
                                allagh_seiras = "♠"

                        if selection[0] == "7":
                            if len(trapoula)>=2:
                                for x in range(2):
                                    if k != len(cards) - 1:
                                        cards[k + 1] += trapoula[0]
                                        boomer = trapoula[0]
                                        trapoula = [x for x in trapoula if x != boomer]
                                    else:
                                        cards[0] += trapoula[0]
                                        boomer = trapoula[0]
                                        trapoula = [x for x in trapoula if x != boomer]
                                    if trapoula == []:
                                        trapoula = trap_cards(trapoula, katw_trapoula)
                                        katw_trapoula = []
                                        katw_trapoula+=[open_card]
                                        if trapoula==[]:
                                            print("ΔΕΝ ΥΠΑΡΧΟΥΝ ΑΛΛΕΣ ΚΑΡΤΕΣ ΔΙΑΘΕΣΙΜΕΣ ΣΤΗΝ ΚΛΕΙΣΤΗ ΤΡΑΠΟΥΛΑ")
                                            popa=True
                                        else:
                                            popa=False
                        if selection[0] == "8" and len(cards[k]) == 0:
                            i += [(trapoula[0])]
                            boomer = trapoula[0]
                            trapoula = [x for x in trapoula if x != boomer]
                        elif selection[0] == "8" and len(cards[k]) != 0:
                            boyka = k
                            baby_yoda = 0

                        if selection[0] == "9":
                            t = 0
                    else:
                        if popa==False:
                            i += [(trapoula[0])]
                            boomer = trapoula[0]
                            trapoula = [x for x in trapoula if x != boomer]

                    if trapoula == []:
                        trapoula = trap_cards(trapoula, katw_trapoula)
                        katw_trapoula = []
                        katw_trapoula+=[open_card]
                        if trapoula==[]:
                            print("ΔΕΝ ΥΠΑΡΧΟΥΝ ΑΛΛΕΣ ΚΑΡΤΕΣ ΔΙΑΘΕΣΙΜΕΣ ΣΤΗΝ ΚΛΕΙΣΤΗ ΤΡΑΠΟΥΛΑ")
                            popa=True
                        else:
                            popa=False
                if cards[k] == []:
                    print(True)
                    terma = "YES"  # ΚΑΠΟΙΟΣ ΒΓΗΚΕ
                    allagh_seiras=None
                    break;
                k += 1
        terma = None
        r = 0
        maybe_winner = r
        min = poko[r] #arxeio8etei tous ligoterous pontous ston prwto paixth
        for i in cards:
            for x in i:
                poko[r]+= x[2]
            if poko[r] > 50:
                flag = True 
            if poko[r] < min:
                min = poko[r]
                maybe_winner = r
            r += 1

        telos = 0 #deixnei posoi paixtes exoun tous ligoterous pontous
        r = 0
        for i in poko:
            print("Ο παίχτης :" + players[r] + " έχει " + str(i) + " πόντους")
            if i == min:
                maybe_winner = r
                telos += 1
            r += 1
        #print(flag)
        if telos > 1: #an einai panw apo enan oi paixtes pou exoun tous ligoterous pontous janapaizetai game
            print(str(telos) + "έχουν τους ίδιους πόντους")
        else:   
            print("Ένα άτομο έχει τους λιγότερους πόντους")
    return "O παίχτης " + players[maybe_winner] + " νίκησε"

print(games(players))
print("Μια ευγενική χορηγία του Κωνσταντίνου Μάρκο(Α.Μ.3190112) και του Γεώργιου Κοτσιφού(Α.Μ.3190093)")