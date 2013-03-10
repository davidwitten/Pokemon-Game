import time
import random
def PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6):
    if pokemon1[0] == 1:
        if pokemon2[0] == 1:
            if pokemon3[0] == 1:
                if pokemon4[0] == 1:
                    if pokemon5[0] == 1:
                        if pokemon6[0] == 1:
                            print("You are full")
                        else:
                            return 6
                    else:
                        return 5
                else:
                    return 4
            else:
                return 3
        else:
            return 2
    else:
        return 1
def foreverSout(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6):
    switchRight = False    
    so = input("Switch out whom?")
    
    while chooseRight!=True:
        switchRight = True
        if diff == 1 and pokemon1[0] + pokemon1[1] == 2:
            print("Okay")
        elif diff == 2 and pokemon2[0] + pokemon2[1] == 2:
            print("Okay")
        elif diff == 3 and pokemon3[0] + pokemon3[1] == 2:
            print("Okay")
        elif diff == 4 and pokemon4[0] + pokemon4[1] == 2:
            print("Okay")
        elif diff == 5 and pokemon5[0] + pokemon5[1] == 2:
            print("Okay")
        elif diff == 6 and pokemon6[0] + pokemon6[1] == 2:
            print("Okay")
        else:
            print("Invalid, so...")
            so = input("To who!")
            switchRight = False        
    return(so)
def power(mypower,opower):
            if mypower.lower() == "normal":
                if opower.lower() == "rock" or opower.lower() == "steel":
                    return "x"
                elif opower.lower() == "ghost":
                    return False
                else:
                    return "Neutral"
            elif mypower.lower() == "fire":
                if opower.lower() == "fire" or opower.lower() == "water" or opower.lower() == "rock" or opower.lower() == "dragon":
                    return "x"#1/2
                elif opower.lower() == "grass" or opower.lower() == "ice" or opower.lower() == "bug" or opower.lower() == "steel":
                    return True#*2
                else:
                    return "Neutral"
            elif mypower.lower() == "water":
                if opower.lower() == "water" or opower.lower() == "grass" or opower.lower() == "dragon":
                    return "x"
                elif opower.lower() == "fire" or opower.lower() == "ground" or opower.lower() == "rock":
                    return True
                else:
                    return "Neutral"
            elif mypower.lower() == "electric":
                if opower.lower() == "water" or opower.lower() == "fly":
                    return True
                elif opower.lower() == "ground":
                    return False
                elif opower.lower() == "electric" or opower.lower() == "grass" or opower.lower() == "dragon":
                    return "x"
                else:
                    return "Neutral"
            elif mypower.lower() == "grass":
                if opower.lower() == "fire" or opower.lower() == "grass" or opower.lower() == "poison" or opower.lower() == "fly" or opower.lower() == "bug" or opower.lower() == "dragon" or opower.lower() == "steel":
                    return "x"
                elif opower.lower() == "water" or opower.lower() == "ground" or opower.lower() == "rock":
                    return True
                else:
                    return "Neutral"
                #true(*2),false(0),x(1/2),neutral-nothing
            elif mypower.lower() == "ice":
                if opower.lower() == "fire" or opower.lower() == "water" or opower.lower() == "ice" or opower.lower() == "steel":
                    return "x"
                elif opower.lower() == "grass" or opower.lower() == "ground" or opower.lower() == "fly":
                    return True
                else:
                    return "Neutral"
            elif mypower.lower() == "fight":
                if opower.lower() == "normal" or opower.lower() == "ice" or opower.lower() == "rock" or opower.lower() == "dark" or opower.lower() == "steel":
                    return True
                elif opower.lower() == "poison" or opower.lower() == "fly" or opower.lower() == "psychic" or opower.lower() == "bug":
                    return "x"
                elif opower.lower() == "ghost":
                    return False
                else:
                    return "Neutral"
            elif mypower.lower() == "poison":
                if opower.lower() == "poison" or opower.lower() == "ground" or opower.lower() == "rock" or opower.lower() == "ghost":
                    return "x"
                elif opower.lower() == "grass":
                    return True
                elif opower.lower() == "steel":
                    return False
                else:
                    return "Neutral"
            elif mypower.lower() == "ground":
                if opower.lower() == "fire" or opower.lower() == "electric" or opower.lower() == "poison" or opower.lower() == "rock" or opower.lower() == "steel":
                    return True
                elif opower.lower() == "grass" or opower.lower() == "bug":
                    return "x"
                elif opower.lower() == "fly":
                    return False
                else:
                    return "Neutral"
            elif mypower.lower() == "fly":
                if opower.lower() == "electric" or opower.lower() == "rock" or opower.lower() == "steel":
                    return "x"
                elif opower.lower() == "grass" or opower.lower() == "fight" or opower.lower() == "bug":
                    return True
                else:
                    return "Neutral"
            elif mypower.lower() == "psychic":
                if opower.lower() == "fight" or opower.lower() == "poison":
                    return True
                elif opower.lower() == "dark":
                    return False
                elif opower.lower() == "psychic" or opower.lower() == "steel":
                    return "x"
                else:
                    return "Neutral"
            elif mypower.lower() == "bug":
                if opower.lower() == "fire" or opower.lower() == "fight" or opower.lower() == "poison" or opower.lower() == "fly" or opower.lower() == "ghost" or opower.lower() == "steel":
                    return "x"
                elif opower.lower() == "grass" or opower.lower() == "dark" or opower.lower() == "psychic":
                    return True
                else:
                    return "Neutral"
            elif mypower.lower() == "rock":
                if opower.lower() == "fire" or opower.lower() == "ice" or opower.lower() == "fly" or opower.lower() == "bug":
                    return True
                elif opower.lower() == "fight" or opower.lower() == "ground" or opower.lower() == "steel":
                    return "x"
                else:
                    return "Neutral"
            elif mypower.lower() == "ghost":
                if opower.lower() == "normal":
                    return False
                elif opower.lower() == "psychic" or opower.lower() == "ghost":
                    return True
                elif opower.lower() == "steel" or opower.lower() == "dark":
                    return "x"
                else:
                    return "Neutral"
            elif mypower.lower() == "dragon":
                if opower.lower() == "dragon":
                    return True
                elif opower.lower() == "steel":
                    return "x"
                else:
                    return "Neutral"
            elif mypower.lower() == "dark":
                if opower.lower() == "fight" or opower.lower() == "dark" or opower.lower() == "steel":
                    return "x"
                elif opower.lower() == "psychic" or opower.lower() == "ghost":
                    return True
                else:
                    return "Neutral"
            elif mypower.lower() == "steel":
                if opower.lower() == "fire" or opower.lower() == "water" or opower.lower() == "electric" or opower.lower() == "steel":
                    return "x"
                elif opower.lower() == "ice" or opower.lower() == "rock":
                    return True
                else:
                    return "Neutral"
            elif mypower.lower() == "champ":
                return True
            elif mypower.lower() == "champion":
                return "2true"
            elif mypower.lower() == "allchamp":
                return "3true"
            elif mypower.lower() == "asdf":
                return False
            else:
                return "Neutral"              
