import random
class player:
    def __init__(self, name,owncards,suspect_cards=None) -> None:

        self.n=name
        self.cards=owncards
        self.suspect=suspect_cards

    def read(self,cards_pub=None,free_cards = None,reveal=None):
        if self.suspect is None:
            self.suspect = {key:value.copy()for key,value in cards_pub.items() }

            for key,value  in self.suspect.items():   
                try:
                    for i in self.cards:
                        if i in value:
                            value.remove(i)
                            print("fuer re movido", i ," en", key)
                            
                        else:
                            continue
                except:
                    continue
        if free_cards is not None:
            for key,value  in self.suspect.items():   
                try:
                    for i in free_cards:
                        if i in value:
                            value.remove(i)
                            print("fuer re movido", i ," en", key)
                            
                        else:
                            continue
                except:
                    continue
        if reveal is not None:
            print("hey")
            for key,value  in self.suspect.items():   
                try:
                    if reveal in value:
                        value.remove(reveal)
                        print("fuer re movido", reveal ," en", key)
                        
                    else:
                        
                        break

                except:
                    
                    continue

    def response(self,list_sp):
        for card in list_sp:
            if card in self.cards:
                print("se mostro esta carta ",card)
                break
        return card
    
    def sustec(self):
        guess=[]
        for key,cards in self.suspect.items():
            carta_elegida=random.choice(cards)
            guess.append(carta_elegida)
        return guess

    def make_gult(self):
        gulty=[]
        if len(self.suspect["Habitaciones"])== 1:
            gulty.append(self.suspect["Habitaciones"][0])
        if len(self.suspect["Armas"])== 1:
            gulty.append(self.suspect["Armas"][0])

        if len(self.suspect["Sospechosos"])== 1:
            gulty.append(self.suspect["Sospechosos"][0])
        print(gulty)
        return gulty