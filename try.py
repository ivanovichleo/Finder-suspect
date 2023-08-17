from jugadores import player
import random

Cartas={
        "Habitaciones":["Cocina","Comendor","Jacuzzi","Bar","Garaje","Baño","Habitación","gimnasio"],
        "Armas":["Taza","Katana","Cable","Bate"], 
        "Sospechosos":["Caballero Blanco","Sir Blake","Sra. Rose","Moradito","Amarillota","king gray"]
    }

def seleccionador():
    Crim=[]
    for key in Cartas.values():
        Crim.append(random.choice(key))
    return Crim
    # los sospechosos seria interesante que los nombres sean los jugadoresa

def dealer(n_players,Crimen):

    Cartas_restantes=[]
    count=0
    
    for value in Cartas.values():
        Cartas_restantes.extend(value)
        Cartas_restantes.remove(Crimen[count])
        count += 1
    Cartas_dis=Cartas_restantes.copy()
    Cartas_pub=[]
    distribution_cards={}


    if len(Cartas_restantes)%n_players == 0:
        
    #Reparte las cartas para cada jugador y las elimina las cartas de una lista temporal  para que 2 jugadores no tengan la misma carta
        for indice in range(n_players):
            
            distribution_cards[indice]=random.sample(Cartas_dis,k=len(Cartas_restantes)//n_players)

            for n in distribution_cards[indice]:
            
                Cartas_dis.remove(n)

        return distribution_cards, Cartas_pub

    else:
        
        Cartas_pub=random.sample(Cartas_dis,k=len(Cartas_restantes)%n_players)
        
        for cartas in Cartas_pub:
            Cartas_dis.remove(cartas)
        
        for indice in range(n_players):

            distribution_cards[indice]=random.sample(Cartas_dis,k=len(Cartas_restantes)//n_players)

            for n in distribution_cards[indice]:
            
                Cartas_dis.remove(n)
        return distribution_cards,Cartas_pub

def gestor(players):
    random.shuffle(Cartas["Sospechosos"])
    for turn_name in Cartas["Sospechosos"]:
        for player in players:
            if player.n == turn_name:
                # print(Cartas["Sospechosos"]," hola",players[(players.index(player))-1],players.index(player),players.index(players[(players.index(player))-1]))
                print(player.n ,player.suspect)
                sospecha=player.sustec()
                print( sospecha)
                respuesta=players[(players.index(player))-1].response(sospecha)
                print( respuesta)
                player.read(reveal=respuesta)
                print(player.n ,player.suspect)
                
            else:
                pass
   

                
                
def winner(Suspect,win_deck,player):
    count_similaties=0
    for part in Suspect:
        if part in win_deck:
            count_similaties+=1
    if count_similaties==3:
        print("el ganador es ", player)
    else:
        return False
    
def run():
    n_player=int(input("Bienvenido cuantos jugadores quieres que simulemos max son 6"))
    
    players=[]
    repartidas_C,publicas=dealer(n_player,seleccionador())

    
    for key,cards in repartidas_C.items():

        player_m=player(Cartas["Sospechosos"][key],cards)
        player_m.read(cards_pub=Cartas,free_cards=publicas)
        players.append(player_m)
    gestor(players)
    # player1=player("juan",["Cocina","Comendor","Jacuzzi","Bar","Garaje","Baño","Habitación","Taza","Katana","Cable","Caballero Blanco","Sir Blake"])
    # player1.read(Cartas)
    # # player1.read(Cartas, reveal=["Taza"])
    # player1.response(["Jacuzzi"])
    # player1.sustec()
    # player1
    
    # print (Cartas)
    # for key,value  in Cartas.items():   
    #     try:
    #         for i in ["Caballero Blanco","Jacuzzi","Bar","Cable"]:
    #             if i in value:
    #                 value.remove(i)
    #                 print("fuer removido ", i ," en", key)
    #             else:
    #                 continue
    #     except:
    #         continue
    # print ( Cartas)



if __name__ == "__main__":
    run()