def Quest(hp,opphp,hunger,q1,q2,q3,cow,chicken,plantfood,distance):
    print("1 - Save the Princess")
    print("2 - Beat the Evil Pokemon")
    print("3 - Find Secret Treasure")
    QuestPick = int(input("Enter the number of the quest you wish to attempt."))
    if QuestPick == 1:
        print("Hello, you have begun your quest.")
        print("If you complete this quest, You will get 10000 dollars and 5 fame points.")
        print("Okay, good luck!")
        while opphp < 0:
            totalfood = chicken + cow + plantfood
            print("Quick Stats:")
            print("\tHP:",hp)
            print("\thunger:",hunger)
            print("\tOpponent Health:",opphp)
            print("\tDistance",distance)
            print("Total food in your possesion:",totalfood)
            if distance < 100:
                quechoose1 = input("Your choices are to eat, to advance, or to rest.")
                if quechoose1.lower() == "eat":
                    if totalfood > 0:
                        print(cow,"pieces of cow")
                        print(chicken,"chicken")
                        print(plantfood,"plants")
                        foodchoose = input("Which food?")
                        if foodchoose.lower() == "cow":
                            if cow > 0:
                                cow -= 1
                                hunger += 5
                                print("You now have",cow,"pieces of cow.")
                            else:
                                print("Sorry, you don't have any cow.")
                        elif foodchoose.lower() == "chicken":
                            if chicken > 0:
                                hunger += 10
                                chicken -= 1
                                print("You now have",chicken,"pieces of chicken.")
                            else:
                                print("Sorry, you don't have any chicken.")
                        elif foodchoose.lower() == "plant" or  foodchoose.lower() == "plants":
                            if plantfood > 0:
                                hunger += 15
                                plantfood -= 1
                            else:
                                print("Sorry,you don't ahve any plants.")
                        else:
                            print("Sorry, that is an invalid answer.")
                    else:
                        print("You have no food.")
                        print("Your choice is to hunt.")
                        x = random.randint(1,10)
                        if x >= 6:
                            c = random.randint(1,3)
                            if c == 1:
                                chicken += 1
                                print("You caught a chicken!")
                            elif c == 2:
                                cow += 5
                                print("You caught a cow!")
                            elif c == 3:
                                plantfood += 5
                                print("You found some edible plants!")
                            else:
                                print('this is else')
                        else:
                            hunger -= 10
                            print("You couldn't find anything.")
                elif quechoose1.lower() == "advance":
                    distance +=  50
                    hunger -= 5
                    print("You just advance 10 units you have", 200 - distance,"left to go.")
                    print(hunger,"Hunger Points")
            elif distance >= 100 and distance < 200:
                print("Good job, warrior")
                print("You have passed 100 units.")
                print("You must fight.")
                print("Against a pokemon with level 300.")
                quefight = 1
                opphp = 300
                if opphp < 0 and quefight == 1:
                    distance += 100
                    print("You passed!")
            else:
                print("y")
            
        return(hp ,opphp ,hunger ,q1 ,q2 ,q3, cow, chicken, plantfood, distance)
def Attack(hp,opphp,pp1,pp2,pp3,pp4,pp5,defc,win,opower,mypower,op,nametank,Powerup):
    damage = random.randint(0,20)
    dec = random.randint(10,40)
    stomp = random.randint(5,30)
    kayasaki = random.randint(1,20)
    berry = random.randint(1,5)
    soup = random.randint(1,5)
    
    def criticald(cats):
        if cats >= 30:
            return print("It's a critical hit!")
        return False
    def criticals(stomp):
        if stomp >= 20:
            return print("Critical Hit!")
        return False
    def criticalk(kayasaki):
        if kayasaki >= 15:
            return print("Critical Hit!")
        return False
    def criticalb(damage):
        if damage >= 15:
            return print("That was a critical hit to you.")
        return False
    def berrys(berry):
        if berry >= 4:
            return print("Your opponent found a berry.")
        return False
    def rampage(soup):
        if soup == 5 and pp4 > 0:
            return True
        return False
    if Powerup > 0:
            kayasaki = kayasaki + 30
            dec = dec + 10
            stomp = stomp + 20

    print("Your move choices are:")
    print("%15s%15s" % ("Move","PP"))
    print()
    print("%20s%10d"%("Decimation",pp1))
    print("%15s%15d"%("Stomp",pp2))
    print("%18s%12d"%("Kayasaki",pp3))
    print("%17s%13d"%("Rampage",pp4))
    print("%22s%8d"%("Defense Curl",pp5))
    print()
    print("<INFO>")
    print("\tDecimation is the strongest regular move.")
    print("\tStomp is the 2nd strongest regular move")
    print("\tKayasaki is the weakest attacking regular move.")
    print("\tRampage, has the potential to KnockOut on contact")
    print("\tDefense Curl weakens enemy attacks.")
    
    mymove = input("Which move will you pick?")
    if mymove.lower() == "decimation" or mymove.lower() == "d":
        if pp1 > 0:
            print("Go! use Decimation!")
            print("Your pokemon is focusing...")
            time.sleep(.5)
            pp1 = pp1 - 1
            criticald(dec)
            power(mypower,opower)
            if power(mypower,opower) == "Neutral":
                opphp -= dec
                print("Your attack was fairly effective.")
            elif power(mypower,opower) == "x":
                opphp -= (dec/2)
                print("Not very effective....")
            elif power(mypower,opower) == True:
                opphp -= (dec * 2)
                print("Your strike was super Effective!")
            elif power(mypower,opower) == False:
                print("This doesn't impact your opponent's pokemon.")
            elif power(mypower,opower) == "2true":
                print("Super Super Effective!")
                opphp -= (dec * 3)
            elif power(mypower,opower) == "3true":
                print("Super Duper Super Effective!")
                opphp -= (dec * 4)
            else:
                print(mypower,"Mypower")
                print(opower,"Opower")
                print("Glitch")
                print(power(opower,mypower))
                print(nametank + 1)#reason for that is it will say an error, but i know where it is
            criticalb(damage)
            power(opower,mypower)
            if power(opower,mypower) == "Neutral":
                hp -= damage
                print("Your opponent's strike was fairly effective.")
            elif power(opower,mypower) == "x":
                hp -= (damage/2)
                print("Not very effective against you....")
            elif power(opower,mypower) == True:
                hp -= (damage * 2)
                print("Super Effective to you!")
            elif power(opower,mypower) == False:
                print("This doesn't affect your pokemon.")
            elif power(opower,mypower) == "2true":
                print("Super Super Effective!")
                hp -= (damage * 3)
            elif power(opower,mypower) == "3true":
                print("Super Duper Super Effective!")
                hp -= (damage * 4)
            else:
                print(mypower,"Mypower")
                print(opower,"Opower")
                print("Glitch")
                print(nametank + 1)#reason for that is it will say an error, but i know where it is
            if berrys(berry):
                opphp = opphp + berry
                print("Your opponent found a berry!")
            print("Right now")
            print("%-23s%-10s"% ("Player","HP"))
            print("%-23s%-10d"% ("You", hp))
            print("%-23s%-10d"% ("(Opp.)" + nametank[op],opphp))
        else:
            print("oh, i'm sorry, you have,",pp1,"PP left for that move.")

    elif mymove.lower() == "defense curl" or mymove.lower == "dc":
        if pp5 > 0:                    
            defc = defc + 1
            pp5 = pp5 - 1
            print("You have",pp5,"Moves left for Defense Curl.")
        else:
            print("You have 0 PP left for Defense Curl.")

    elif mymove.lower() == "test" or mymove.lower() == "t":
        opphp = 0
        print("Boomshakalaka")
    elif mymove.lower() == "testlose":
        hp = -1000
        win = 5
    elif mymove.lower() == "stomp" or mymove.lower() == "s":
        if pp2 > 0:
            print("Go, use Stomp!")
            print("Your pokemon is focusing")
            time.sleep(.5)
            print("Your pokemon used Stomp.")
            pp2 = pp2 - 1
            criticals(stomp)
            power(mypower,opower)
            if power(mypower,opower) == "Neutral":
                opphp -= stomp
                print("Fairly effective")
            elif power(mypower,opower) == "x":
                opphp -= (stomp/2)
                print("Ineffective....")
            elif power(mypower,opower) == True:
                opphp -= (stomp * 2)
                print("Super Effective!")
            elif power(mypower,opower) == False:
                if mypower.lower() == "asdf":
                    print("Naveen does no damage.")
                else:
                    print("This doesn't impact your opponent's pokemon.")
            elif power(mypower,opower) == "2true":
                print("Super Super Effective!")
                opphp -= (stomp * 3)
            elif power(mypower,opower) == "3true":
                print("Super Duper Super Effective!")
                opphp -= (stomp * 4)
            else:
                print(mypower,"Mypower")
                print(opower,"Opower")
                print("Glitch")
                print(nametank + 1)#reason for that is it will say an error, but i know where it is
            criticalb(damage)
            power(opower,mypower)
            if power(opower,mypower) == "Neutral":
                hp -= damage
                print("Your opponent's strike was fairly effective.")
            elif power(opower,mypower) == "x":
                hp -= (damage/2)
                print("Not very effective to you....")
            elif power(opower,mypower) == True:
                hp -= (damage * 2)
                print("Super Effective to you!")
            elif power(opower,mypower) == False:
                if mypower.lower() == "asdf":
                    print("Naveen does no damage.")
                else:
                    print("This doesn't impact your pokemon.")
            elif power(mypower,opower) == "2true":
                print("Super Super Effective!")
                hp -= (damage * 3)
            elif power(mypower,opower) == "3true":
                print("Super Duper Super Effective!")
                hp -= (damage * 4)
            else:
                print(mypower,"Mypower")
                print(opower,"Opower")
                print("Glitch")
                print(nametank + 1)#reason for that is it will say an error, but i know where it is
            if berrys(berry):
                opphp = opphp + berry
                print("Your opponent found a berry!")
            print("Right now")
            print("%-23s%-10s"% ("Player","HP"))
            print("%-23s%-10d"% ("You", hp))
            print("%-23s%-10d"% ("(Opp.)" + nametank[op],opphp))
        else:
            print("Sorry, you have",pp2,"PP left for the Stomp Move.")
    elif mymove.lower() == "kayasaki" or mymove.lower() == "k":
        if pp3 > 0:
            print("Attack! Use KAYASAKI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            time.sleep(.3)
            print("Your pokemon just used Kayasaki.")
            pp3 = pp3 - 1
            criticalk(kayasaki)
            power(mypower,opower)
            if power(mypower,opower) == "Neutral":
                opphp -= kayasaki
                print("Fairly effective")
            elif power(mypower,opower) == "x":
                opphp -= (kayasaki/2)
                print("Ineffective....")
            elif power(mypower,opower) == True:
                opphp -= (kayasaki * 2)
                print("Super Effective!")
            elif power(mypower,opower) == False:
                if mypower.lower() == "asdf":
                    print("Naveen does no damage.")
                else:
                    print("This doesn't impact your opponent's pokemon.")
            elif power(mypower,opower) == "2true":
                print("Super Super Effective!")
                opphp -= (kayasaki * 3)
            elif power(mypower,opower) == "3true":
                print("Super Duper Super Effective!")
                opphp -= (kayasaki * 4)
            else:
                print(mypower,"Mypower")
                print(opower,"Opower")
                print("Glitch")
                print(nametank + 1)#reason for that is it will say an error, but i know where it is
            criticalb(damage)
            power(opower,mypower)
            if power(opower,mypower) == "Neutral":
                hp -= damage
                print("Your opponent's strike was fairly effective.")
            elif power(opower,mypower) == "x":
                hp -= (damage/2)
                print("Not very effective to you....")
            elif power(opower,mypower) == True:
                hp -= (damage * 2)
                print("Super Effective to you!")
            elif power(opower,mypower) == False:
                if mypower.lower() == "asdf":
                    print("Your Naveen does no damage.")
                else:
                    print("This doesn't impact your pokemon.")
            elif power(opower,mypower) == "2true":
                print("Super Super Effective!")
                hp -= (damage * 3)
            elif power(opower,mypower) == "3true":
                print("Super Duper Super Effective!")
                hp -= (damage * 4)
            else:
                print(mypower,"Mypower")
                print(opower,"Opower")
                print("Glitch")
                print(nametank + 1)#reason for that is it will say an error, but i know where it is
            if berrys(berry):
                opphp += berry
                print("Your opponent found a berry!")
            print("Right now,")
            print("%-23s%-10s"% ("Player","HP"))
            print("%-23s%-10d"% ("You", hp))
            print("%-23s%-10d"% ("(Opp.)" + nametank[op],opphp))
    elif mymove.lower() == "r" or mymove.lower() == "rampage" :
        if pp4 > 0:
            hp -= damage
            print("Your hp:",hp)
            print("Your opponent's",opphp)
            pp4 -= 1 
            print("The riskiest move in the game...")
            input("Your pokemon is sweating up a storm!")
            if rampage(soup) == True:
                input("You won because of rampage!")
                opphp = -10
            print("The move may have been unsuccesful, but at least you tried!")
            print("Now the Rampage move has", pp4,"PP.")
        else:
            print("Sorry, but that is an invalid option,for you have",pp4,"PP for the Rampage move.")

    else:
        print("I don't think that is a real move, or you just misspelled it.")
    return (hp, opphp, pp1, pp2, pp3, pp4, pp5, defc, win)
def PrintVar(deposit,moneybank,money,ppill,ppp,hppp,fppp,frpp,stone,bould,blaster,blaster_ammo,Powerup,HPdecreaser,HPdecreaser2,HPdecreaser3,HPdecreaser4,arrow,pokepp,ultrapp):
    print("Your deposited money:",deposit)
    print("Your money in bank:",moneybank)
    print("Your pocket money:",money)
    print("Items:")
    print(ppill,"PP restoring pill(s).")
    print(ppp,"potion(s).")
    print(hppp,"hyper potion(s).")
    print(ultrapp,"Ultra Ball(s).")
    print(fppp,"Full Potion(s)")
    print(frpp,"Full Restore(s)")
    print(stone,"Stone(s)")
    print(bould,"boulder(s)")
    print(blaster,"blaster(s), although you only need 1.")
    print(blaster_ammo,"blaster ammo(s).")
    print(Powerup,"Powerup(s).")
    if HPdecreaser > 0:
        if HPdecreaser2 > 0:
            if HPdecreaser3 > 0:
                if HPdecreaser4 > 0:
                    print(HPdecreaser4,"Final level upgrade HPdecreaser(s).")
                else:
                    print(HPdecreaser3,"3rd-level upgraded HPdecreaser(s).")
            else:
                print(HPdecreaser2,"2nd-level upgraded HPdecreaser(s).")
        else:
            print(HPdecreaser,"Starter HPdecreaser(s).")
    else:
        print(HPdecreaser,"Starter HPdecreaser(s).")                                
    print(arrow,"arrow(s)")
    print(pokepp,"Pokeballs")
    if deposit != moneybank:
        print("Note: If deposited money and money in bank are different: it's not broken.")
def ChooseDifficulty():
    chooseRight = False    
    diff = input("Before we begin, what difficulty do you want it on?(easy, normal, hard, expert, or EXTREMEexpert(just type 'ee')?")
    
    while chooseRight!=True:
        chooseRight = True
        if diff.lower() == "easy" or diff.lower() == "e":
            print("I see that you either are lazy or are a beginner. It's okay, that's how all the master pokemon trainers started.")
        elif diff.lower() == "n" or diff.lower() == "normal":
            print("I see that you like the normal difficulty the best, i agree.")
        elif diff.lower() == "h" or diff.lower() == "hard":
            print("I see that you are a pretty good pokemon trainer.")
        elif diff.lower() == "ex" or diff.lower() == "expert":
            print("You must be a real pokemon master.")
        elif diff.lower() == "extreme expert" or diff.lower() == "extremeexpert" or diff.lower() == "ee":
            print("This is almost impossible.")
            print("I salute you, captain!")
        else:
            print("I don't understand, probably because my primary language is binary.")
            diff = input("Which difficulty!")
            chooseRight = False        
    return(diff)
def ChooseLength():
    chooseRight = False    
    lig = input("Do you want a long, short, or medium-length game?")    
    while chooseRight!=True:
        chooseRight = True
        if lig.lower() == "short" or lig.lower() == "s":
            print("Congrats, you will play short games.")
        elif lig.lower() == "medium" or lig.lower() == "m":
            print("Congrats, you'll play medium-length games.")
        elif lig.lower() == "long" or lig.lower() == "l" :
            print("You are officially going to play long games.")
        else:
            print("I didn't quite get that.")
            lig = input("Which difficulty?")
            chooseRight = False        
    return(lig)
def SaveGame(outputFile,name,hp,win,money,Powerup,opphp,pp1,pp2,pp3,pp4,pp5,diff,lig,blaster,blaster2,blaster3,blaster4,blaster_ammo,HPdecreaser,HPdecreaser2,HPdecreaser3,HPdecreaser4,arrow,hunger,cow,chicken,plantfood,deposit,moneybank,strdeposit,depoadd,withdraw,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6,h1n,h2n,h3n,h4n,h5n,h6n,pp1n1,pp1n2,pp1n3,pp1n4,pp1n5,pp1n6,pp2n1,pp2n2,pp2n3,pp2n4,pp2n5,pp2n6,pp3n1,pp3n2,pp3n3,pp3n4,pp3n5,pp3n6,pp4n1,pp4n2,pp4n3,pp4n4,pp4n5,pp4n6,pp5n1,pp5n2,pp5n3,pp5n4,pp5n5,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,power1n,power2n,power3n,power4n,power5n,power6n,totactiv,totalife,mypower,op,ppill):
    f = open(outputFile + "save_" + name + ".log",'w')
    f.write(str([opphp,win,hp,money,pp1,pp2,pp3,pp4,pp5,op,hp]) + "\n")
    f.write(str(diff) + "\n")
    f.write(str(lig) + "\n")
    f.write(str([blaster,blaster2,blaster3,blaster4, blaster_ammo,hp]) + "\n")
    f.write(str([HPdecreaser,HPdecreaser2,HPdecreaser3,HPdecreaser4,arrow,Powerup,hp]) + "\n")
    f.write(str([hunger,cow,chicken,plantfood,hp]) + "\n")
    f.write(str([moneybank,deposit,strdeposit,depoadd,withdraw,ppill,hp]) + "\n")
    f.write(str([h1n,h2n,h3n,h4n,h5n,h6n,hp]) + "\n")
    f.write(str([pp1n1,pp1n2,pp1n3,pp1n4,pp1n5,pp1n6,hp]) + "\n")
    f.write(str([pp2n1,pp2n2,pp2n3,pp2n4,pp2n5,pp2n6,hp]) + "\n")
    f.write(str([pp3n1,pp3n2,pp3n3,pp3n4,pp3n5,pp3n6,hp]) + "\n")
    f.write(str([pp4n1,pp4n2,pp4n3,pp4n4,pp4n5,pp4n6,hp]) + "\n")
    f.write(str([pp5n1,pp5n2,pp5n3,pp5n4,pp5n5,pp5n6,hp]) + "\n")
    f.write(str([p1n.strip("'"),p2n.strip("'"),p3n.strip("'"),p4n.strip("'"),p5n.strip("'"),p6n.strip("'"),hp]) + "\n")
    f.write(str([pokemon1[0],pokemon2[0],pokemon3[0],pokemon4[0],pokemon5[0],pokemon6[0],pokemon1[1],pokemon2[1],pokemon3[1],pokemon4[1],pokemon5[1],pokemon6[1],hp]) + "\n")
    f.write(str([power1n.strip('"').strip("'").strip('/'),power2n.strip("'").strip('"').strip('/'),power3n.strip("'").strip('"').strip('/'),power4n.strip("'").strip('"').strip('/'),power5n.strip("'").strip('"').strip('/'),power6n.strip("'").strip('"').strip('/'),hp]) + "\n")
    f.write(str([totactiv,totalife,mypower,hp]) + "\n")
    f.close()
   
def PowerInfo():
    print("\t\t<Normal> is neutral against all except that it is ineffective against ghost, and is weakened against Rock and Steel.")
    print("\t\t<Fire> is super effective against grass, ice, bug, and steel. It is weak against itself, water, rock, and dragon.")
    print("\t\t<Water> is super effective against  fire, ground and rock.")
    print("\t\t<Electric> is super effective against water, and flying. It is completely ineffective against ground.")
    print("\t\t<Grass> is super effective against water, ground, and rock. It is ineffective against fire, grass, poison, flying, bug, dragon, and steel.>")
    print("\t\t<Ice> is super effective against grass, ground, flying, and dragon.")
    print("\t\t<Fight> is super effective against normal, ice, rock, dark, and steel. It has no effect on ghosts.")
    print("\t\t<Poison> is super effective against grass and has no effect on steel.")
    print("\t\t<Ground> is super effective against fire, electric, poison, rock, and steel.it has no effect on flying.")
    print("\t\t<Flying is super effective against grass, fighting, and bug-type pokemon.")
    print("\t\t<Psychic> is super effective against flying and poison, but doesn't effect dark.")
    print("\t\t<Bug> is super effective against grass, psychic, and dark.")
    print("\t\t<Rock> is super effective against fire, ice, flying, and bug-type pokemon.")
    print("\t\t<Ghost> is super effective against ghost, and psychic type pokemon, and has no effect on normal pokemon.")
    print("\t\t<Dragon> is only super effective against dragon.")
    print("\t\t<Dark> is super effective against ghost, and psychic-type pokemon.")
    print("\t\t<Steel is super effective against ice, and rock-type pokemon.")
def CheckName(OutputDir, name):
    import os
    found = False
    hp = 100
    if name.lower() == "ash ketchum":
        print("Oh my god, welcome ash!")
        hp = 300
    elif name.lower() == "david" or name.lower() == "david w":
        print("Oh hi david.")
        print("Hello master, what a pleasure that you are playing or test out your own game!")
    print("Hey", name,"! Welcome to Pokemon World!")

    fList = os.listdir(OutputDir)
    for fName in fList:
        if fName == "save_" + name + ".log":
            found = True
            choice = input("We see you've played with us before. Would you like to continue? (y/n)")
            if choice.lower() == "y":
                f = open(OutputDir + fName,'r')
                vitals = f.readline().strip('[').strip(']').strip('"\n"').split(', ')#vitals
                opphp = float(vitals[0])
                win = int(vitals[1])
                hp = float(vitals[2])
                money = float(vitals[3])
                pp1 = int(vitals[4])
                pp2 = int(vitals[5])
                pp3 = int(vitals[6])
                pp4 = int(vitals[7])
                pp5 = int(vitals[8])
                op = int(vitals[9])
                diff = str(f.readline()).strip('"\n"')
                lig = str(f.readline()).strip('"\n"')
                blasters = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')#blasters
                blaster = int(blasters[0])
                blaster2 = int(blasters[1])
                blaster3 = int(blasters[2])
                blaster4 = int(blasters[3])
                blaster_ammo = int(blasters[4])
                weaps = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')#weapons
                HPdecreaser = int(weaps[0])
                HPdecreaser2 = int(weaps[1])
                HPdecreaser3 = int(weaps[2])
                HPdecreaser4 = int(weaps[3])
                arrow = int(weaps[4])
                Powerup = int(weaps[5])
                hung = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')#hunger
                hunger = int(hung[0])
                cow = int(hung[1])
                chicken = int(hung[2])
                plantfood = int(hung[3])
                rmoney = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')#rest of money
                moneybank = float(rmoney[0])
                deposit = float(rmoney[1])
                strdeposit = float(rmoney[2])
                depoadd = float(rmoney[3])
                withdraw = float(rmoney[4])
                ppill = int(rmoney[5])
                hnn = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')#All personal health
                h1n = round(float(hnn[5]))
                h2n = round(float(hnn[5]))
                h3n = round(float(hnn[5]))
                h4n = round(float(hnn[5]))
                h5n = round(float(hnn[5]))
                h6n = round(float(hnn[5]))
                pp1p = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')#all pp1
                pp1n1 = int(pp1p[0])
                pp1n2 = int(pp1p[1])
                pp1n3 = int(pp1p[2])
                pp1n4 = int(pp1p[3])
                pp1n5 = int(pp1p[4])
                pp1n6 = int(pp1p[5])
                pp2p = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')#all pp1
                pp2n1 = int(pp2p[0])
                pp2n2 = int(pp2p[1])
                pp2n3 = int(pp2p[2])
                pp2n4 = int(pp2p[3])
                pp2n5 = int(pp2p[4])
                pp2n6 = int(pp2p[5])
                pp3p = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')#all pp1
                pp3n1 = int(pp3p[0])
                pp3n2 = int(pp3p[1])
                pp3n3 = int(pp3p[2])
                pp3n4 = int(pp3p[3])
                pp3n5 = int(pp3p[4])
                pp3n6 = int(pp3p[5])
                pp4p = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')#all pp1
                pp4n1 = int(pp4p[0])
                pp4n2 = int(pp4p[1])
                pp4n3 = int(pp4p[2])
                pp4n4 = int(pp4p[3])
                pp4n5 = int(pp4p[4])
                pp4n6 = int(pp4p[5])
                pp5p = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')#all pp1
                pp5n1 = int(pp5p[0])
                pp5n2 = int(pp5p[1])
                pp5n3 = int(pp5p[2])
                pp5n4 = int(pp5p[3])
                pp5n5 = int(pp5p[4])
                pp5n6 = int(pp5p[5])
                namez = f.readline().strip('[').strip(']').strip('"\n"').split(', ')#all names.strip('"').strip('/')
                p1n = namez[0].strip("'").strip("'")
                p2n = namez[1].strip("'").strip("'")
                p3n = namez[2].strip("'").strip("'")
                p4n = namez[3].strip("'").strip("'")
                p5n = namez[4].strip("'").strip("'")
                p6n = namez[5].strip("'").strip("'")
                ol = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')
                pokemon1 = [0,0,0,0,0,0,0,0,0,0]
                pokemon2 = [0,0,0,0,0,0,0,0,0,0]
                pokemon3 = [0,0,0,0,0,0,0,0,0,0]
                pokemon4 = [0,0,0,0,0,0,0,0,0,0]
                pokemon5 = [0,0,0,0,0,0,0,0,0,0]
                pokemon6 = [0,0,0,0,0,0,0,0,0,0]
                pokemon1[0] = int(ol[0])
                pokemon2[0] = int(ol[1])
                pokemon3[0] = int(ol[2])
                pokemon4[0] = int(ol[3])
                pokemon5[0] = int(ol[4])
                pokemon6[0] = int(ol[5])
                pokemon1[1] = int(ol[6])
                pokemon2[1] = int(ol[7])
                pokemon3[1] = int(ol[8])
                pokemon4[1] = int(ol[9])
                pokemon5[1] = int(ol[10])
                pokemon6[1] = int(ol[11])
                power = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')#power
                power1n = power[0].strip("'").strip("'")
                power2n = power[1].strip("'").strip("'")
                power3n = power[2].strip("'").strip("'")
                power4n = power[3].strip("'").strip("'")
                power5n = power[4].strip("'").strip("'")
                power6n = power[5].strip("'").strip("'")
                
                xxx = f.readline().strip('[').strip(']').strip('"\n"').strip('"').strip('/').split(', ')
                totalife = int(xxx[1])
                totactiv = int(xxx[0])
                mypower = xxx[2]
                pokemon1 = [pokemon1[0],pokemon1[1],h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1, p1n,power1n]
                pokemon2 = [pokemon2[0],pokemon2[1],h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2, p2n,power2n]
                pokemon3 = [pokemon3[0],pokemon3[1],h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3, p3n,power3n]
                pokemon4 = [pokemon4[0],pokemon4[1],h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4, p4n,power4n]
                pokemon5 = [pokemon5[0],pokemon5[1],h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5, p5n,power5n]
                pokemon6 = [pokemon6[0],pokemon6[1],h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6, p6n,power6n]
                f.close()
            else:
                win = 0
                hp = 100
                money = 100
                opphp = 100
                blaster = 0
                blaster2 = 0
                blaster3 = 0
                blaster4 = 0
                blaster_ammo = 0
                HPdecreaser = 0
                HPdecreaser2 = 0
                HPdecreaser3 = 0
                HPdecreaser4 = 0
                arrow = 0
                Powerup = 0
                pp1 = 5
                pp2 = 10
                pp3 = 20
                pp4 = 2
                pp5 = 10
                hunger = 100
                cow = 0
                chicken = 0
                plantfood = 0
                deposit = 0
                moneybank = 0
                strdeposit = 0
                depoadd = 0
                withdraw = 0
                h1n = 100
                h2n = 101
                h3n = 102
                h4n = 103
                h5n = 104
                h6n = 105
                pp1n1 = 5
                pp1n2 = 5
                pp1n3 = 5
                pp1n4 = 5
                pp1n5 = 5
                pp1n6 = 5
                pp2n1 = 10
                pp2n2 = 10
                pp2n3 = 10
                pp2n4 = 10
                pp2n5 = 10
                pp2n6 = 10
                pp3n1 = 20
                pp3n2 = 20
                pp3n3 = 20
                pp3n4 = 20
                pp3n5 = 20
                pp3n6 = 20
                pp4n1 = 2
                pp4n2 = 2
                pp4n3 = 2
                pp4n4 = 2
                pp4n5 = 2
                pp4n6 = 2
                pp5n1 = 10
                pp5n2 = 10
                pp5n3 = 10
                pp5n4 = 10
                pp5n5 = 10
                pp5n6 = 10
                p1n = 'Digisaurus'
                p2n = ''
                p3n = ''
                p4n = ''
                p5n = ''
                p6n = ''
                power1n = 'Normal'
                power2n = ''
                power3n = ''
                power4n = ''
                power5n = ''
                power6n = ''
                totalife = 1
                totactiv = 1
                pokemon1 = [1,1,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1, p1n,power1n]
                pokemon2 = [0,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2, p2n,power2n]
                pokemon3 = [0,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3, p3n,power3n]
                pokemon4 = [0,0,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4, p4n,power4n]
                pokemon5 = [0,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5, p5n,power5n]
                pokemon6 = [0,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6, p6n,power6n]
                diff = ChooseDifficulty()
                lig = ChooseLength()
                mypower = 'Normal'
                op = random.randint(0,31)
                ppill = 0
    if not found:
        win = 0
        hp = 100
        money = 100
        opphp = 100
        pp1 = 5
        pp2 = 10
        pp3 = 20
        pp4 = 2
        pp5 = 10
        diff = ChooseDifficulty()
        lig = ChooseLength()
        blaster = 0
        blaster2 = 0
        blaster3 = 0
        blaster4 = 0
        blaster_ammo = 0
        HPdecreaser = 0
        HPdecreaser2 = 0
        HPdecreaser3 = 0
        HPdecreaser4 = 0
        hunger = 100
        cow = 0
        Powerup = 0
        chicken = 0
        plantfood = 0
        deposit = 0
        moneybank = 0
        strdeposit = 0
        depoadd = 0
        withdraw = 0
        h1n = 100
        h2n = 101
        h3n = 102
        h4n = 103
        h5n = 104
        h6n = 105
        pp1n1 = 5
        pp1n2 = 5
        pp1n3 = 5
        pp1n4 = 5
        pp1n5 = 5
        pp1n6 = 5
        pp2n1 = 10
        pp2n2 = 10
        pp2n3 = 10
        pp2n4 = 10
        pp2n5 = 10
        pp2n6 = 10
        pp3n1 = 20
        pp3n2 = 20
        pp3n3 = 20
        pp3n4 = 20
        pp3n5 = 20
        pp3n6 = 20
        pp4n1 = 2
        pp4n2 = 2
        pp4n3 = 2
        pp4n4 = 2
        pp4n5 = 2
        pp4n6 = 2
        pp5n1 = 10
        pp5n2 = 10
        pp5n3 = 10
        pp5n4 = 10
        pp5n5 = 10
        pp5n6 = 10
        p1n = 'Digisaurus'
        p2n = ''
        p3n = ''
        p4n = ''
        p5n = ''
        p6n = ''
        power1n = 'Normal'
        mypower = 'Normal'
        power2n = ''
        power3n = ''
        power4n = ''
        power5n = ''
        power6n = ''
        totalife  = int(1)
        totactiv = int(1)
        pokemon1 = [1,1,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1, p1n,power1n]
        pokemon2 = [0,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2, p2n,power2n]
        pokemon3 = [0,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3, p3n,power3n]
        pokemon4 = [0,0,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4, p4n,power4n]
        pokemon5 = [0,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5, p5n,power5n]
        pokemon6 = [0,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6, p6n,power6n]
        arrow = 0
        op = random.randint(0,31)
        ppill = 0
    return(name,hp,win,money,Powerup,opphp,pp1,pp2,pp3,pp4,pp5,diff,lig,blaster,blaster2,blaster3,blaster4,blaster_ammo,HPdecreaser,HPdecreaser2,HPdecreaser3,HPdecreaser4,arrow,hunger,cow,chicken,plantfood,deposit,moneybank,strdeposit,depoadd,withdraw,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6,h1n,h2n,h3n,h4n,h5n,h6n,pp1n1,pp1n2,pp1n3,pp1n4,pp1n5,pp1n6,pp2n1,pp2n2,pp2n3,pp2n4,pp2n5,pp2n6,pp3n1,pp3n2,pp3n3,pp3n4,pp3n5,pp3n6,pp4n1,pp4n2,pp4n3,pp4n4,pp4n5,pp4n6,pp5n1,pp5n2,pp5n3,pp5n4,pp5n5,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,power1n,power2n,power3n,power4n,power5n,power6n,totactiv, totalife,mypower,op,ppill)
def hints(hp,opphp,pp1,pp2,pp3,pp4,pp5,name):
    if hp < opphp:
        if hp < 50:
            if hp < 25:
                if hp < 10:
                    if hp < 5:
                        if hppp > 0:
                            print("I would definitely use a hyper potion.")
                        else:
                            if pp4 > 0:
                                print(" I would definitely go for the KO, use Rampage!")
                            else:
                                if pp1 > 0:
                                    print("I don't know..., Decimation would be a pretty good option.")
                                else:
                                    if pp2 > 0:
                                        print("Well I know that you can't use your strongest move(s), but you can still use Stomp.")
                                        print("I would choose Stomp. Or restore all PP with a PP pill, and be able to use Rampage,and Decimation again.")
                                    else:
                                        if pp3 > 0:
                                            print("Sorry, Kayasaki is your last resort, or you can always use a pokeball.")
                                        else:
                                            if pokepp > 0:
                                                print("Just use a pokeball!")
                                            else:
                                                print("You're screwed.")
                    else:
                        if hp == 5:
                            if hppp > 0:
                                print("I would definitely use a hyper potion.")
                            else:
                                if pp4 > 0:
                                    print(" I would definitely go for the KO, use Rampage!")
                                else:
                                    if pp1 > 0:
                                        print("I don't know..., Decimation would be a pretty good option.")
                                    else:
                                        if pp2 > 0:
                                            print("Well I know that you can't use your strongest move(s), but you can still use Stomp.")
                                            print("I would choose Stomp. Or restore all PP with a PP pill, and be able to use Rampage,and Decimation again.")
                                        else:
                                            if pp3 > 0:
                                                print("Sorry, Kayasaki is your last resort, or you can always use a pokeball.")
                                            else:
                                                if pokepp > 0:
                                                    print("Just use a pokeball!")
                                                else:
                                                    if money > 0:
                                                        print("Go to the pokemon store.")
                                                    else:
                                                        print("You really are screwed.")
                        else:
                            if hppp > 0:
                                print("I would definitely use a hyper potion.")
                            else:
                                if pp4 > 0:
                                    print(" I would definitely go for the KO, use Rampage!")
                                else:
                                    if pp1 > 0:
                                        print("I don't know..., Decimation would be a pretty good option.")
                                    else:
                                        if pp2 > 0:
                                            print("Well I know that you can't use your strongest move(s), but you can still use Stomp.")
                                            print("I would choose Stomp. Or restore all PP with a PP pill, and be able to use Rampage,and Decimation again.")
                                        else:
                                            if pp3 > 0:
                                                print("Sorry, Kayasaki is your last resort, or you can always use a pokeball.")
                                            else:
                                                if pokepp > 0:
                                                    print("Just use a pokeball!")
                                                else:
                                                    print("You're screwed.LOL")
                            
                else:
                    if pp4 > 0:
                        print("I might recommend trying to KO the opponent, you have less than 20 HP.")
                    else:
                        if pp1 > 0:
                            print("I don't know..., Decimation would be a pretty good option. It is a strong move, and you can win if you are lucky")
                        else:
                            if pp2 > 0:
                                print("Well I know that you can't use your strongest move(s), but you can still use Stomp.")
                                print("I would choose Stomp. Or use a PP pill and restore all PP.")
                            else:
                                if pp3 > 0:
                                    if ppill <= 0:
                                        print("Sorry, Kayasaki is your last resort, or you can always use a pokeball.")
                                    else:
                                        print("Use a PP pill!(in inventory)")
                                else:
                                    if pokepp > 0:
                                        print("Just use a pokeball! You still have a chance!")
                                    else:
                                        print("You're kinda screwed, use a PP pill.It will restore all your moves(Probably should've told you sooner;P)")
            else:
                if pp1 > 0:
                    print("I might recommend trying to win the opponent with Decimation, and plus, you have over 20 HP. Decisions aren't as important as when you are under 10 HP.")
                else:
                    if pp4 > 0:
                        print("I don't know..., Decimation would be a pretty good option, if you could use it,I know this is risky, but I would try Rampage, even though you have over 20 HP, and your opponent has more.")
                    else:
                        if pp2 > 0:
                            if ppill > 0:
                                print("Well I know that you can't use your strongest move(s), but you can still use Stomp.")
                                print("I would choose Stomp. Or use a PP pill and restore all PP.")
                            else:
                                print("USE STOMP!, it's your best option of survival!")
                        else:
                            if pp3 > 0:
                                if ppill <= 0:
                                    print("Sorry, Kayasaki is your last resort, or you can always use a pokeball.")
                                else:
                                    print("Use a PP pill!(in inventory)")
                            else:
                                if pokepp > 0:
                                    print("Just use a pokeball! You still have a chance!")
                                else:
                                    print("You're kinda screwed, use a PP pill.It will restore all your moves(Probably should've told you sooner;P)")
        else:
            if pp1 > 0:
                print("Decimation is your best friend in this case scenario, you're losing, but you have more than 50 HP")
                print("You shouldn't panic.")
            else:
                if pp4 > 0:
                    if ppill > 0:
                        print("Decimation was your best choice, but since you can't do that, you should use a PPill, or just use Rampage!")
                    else:
                        print("Use rampage!")
                else:
                    if pp2 > 0:
                        if ppill > 0:
                            print("I'd strongly recommend using a PPill, or use Stomp.")
                        else:
                            print("Use STOMP!")
                    else:
                        if pp3 > 0:
                            if ppill > 0:
                                print("I'd seriously recommend using the PPill. Kayasaki isn't the most reliable of moves.")
                            else:
                                print("I'd use Kayasaki!")
                        else:
                            if pokepp > 0:
                                print("Look. You have", pokepp,"Pokeballs and no moves left, this is your only chance to win.")
                            else:
                                print("LOL, you lose!LOL LOL LOL LOL LOL LOL LOL LOL LOL LOL LOL" * 5)
                        
    elif hp > opphp:
        if opphp < 20:
            if opphp < 10:
                if pp1 > 0:
                    print("I might use a pokeball, or use Decimation!")
                else:
                    if ppill > 0:
                        print("Use a PPILL!")
                    else:
                        if pp4 > 0:
                            print("Use Rampage!")
                        else:
                            if pp2 > 0:
                                print("USe Stomp!")
                            else:
                                if pp3 > 0:
                                    print("Use Kayasaki!")
                                else:
                                    if pokepp > 0:
                                        print("Go for the catch!")
                                    else:
                                        print("How were you leading in the first place?" + "LOL LOL LOL LOL" * 500)
            else:
                if pp1 > 0:
                    print("I might use a pokeball, or use Decimation(Recommended)!")
                else:
                    if ppill > 0:
                        print("Use a PPILL!")
                    else:
                        if pp4 > 0:
                            print("Use Rampage!")
                        else:
                            if pp2 > 0:
                                print("USe Stomp!")
                            else:
                                if pp3 > 0:
                                    print("Use Kayasaki!")
                                else:
                                    if pokepp > 0:
                                        print("Go for the catch!")
                                    else:
                                        print("How were you leading in the first place?" + "LOL LOL LOL LOL" * 500)
        else:
            if hp - 30 > opphp:
                print("You are decimating right now, keep up the good work, you don't need my help.")
                print("I'm just the programmer who made this program.No big deal!")
                print("You don't need my insight, Bah!")
            else:
                if hp - 20 > opphp:
                    print("You are still crushing your opponent.")
                    print("Why would you ask me?")
                    print("I'm just the programmer who made this program.No big deal!")
                    print("You don't need my insight, Bah!")
                else:
                    if hp - 10 > opphp:
                        print("Hmm, just use the moves in order of strength:1. Decimation Also, 1. Rampage(Hard to Classify because can inflict 0 or win pokemon) 2. Stomp 3.Kayasaki")
                    else:
                        if hp - 5 > opphp:
                            print("I see that it us very close.Use your moves in order of strength, Decimation, Rampage, Stomp and Kayasaki")
    else:
        if hp == 100:
            print("You just started the game!")
            print("Stop abusing my powers!")
        else:
            print("This is serious, two pokemon are tied. Stop slacking and fight, you don't need my advice, I'm just a collection of words on a monitor!You'd trust me?")
def PokemonCenter(money,h1n,h2n,h3n,h4n,h5n,h6n,hp):
    thiefr = random.randint(1,10)
    def thief():
        if thiefr >= 5:
            return True
        else:
            return False
    if money > 0:
        hp = 100
        print("Your hp has been restored.")
        print("Your average hp",((h1n + h2n + h3n + h4n + h5n + h6n)/6))
        print("But we are not as nice as the nurses in the real game.")
        print("You must pay me.")
        thef = input("Will you steal? (y or n)")
        if thef.lower() == "y" or thef.lower() == "yes":
            if thief() == True:
                print("...")
                time.sleep(1)
                print("You got away!")
                print("Luckily, those nurses forgot your face, so you can keep healing your pokemon.")
                h1n = 100
                h2n = 100
                h3n = 100
                h4n = 100
                h5n = 100
                h6n = 100
                print("Your average HP is now",((h1n + h2n + h3n + h4n + h5n + h6n)/6))
            else:
                print("...")
                time.sleep(1)
                print("Well you failed, and the Pokemon Police stopped you.")
                print("You payed $75, for the police ticket was $25.")
                money -= 75
                h1n = 100
                h2n = 100
                h3n = 100
                h4n = 100
                h5n = 100
                h6n = 100
                print("At least your average HP is now", ((h1n + h2n + h3n + h4n + h5n + h6n)/6))
        elif thef.lower() == "n" or thef.lower() == "no":
            print("Well good. Stealing is bad.")
            money -= 50
            hp = 100
            h1n = 100
            h2n = 100
            h3n = 100
            h4n = 100
            h5n = 100
            h6n = 100
        else:
            print("No comprendo.")
            money -= 50
            hp = 100
            h1n = 100
            h2n = 100
            h3n = 100
            h4n = 100
            h5n = 100
            h6n = 100
    else:
        print("You don't have enough money to heal your pokemon.")
        print("But you can fight to earn money.")
        print("Just go back to the arena.")
    return (money, h1n, h2n, h3n, h4n, h5n, h6n, hp)
