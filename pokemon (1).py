import time
import random
import AuxFunctions
import pyglet
"""
David W.
Program Complete (for now....)
v.1.2
"""
#############################################
outputFile = 'C:/Python33/David/Pokemon/Output/'
player = pyglet.media.Player()
nametank = ["Trimonocole","Trimonocle X","Almighty Trimonocle","Windowsaur","Rocketman","Karateking","Jujitschamp","Pokeon","Monpoke","Megladon","Macsquito","Drago","Packman","Monkeyman","Superman","Man","Beestorm","Olympio","Slithero","Boultron","Digitalus","Misterio","Frogbob","Longnorm","Pokemontisaurus","Candyman","Bicyclone","Blazetron","Hydron","Volta","Brain Man","Ironsaur","Naveen","Naveen","Boss A","Boss B"]
powers = ["Champ","Champion","Allchamp","Ground","Flying","Fight","Fight","Normal","Normal","Water","Bug","Dragon","Dark","Grass","Flying","Normal","Bug","Ghost","Grass","Rock","Metal","Normal","Adaptive","Normal","Dragon","Ice","Normal","Fire","Water","Electric","Psychic","Steel","ASDF","ASDF","Champ","Champ"]

#money/bank
a = 0
b = 0
op = random.randint(1,len(powers)-3)
opower = powers[op]
mypower = 'Normal'
quefight = 0
money = int(100)
moneybank = int(0)
deposit = int(0)
strdeposit = int(0)
depoadd = int(0)
withdraw = int(0)
#hps
hp = int(100)
hunger = int(100)
cow = int(0)
chicken = int(0)
plantfood = int(0)
wheat = 0
bread = 0
totalfood = cow + chicken + plantfood
fail = 0
#quest
q1 = int(0)
q2 = int(0)
q3 = int(0)
distance = int(0)
opphp = 100
#pp's
pp1 = int(5)
pp2 = int(10)
pp3 = int(20)
pp4 = int(2)
pp5 = int(10)
#potion
ppp = int(10)
#berry
berry = int(5)
#pokeball
pokepp = int(20)
ultrapp = int(5)
#other potions and heals
hppp = int(1)
fppp = int(0)
frpp = int(0)
ppill = int(1)
#other battle items in inventory
stone = int(0)
rock = int(0)
bould = int(0)
#market
    #blaster
blaster = int(0)
blaster2 = int(0)
blaster3 = int(0)
blaster4 = int(0)
blaster_ammo = int(0)
    #HPdecreaser
HPdecreaser = int(0)
HPdecreaser2 = int(0)
HPdecreaser3 = int(0)
HPdecreaser4 = int(0)
arrow = int(0)
Powerup = int(0)
#more inv
defc = int(0)
win = int(0)
#move after battle
mab = int(0)
#pokemon
power1n = 'Normal'
power2n = ''
power3n = ''
power4n = ''
power5n = ''
power6n = ''
p1n = 'Digisaurus'
p2n = ''
p3n = ''
p4n = ''
p5n = ''
p6n = ''
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
pokemon1 = [1,1,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
pokemon2 = [0,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2, p2n,power2n]
pokemon3 = [0,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3, p3n,power3n]
pokemon4 = [0,0,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4, p4n,power4n]
pokemon5 = [0,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5, p5n,power5n]
pokemon6 = [0,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6, p6n,power6n]
totalife = 1
totactiv = 1
averohp = (h1n + h2n + h3n + h4n + h5n + h6n)/6
whoh = """Pokemon is a game where you battle other pokemon. You win if your opponent loses all of his/her HP(or health points.
You have a certain amount times that you can use a move (PP, or playing points)if all PP for a certain move run out, then you can't use that move.
Typically, stronger moves have smaller PP's, so it would be more fair.
Pokeballs are used to catch another pokemon. It makes that pokemon your own.
When the opponent's pokemon has lower HP, then it is easier to catch."""
credits1 = """Made by David W.(Real) Copyrights by Nintendo and Game Freak. Version 1.7(BETA)leaves BETA when all save is DONE.
Thanks to many people:

"""
credits2 ="""I appreciate that you have played this game.
Veritas Liberat!
"""
"""
*********************************************************************************
"""
##################################################
name =  input("Hello sir or ma'am! You have just fallen from the sky!What is your name?(if you remember it.)")

[name,hp,win,money,Powerup,opphp,pp1,pp2,pp3,pp4,pp5,diff,lig,blaster,blaster2,blaster3,blaster4,blaster_ammo,HPdecreaser,HPdecreaser2,HPdecreaser3,HPdecreaser4,arrow,hunger,cow,chicken,plantfood,deposit,moneybank,strdeposit,depoadd,withdraw,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6,h1n,h2n,h3n,h4n,h5n,h6n,pp1n1,pp1n2,pp1n3,pp1n4,pp1n5,pp1n6,pp2n1,pp2n2,pp2n3,pp2n4,pp2n5,pp2n6,pp3n1,pp3n2,pp3n3,pp3n4,pp3n5,pp3n6,pp4n1,pp4n2,pp4n3,pp4n4,pp4n5,pp4n6,pp5n1,pp5n2,pp5n3,pp5n4,pp5n5,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,power1n,power2n,power3n,power4n,power5n,power6n,totactiv,totalife,mypower,op,ppill] = AuxFunctions.CheckName(outputFile,name)
opower = powers[op]
mus = input("Would you like music?(y/n)")
print("Good Luck on your adventure!")
if opphp > 0:
    print("Well, a wild pokemon appeared.")
    print("It is a",nametank[op])
    print("It's type is",opower)
    print("Your battle will begin in:")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(0.45)
if lig.lower() == "l" or lig.lower() == "long":
    hp = hp + 400
    opphp = opphp + 400
    pp1 = pp1 + 5
    pp2 = pp2 + 5
    pp3 = pp3 + 10
    pp4 = pp4 + 2
elif lig.lower() == "m" or lig.lower() == "medium":
    hp = hp + 200
    opphp = opphp + 200
    pp1 = pp1 + 2
    pp2 = pp2 + 2
    pp3 = pp3 + 4
    pp4 = pp4 + 1
if mus.lower() == "y":
    player.eos_action = player.EOS_LOOP
while 1:
    if mus == "y":
        try:        
            sound = pyglet.media.load('./wild_pokemon.mp3', streaming=False)
            player.queue(sound)
            player.play()
        except WindowsError:
            print("Sorry about the audio error, at least the game didn't crash!")
    while totalife >= 1 and totactiv >= 1:
        def FixLifeBug(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6):
            if h1n > 0 and p1n != "":
                pokemon1[0] = 1
                pokemon1[8] = p1n
            if h2n > 0 and p2n != "":
                pokemon2[0] = 1
                pokemon2[8] = p2n
            if h3n > 0 and p1n != "":
                pokemon3[0] = 1
                pokemon3[8] = p3n
            if h4n > 0 and p1n != "":
                pokemon4[0] = 1
                pokemon4[8] = p4n
            if h5n > 0 and p5n != "":
                pokemon5[0] = 1
                pokemon5[8] = p5n
            if h6n > 0 and p6n != "":
                pokemon6[0] = 1
                pokemon6[8] = p6n
            return [pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6]
        aaaaa = FixLifeBug(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
        pokemon1 = aaaaa[0]
        pokemon2 = aaaaa[1]
        pokemon3 = aaaaa[2]
        pokemon4 = aaaaa[3]
        pokemon5 = aaaaa[4]
        pokemon6 = aaaaa[5]
        if hp < 0:
            totalife = 0
            totactiv = 0
        totalife = int(pokemon1[0]) + int(pokemon2[0]) + int(pokemon3[0]) + int(pokemon4[0]) + int(pokemon5[0]) + int(pokemon6[0])
        totactiv = int(pokemon1[1]) + int(pokemon2[1]) + int(pokemon3[1]) + int(pokemon4[1]) + int(pokemon5[1]) + int(pokemon6[1])
        if pokemon1[0] == 1 and pokemon1[1] == 1:
            mypower = pokemon1[len(pokemon1)-1]
            h1n = hp
            pp1n1 = pp1
            pp2n1 = pp2
            pp3n1 = pp3
            pp4n1 = pp4
            pp5n1 = pp5
            pokemon1 = [1,1,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]            
            if h1n <= 0:
                pokemon1[0] = 0
                pokemon1[1] = 0
                totalife = pokemon1[0] + pokemon2[0] + pokemon3[0] + pokemon4[0] + pokemon5[0] + pokemon6[0]
                totactiv = pokemon1[1] + pokemon2[1] + pokemon3[1] + pokemon4[1] + pokemon5[1] + pokemon6[1]
        elif pokemon2[0] == 1 and pokemon2[1] == 1:
            mypower = power2n
            h2n = hp
            pp1n2 = pp1
            pp2n2 = pp2
            pp3n2 = pp3
            pp4n2 = pp4
            pp5n2 = pp5
            pokemon2 = [1,1,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2, p2n,power2n]
            if h2n <= 0:
                pokemon2[0] = 0
                pokemon2[1] = 0
                totalife = pokemon1[0] + pokemon2[0] + pokemon3[0] + pokemon4[0] + pokemon5[0] + pokemon6[0]
        elif pokemon3[0] == 1 and pokemon3[1] == 1:
            mypower = power3n
            h3n = hp
            pp1n3 = pp1
            pp2n3 = pp2
            pp3n3 = pp3
            pp4n3 = pp4
            pp5n3 = pp5
            pokemon3 = [1,1,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3, p3n,power3n]
            if h3n <= 0:
                pokemon3[0] = 0
                pokemon3[1] = 0
                totalife = pokemon1[0] + pokemon2[0] + pokemon3[0] + pokemon4[0] + pokemon5[0] + pokemon6[0]
                totactiv = pokemon1[1] + pokemon2[1] + pokemon3[1] + pokemon4[1] + pokemon5[1] + pokemon6[1]
        elif pokemon4[0] == 1 and pokemon4[1] == 1:
            mypower = power4n
            h4n = hp
            pp1n4 = pp1
            pp2n4 = pp2
            pp3n4 = pp3
            pp4n4 = pp4
            pp5n4 = pp5
            pokemon4 = [1,1,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4, p4n,power4n]
            if h4n <= 0:
                pokemon4[0] = 0
                pokemon4[1] = 0
                totalife = pokemon1[0] + pokemon2[0] + pokemon3[0] + pokemon4[0] + pokemon5[0] + pokemon6[0]
                totactiv = pokemon1[1] + pokemon2[1] + pokemon3[1] + pokemon4[1] + pokemon5[1] + pokemon6[1]
        elif pokemon5[0] == 1 and pokemon5[1] == 1:
            mypower = power5n
            h5n = hp
            pp1n5 = pp1
            pp2n5 = pp2
            pp3n5 = pp3
            pp4n5 = pp4
            pp5n5 = pp5
            pokemon5 = [1,1,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5, p5n,power5n]
            if h5n <= 0:
                pokemon5[0] = 0
                pokemon5[1] = 0
                totalife = pokemon1[0] + pokemon2[0] + pokemon3[0] + pokemon4[0] + pokemon5[0] + pokemon6[0]
                totactiv = pokemon1[1] + pokemon2[1] + pokemon3[1] + pokemon4[1] + pokemon5[1] + pokemon6[1]
        elif pokemon6[0] == 1 and pokemon6[1] == 1:
            mypower = power6n
            h6n = hp
            pp1n6 = pp1
            pp2n6 = pp2
            pp3n6 = pp3
            pp4n6 = pp4
            pp5n6 = pp5
            pokemon6 = [1,1,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6, p6n,power6n]
            if h6n <= 0:
                pokemon6[0] = 0
                pokemon6[1] = 0
                totalife = pokemon1[0] + pokemon2[0] + pokemon3[0] + pokemon4[0] + pokemon5[0] + pokemon6[0]
                totactiv = pokemon1[1] + pokemon2[1] + pokemon3[1] + pokemon4[1] + pokemon5[1] + pokemon6[1]
        def discheck(diswho):
            if diswho == 1:
                if pokemon1[0] == 1:
                    return True
                else:
                    return False
            elif diswho == 2:
                if pokemon2[0] == 1:
                    return True
                else:
                    return False
            elif diswho == 3:
                if pokemon3[0] == 1:
                    return True
                else:
                    return False
            elif diswho == 4:
                if pokemon4[0] == 1:
                    return True
                else:
                    return False
            elif diswho == 5:
                if pokemon5[0] == 1:
                    return True
                else:
                    return False
            elif diswho == 6:
                if pokemon6[0] == 1:
                    return True
                else:
                    return False
            else:
                return False
        damage = random.randint(0,20)
        fullpo = random.randint(100,150)
        pokeball = random.randint(1,10)
        pokeball1 = random.randint(1,5)
        pokeball2 = random.randint(1,20)
        pokeball3 = random.randint(1,2)
        standard = random.randint(1,100)
        thiefr = random.randint(1,10)
        rstone = random.randint(5,15)
        rrock = random.randint(10,20)
        rbould = random.randint(20,30)
        rblaster = random.randint(50,110)
        rblaster2 = random.randint(65,125)
        rblaster3 = random.randint(80,140)
        rblaster4 = random.randint(95,165)
        rHPdecreaser = random.randint(30,90)
        rHPdecreaser2 = random.randint(45,105)
        rHPdecreaser3 = random.randint(60,120)
        rHPdecreaser4 = random.randint(75,135)
        
        def criticalb(damage):
            if damage >= 15:
                print("That was a critical hit to you.")
            else:
                return False
        def Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6):
            AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3, pokemon4,pokemon5,pokemon6)
            if AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3, pokemon4,pokemon5,pokemon6) == 1:
                h1n = opphp
                pp1n1 = 5
                pp2n1 = 10
                pp3n1 = 20
                pp4n1 = 2
                pp5n1 = 10
                p1n = nametank[op]
                power1n = opower
                pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
            elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3, pokemon4,pokemon5,pokemon6) == 2:
                h2n = opphp
                pp1n2 = 5
                pp2n2 = 10
                pp3n2 = 20
                pp4n2 = 2
                pp5n2 = 10
                p2n = nametank[op]
                power2n = opower
                pokemon2 = [1,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
            elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3, pokemon4,pokemon5,pokemon6) == 3:
                h3n = opphp
                pp1n3 = 5
                pp2n3 = 10
                pp3n3 = 20
                pp4n3 = 2
                pp5n3 = 10
                p3n = nametank[op]
                power3n = opower
                pokemon3 = [1,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n]
            elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3, pokemon4,pokemon5,pokemon6) == 4:
                h4n = opphp
                pp1n4 = 5
                pp2n4 = 10
                pp3n4 = 20
                pp4n4 = 2
                pp5n4 = 10
                p4n = nametank[op]
                power4n = opower
                pokemon4 = [1,0,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n]
            elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3, pokemon4,pokemon5,pokemon6) == 5:
                h5n = opphp
                pp1n5 = 5
                pp2n5 = 10
                pp3n5 = 20
                pp4n5 = 2
                pp5n5 = 10
                p5n = nametank[op]
                power5n = opower
                pokemon5 = [1,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
            elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3, pokemon4,pokemon5,pokemon6) == 6:
                h6n = opphp
                pp1n6 = 5
                pp2n6 = 10
                pp3n6 = 20
                pp4n6 = 2
                pp5n6 = 10
                p6n = nametank[op]
                power6n = opower
                pokemon6 = [1,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
            else:
                print("Glitch, serious glitch, please revise glitch.")
            return [1,h1n, h2n,h3n,h4n,h5n,h6n,opphp, pp1n1, pp2n1,pp3n1,pp4n1,pp5n1, pp1n2, pp2n2,pp3n2,pp4n2,pp5n2, pp1n3, pp2n3,pp3n3,pp4n3,pp5n3, pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5, pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6,p1n,p2n,p3n,p4n,p5n,p6n,power1n,power2n,power3n,power4n,power5n,power6n]
        def thief():
            if thiefr >= 5:
                return True
            else:
                return False
        class Pokeball(object):
            def __init__(self,opphp,standard,pokeball,pokeball1,pokeball2,pokeball3):
                self.opphp = opphp
                self.standard = standard
                self.pokeball = pokeball
                self.pokeball1 = pokeball1
                self.pokeball2 = pokeball2
                self.pokeball3 = pokeball3
            def ultrarl(self):
                if self.opphp < 10:
                    if self.standard >= 20:
                        return True
                    else:
                        return False
            def ultral(self):
                if self.opphp >= 10 and self.opphp < 20:
                    if self.standard >= 30:
                        return True
                    else:
                        return False
            def ultraml(self):
                if self.opphp >= 20 and self.opphp < 30:
                    if self.standard >= 40:
                        return True
                    else:
                        return False
            def ultram(self):
                if self.opphp >= 30 and self.opphp < 40:
                    if self.standard >= 50:
                        return True
                    else:
                        return False
            def ultramm(self):
                if self.opphp >= 40 and self.opphp < 50:
                    if self.standard >= 60:
                        return True
                    else:
                        return False
            def ultrabm(self):
                if self.opphp >= 50 and self.opphp < 60:
                    if self.standard >= 65:
                        return True
                    else:
                        return False
            def ultrahbm(self):
                if self.opphp >= 60 and self.opphp < 70:
                    if self.standard >= 70:
                        return True
                    else:
                        return False
            def ultrahhm(self):
                if self.opphp >= 70 and self.opphp < 80:
                    if self.standard >= 75:
                        return True
                    else:
                        return False
            def ultrah(self):
                if self.opphp >= 80 and self.opphp < 90:
                    if self.standard >= 80:
                        return True
                    else:
                        return False
            def ultrahhh(self):
                if self.opphp >= 90:
                    if self.standard >= 85:
                        return True
                    else:
                        return False
            def pokeballh(self):
                if self.opphp >= 65 and self.pokeball2 == 20:
                    return True 
                else:
                    return False
            def pokeballm(self):
                if self.opphp < 65 and self.opphp >= 35 and self.pokeball >= 1:
                    return True
                else:
                    return False
            def pokeballs(self):
                if self.opphp < 35 and self.opphp >= 10 and self.pokeball1 == 1:
                    return True
                else:
                    return False
            def pokeballes(self):
                if self.opphp < 10 and self.opphp > 0 and self.pokeball3 == 1:
                    return True
                else:
                    return False
        moveffect = Pokeball(opphp,standard,pokeball,pokeball1,pokeball2,pokeball3)
        def rampage(soup):
            if soup == 5 and pp4 > 0:
                return True
            return False
        
        ######################
        damage = damage - defc
        ######################
        if diff.lower() == "easy" or diff.lower() == "e":
            if damage >=5:
                damage = round(damage * (1 + (win/10)))-5
            else:
                damage = round(damage * (1 + (win/10)))
        elif diff.lower() == "h" or diff.lower() == "hard":
            damage = round(damage * (1.5 + (win/10)))
        elif diff.lower() == "ex" or diff.lower() == "expert":
            damage = round(damage * (1.75 + (win/10)))
        elif diff.lower() == "extreme expert" or diff.lower() == "ee":
            damage = round(damage * (2 + (win/10)))
        else:
            damage = round(damage * (1.1 + (win/10)))          

        
        if opphp > 0 and totalife > 0 and totactiv > 0:
            print("Here are your choices:\n")
            print("\t\tCredits- view credits")
            print("\t\tHelp - Clear up any confusion")
            print("\t\tInventory- use your belongings")
            print("\t\tPokeball - If you want to catch a pokemon")
            print("\t\tAttack- Attack your opponent")
            print("\t\tSummary - Summarizes your current state")
            print("\t\tHint - Provides a basic hint at what to do")
            print("\t\tCheck - Check your pokemon and their stats")
            print("\t\tSout(stands for Switch Out), where you can switch out your pokemon.")
            print("\t\tDiscard, where you can let your pokemon go. You get a small pay for them.")
            print("\t\tSave - Saves your information, so you can continue later")
            print("\t\tRun - Flee the battlefield.")
            origc = input("What do you choose?")
            if origc.lower() == "credits" or origc.lower() == "c":
                print("Pocket Monster Python Game Credits:")
                time.sleep(1)
                print("Created by Satoshi Tajiri in 1996")
                time.sleep(1)
                print("This is the second-most successful video game in the world, behind Mario.")
                time.sleep(1.4)
                print("This game is developed by Game Freak.")
                time.sleep(1)
                print("Made by David W, I didn't invent pokemon, but did make it better.")
            elif origc.lower() == "check":
                checkc = input("Check what?(Your pokemon(yp), your opponent(o), or powers/types and how effective they are(t or p)")
                if checkc.lower() == "yp":
                    print("Quick Explanation: For Active and Alive: 1 = True, 0 = False")
                    print("%-10s%-10s%-5s%-5s%-5s%-5s%-5s%-5s%-16s%-5s"% ("Alive","Active","HP","PP1","PP2","PP3","PP4","PP5","Name","Type"))
                    print("")
                    print("%-10d%-10d%-5d%-5d%-5d%-5d%-5d%-5d%-16s%-10s"% (pokemon1[0],pokemon1[1],h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n))
                    print("%-10d%-10d%-5d%-5d%-5d%-5d%-5d%-5d%-16s%-10s"% (pokemon2[0],pokemon2[1],h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n))
                    print("%-10d%-10d%-5d%-5d%-5d%-5d%-5d%-5d%-16s%-10s"% (pokemon3[0],pokemon3[1],h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n))
                    print("%-10d%-10d%-5d%-5d%-5d%-5d%-5d%-5d%-16s%-10s"% (pokemon4[0],pokemon4[1],h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n))
                    print("%-10d%-10d%-5d%-5d%-5d%-5d%-5d%-5d%-16s%-10s"% (pokemon5[0],pokemon5[1],h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n))
                    print("%-10d%-10d%-5d%-5d%-5d%-5d%-5d%-5d%-16s%-10s"% (pokemon6[0],pokemon6[1],h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n))
                elif checkc.lower() == "o":
                    print(opower,":Opponent's Type")
                    print(nametank[op],":Opponent's Name")
                    print(opphp)
                elif checkc.lower() == "powers" or checkc.lower() == "p" or checkc.lower() == "t":
                    AuxFunctions.PowerInfo()
            elif origc.lower() == "discard":
                diswho = int(input("Discard which one (1- 6)?"))
                if discheck(diswho):###
                    if diswho == 1:
                        pokemon1[0] = 0
                        if pokemon1[1] == 1:
                            pp1 = 5
                            pp2 = 10 
                            pp3 = 20
                            pp4 = 2
                            pp5 = 10
                            hp = 100
                        pokemon1[1] = 0
                        h1n = 100
                        pp1n1 = 5
                        pp2n1 = 10
                        pp3n1 = 20
                        pp4n1 = 2
                        pp5n1 = 20
                        p1n = ''
                        power1n = ''
                        money += 50
                    elif diswho == 2:
                        pokemon2[0] = 0
                        if pokemon2[1] == 1:
                            pp1 = 5
                            pp2 = 10 
                            pp3 = 20
                            pp4 = 2
                            pp5 = 10
                            hp = 100
                        pokemon2[1] = 0
                        h2n = 100
                        pp1n2 = 5
                        pp2n2 = 10
                        pp3n2 = 20
                        pp4n2 = 2
                        pp5n2 = 20
                        p2n = ''
                        power2n = ''
                        money += 50
                    elif diswho == 3:
                        pokemon3[0] = 0
                        if pokemon3[1] == 1:
                            pp1 = 5
                            pp2 = 10 
                            pp3 = 20
                            pp4 = 2
                            pp5 = 10
                            hp = 100
                        pokemon3[1] = 0
                        h3n = 100
                        pp1n3 = 5
                        pp2n3 = 10
                        pp3n3 = 20
                        pp4n3 = 2
                        pp5n3 = 20
                        p3n = ''
                        power3n = ''
                        money += 50
                    elif diswho == 4:
                        pokemon4[0] = 0
                        if pokemon4[1] == 1:
                            pp1 = 5
                            pp2 = 10 
                            pp3 = 20
                            pp4 = 2
                            pp5 = 10
                            hp = 100
                        pokemon4[1] = 0
                        h4n = 100
                        pp1n4 = 5
                        pp2n4 = 10
                        pp3n4 = 20
                        pp4n4 = 2
                        pp5n4 = 20
                        p4n = ''
                        power4n = ''
                        money += 50
                    elif diswho == 5:
                        pokemon5[0] = 0
                        if pokemon5[1] == 1:
                            pp1 = 5
                            pp2 = 10 
                            pp3 = 20
                            pp4 = 2
                            pp5 = 10
                            hp = 100
                        pokemon5[1] = 0
                        h5n = 100
                        pp1n5 = 5
                        pp2n5 = 10
                        pp3n5 = 20
                        pp4n5 = 2
                        pp5n5 = 20
                        p5n = ''
                        power5n = ''
                        money += 50
                    elif diswho == 6:
                        pokemon6[0] = 0
                        if pokemon6[1] == 1:
                            pp1 = 5
                            pp2 = 10 
                            pp3 = 20
                            pp4 = 2
                            pp5 = 10
                            hp = 100
                        pokemon6[1] = 0
                        h6n = 100
                        pp1n6 = 5
                        pp2n6 = 10
                        pp3n6 = 20
                        pp4n6 = 2
                        pp5n6 = 20
                        p6n = ''
                        power6n = ''
                        money += 50
            
                            
            elif origc.lower() == "sout":
                try:
                    so = int(input("Switch out who(1-6)?"))
                except ValueError:
                    print("Careful...")
                try:
                    to = int(input("And to whom?(1-6)"))
                except ValueError:
                    print("Careful...")
                    time.sleep(1)
                if so == 1:
                    if pokemon1[0] == 1 and pokemon1[1] == 1:
                        if to == 2:
                            if pokemon2[0] == 1 and pokemon2[1] == 0:
                               pokemon2 = [1,1,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                               print("Okay?")
                               h1n = hp
                               pp1n1 = pp1
                               pp2n1 = pp2
                               pp3n1 = pp3
                               pp4n1 = pp4
                               pp5n1 = pp5
                               mypower = power2n
                               pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                               hp = h2n
                               pp1 = pp1n2
                               pp2 = pp2n2
                               pp3 = pp3n2
                               pp4 = pp4n2
                               pp5 = pp5n2
                               print("Okay")
                               print(pokemon2)
                        elif to == 3:
                            if pokemon3[0] == 1 and pokemon2[1] == 0:
                               pokemon3 = [1,1,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n]
                               print("Okay?")
                               h1n = hp
                               pp1n1 = pp1
                               pp2n1 = pp2
                               pp3n1 = pp3
                               pp4n1 = pp4
                               pp5n1 = pp5
                               mypower = power3n
                               pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                               hp = h3n
                               pp1 = pp1n3
                               pp2 = pp2n3
                               pp3 = pp3n3
                               pp4 = pp4n3
                               pp5 = pp5n3
                               print("Okay")
                               print(pokemon3)
                        elif to == 4:
                            if pokemon4[0] == 1 and pokemon4[1] == 0:
                               pokemon4 = [1,1,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n]
                               print("Okay?")
                               h1n = hp
                               pp1n1 = pp1
                               pp2n1 = pp2
                               pp3n1 = pp3
                               pp4n1 = pp4
                               pp5n1 = pp5
                               mypower = power4n
                               pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                               hp = h4n
                               pp1 = pp1n4
                               pp2 = pp2n4
                               pp3 = pp3n4
                               pp4 = pp4n4
                               pp5 = pp5n4
                               print("Okay")
                               print(pokemon4)
                        elif to == 5:
                            if pokemon5[0] == 1 and pokemon5[1] == 0:
                               pokemon5 = [1,1,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                               print("Okay?")
                               h1n = hp
                               pp1n1 = pp1
                               pp2n1 = pp2
                               pp3n1 = pp3
                               pp4n1 = pp4
                               pp5n1 = pp5
                               mypower = power5n
                               pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                               hp = h5n
                               pp1 = pp1n5
                               pp2 = pp2n5
                               pp3 = pp3n5
                               pp4 = pp4n5
                               pp5 = pp5n5
                               print("Okay")
                               print(pokemon5)
                        elif to == 6:
                           if pokemon6[0] == 1 and pokemon6[1] == 0:
                               pokemon6 = [1,1,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                               print("Okay?")
                               h1n = hp
                               pp1n1 = pp1
                               pp2n1 = pp2
                               pp3n1 = pp3
                               pp4n1 = pp4
                               pp5n1 = pp5
                               mypower = power6n
                               pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                               hp = h6n
                               pp1 = pp1n6
                               pp2 = pp2n6
                               pp3 = pp3n6
                               pp4 = pp4n6
                               pp5 = pp5n6
                               print("Okay")
                               print(pokemon6)
                        else:
                            print("")
                    else:
                        print("Not in your inventory")
                elif so == 2:
                    if pokemon2[0] == 1 and pokemon2[1] == 1:
                        if to == 1:
                            if pokemon1[0] == 1 and pokemon1[1] == 0:
                               pokemon1 = [1,1,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                               print("Okay?")
                               h2n = hp
                               pp1n2 = pp1
                               pp2n2 = pp2
                               pp3n2 = pp3
                               pp4n2 = pp4
                               pp5n2 = pp5
                               mypower = power1n
                               pokemon2 = [1,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                               hp = h1n
                               pp1 = pp1n1
                               pp2 = pp2n1
                               pp3 = pp3n1
                               pp4 = pp4n1
                               pp5 = pp5n1
                               print("Okay")
                               print(pokemon1)
                        elif to == 3:
                            if pokemon3[0] == 1 and pokemon3[1] == 0:
                               pokemon3 = [1,1,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n]
                               print("Okay?")
                               h2n = hp
                               pp1n2 = pp1
                               pp2n2 = pp2
                               pp3n2 = pp3
                               pp4n2 = pp4
                               pp5n2 = pp5
                               mypower = power3n
                               pokemon2 = [1,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                               hp = h3n
                               pp1 = pp1n3
                               pp2 = pp2n3
                               pp3 = pp3n3
                               pp4 = pp4n3
                               pp5 = pp5n3
                               print("Okay")
                               print(pokemon3)
                        elif to == 4:
                            if pokemon4[0] == 1 and pokemon4[1] == 0:
                               pokemon4 = [1,1,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n]
                               print("Okay?")
                               h2n = hp
                               pp1n2 = pp1
                               pp2n2 = pp2
                               pp3n2 = pp3
                               pp4n2 = pp4
                               pp5n2 = pp5
                               mypower = power4n
                               pokemon2 = [1,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                               hp = h4n
                               pp1 = pp1n4
                               pp2 = pp2n4
                               pp3 = pp3n4
                               pp4 = pp4n4
                               pp5 = pp5n4
                               print("Okay")
                               print(pokemon4)
                        elif to == 5:
                            if pokemon5[0] == 1 and pokemon5[1] == 0:
                               pokemon5 = [1,1,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                               print("Okay?")
                               h2n = hp
                               pp1n2 = pp1
                               pp2n2 = pp2
                               pp3n2 = pp3
                               pp4n2 = pp4
                               pp5n2 = pp5
                               mypower = power5n
                               pokemon2 = [1,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                               hp = h5n
                               pp1 = pp1n5
                               pp2 = pp2n5
                               pp3 = pp3n5
                               pp4 = pp4n5
                               pp5 = pp5n5
                               print("Okay")
                               print(pokemon5)
                        elif to == 6:
                           if pokemon6[0] == 1 and pokemon6[1] == 0:
                               pokemon6 = [1,1,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                               print("Okay?")
                               h2n = hp
                               pp1n2 = pp1
                               pp2n2 = pp2
                               pp3n2 = pp3
                               pp4n2 = pp4
                               pp5n2 = pp5
                               mypower = power6n
                               pokemon2 = [1,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                               hp = h6n
                               pp1 = pp1n6
                               pp2 = pp2n6
                               pp3 = pp3n6
                               pp4 = pp4n6
                               pp5 = pp5n6
                               print("Okay")
                               print(pokemon6)
                        else:
                            print("You have a max of 6 pokemon")
                       
                    else:
                        print("Not in your inventory")
                elif so == 3:
                    if pokemon3[0] == 1 and pokemon3[1] == 1:
                        if to == 1:
                            if pokemon1[0] == 1 and pokemon1[1] == 0:
                               pokemon1 = [1,1,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                               print("Okay?")
                               h3n = hp
                               pp1n3 = pp1
                               pp2n3 = pp2
                               pp3n3 = pp3
                               pp4n3 = pp4
                               pp5n3 = pp5
                               pokemon3 = [1,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n]
                               hp = h1n
                               pp1 = pp1n1
                               pp2 = pp2n1
                               pp3 = pp3n1
                               pp4 = pp4n1
                               pp5 = pp5n1
                               print("Okay")
                               print(pokemon1)
                        elif to == 2:
                            if pokemon2[0] == 1 and pokemon2[1] == 0:
                               pokemon2 = [1,1,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                               print("Okay?")
                               h3n = hp
                               pp1n3 = pp1
                               pp2n3 = pp2
                               pp3n3 = pp3
                               pp4n3 = pp4
                               pp5n3 = pp5
                               pokemon3 = [1,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n]
                               hp = h2n
                               pp1 = pp1n2
                               pp2 = pp2n2
                               pp3 = pp3n2
                               pp4 = pp4n2
                               pp5 = pp5n2
                               print("Okay")
                               print(pokemon2)
                        elif to == 4:
                            if pokemon4[0] == 1 and pokemon4[1] == 0:
                               pokemon4 =[1,1,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n]
                               print("Okay?")
                               h3n = hp
                               pp1n3 = pp1
                               pp2n3 = pp2
                               pp3n3 = pp3
                               pp4n3 = pp4
                               pp5n3 = pp5
                               pokemon3 = [1,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n]
                               hp = h4n
                               pp1 = pp1n4
                               pp2 = pp2n4
                               pp3 = pp3n4
                               pp4 = pp4n4
                               pp5 = pp5n4
                               print("Okay")
                               print(pokemon4)
                        elif to == 5:
                            if pokemon5[0] == 1 and pokemon5[1] == 0:
                               pokemon5 = [1,1,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                               print("Okay?")
                               h3n = hp
                               pp1n3 = pp1
                               pp2n3 = pp2
                               pp3n3 = pp3
                               pp4n3 = pp4
                               pp5n3 = pp5
                               pokemon3 = [1,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n]
                               hp = h5n
                               pp1 = pp1n5
                               pp2 = pp2n5
                               pp3 = pp3n5
                               pp4 = pp4n5
                               pp5 = pp5n5
                               print("Okay")
                               print(pokemon5)
                        elif to == 6:
                           if pokemon6[0] == 1 and pokemon6[1] == 0:
                               pokemon6 = [1,1,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                               print("Okay?")
                               h3n = hp
                               pp1n3 = pp1
                               pp2n3 = pp2
                               pp3n3 = pp3
                               pp4n3 = pp4
                               pp5n3 = pp5
                               pokemon3 = [1,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n]
                               hp = h6n
                               pp1 = pp1n6
                               pp2 = pp2n6
                               pp3 = pp3n6
                               pp4 = pp4n6
                               pp5 = pp5n6
                               print("Okay")
                               print(pokemon6)
                        else:
                            print("You have a max of 6 pokemon")
                       
                    else:
                        print("Not in your inventory")
                elif so == 4:
                    if pokemon4[0] == 1 and pokemon4[1] == 1:
                        if to == 1:
                            if pokemon1[0] == 1 and pokemon1[1] == 0:
                               pokemon1 = [1,1,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                               print("Okay?")
                               h4n = hp
                               pp1n4 = pp1
                               pp2n4 = pp2
                               pp3n4 = pp3
                               pp4n4 = pp4
                               pp5n4 = pp5
                               pokemon4 = [1,0,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n]
                               hp = h1n
                               pp1 = pp1n1
                               pp2 = pp2n1
                               pp3 = pp3n1
                               pp4 = pp4n1
                               pp5 = pp5n1
                               print("Okay")
                               print(pokemon1)
                        elif to == 2:
                            if pokemon2[0] == 1 and pokemon2[1] == 0:
                               pokemon2 = [1,1,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                               print("Okay?")
                               h4n = hp
                               pp1n4 = pp1
                               pp2n4 = pp2
                               pp3n4 = pp3
                               pp4n4 = pp4
                               pp5n4 = pp5
                               pokemon4 = [1,0,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n]
                               hp = h2n
                               pp1 = pp1n2
                               pp2 = pp2n2
                               pp3 = pp3n2
                               pp4 = pp4n2
                               pp5 = pp5n2
                               print("Okay")
                               print(pokemon2)
                        elif to == 3:
                            if pokemon3[0] == 1 and pokemon3[1] == 0:
                               pokemon3 = [1,1,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n]
                               print("Okay?")
                               h4n = hp
                               pp1n4 = pp1
                               pp2n4 = pp2
                               pp3n4 = pp3
                               pp4n4 = pp4
                               pp5n4 = pp5
                               pokemon4 = [1,0,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n]
                               hp = h3n
                               pp1 = pp1n3
                               pp2 = pp2n3
                               pp3 = pp3n3
                               pp4 = pp4n3
                               pp5 = pp5n3
                               print("Okay")
                               print(pokemon3)
                        elif to == 5:
                            if pokemon5[0] == 1 and pokemon5[1] == 0:
                               pokemon5 = [1,1,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                               print("Okay?")
                               h4n = hp
                               pp1n4 = pp1
                               pp2n4 = pp2
                               pp3n4 = pp3
                               pp4n4 = pp4
                               pp5n4 = pp5
                               pokemon4 = [1,0,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n]
                               hp = h5n
                               pp1 = pp1n5
                               pp2 = pp2n5
                               pp3 = pp3n5
                               pp4 = pp4n5
                               pp5 = pp5n5
                               print("Okay")
                               print(pokemon5)
                        elif to == 6:
                           if pokemon6[0] == 1 and pokemon6[1] == 0:
                               pokemon6 = [1,1,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                               print("Okay?")
                               h4n = hp
                               pp1n4 = pp1
                               pp2n4 = pp2
                               pp3n4 = pp3
                               pp4n4 = pp4
                               pp5n4 = pp5
                               pokemon4 = [1,0,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n]
                               hp = h6n
                               pp1 = pp1n6
                               pp2 = pp2n6
                               pp3 = pp3n6
                               pp4 = pp4n6
                               pp5 = pp5n6
                               print("Okay")
                               print(pokemon6)
                        else:
                            print("You have a max of 6 pokemon")
                       
                    else:
                        print("Not in your inventory")
                elif so == 5:
                    if pokemon5[0] == 1 and pokemon5[1] == 1:
                        if to == 1:
                            if pokemon1[0] == 1 and pokemon1[1] == 0:
                               pokemon1 = [1,1,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                               print("Okay?")
                               h5n = hp
                               pp1n5 = pp1
                               pp2n5 = pp2
                               pp3n5 = pp3
                               pp4n5 = pp4
                               pp5n5 = pp5
                               pokemon5 = [1,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                               hp = h1n
                               pp1 = pp1n1
                               pp2 = pp2n1
                               pp3 = pp3n1
                               pp4 = pp4n1
                               pp5 = pp5n1
                               print("Okay")
                               print(pokemon1)
                        elif to == 2:
                            if pokemon2[0] == 1 and pokemon2[1] == 0:
                               pokemon2 = [1,1,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                               print("Okay?")
                               h5n = hp
                               pp1n5 = pp1
                               pp2n5 = pp2
                               pp3n5 = pp3
                               pp4n5 = pp4criticalb
                               pp5n5 = pp5
                               pokemon5 = [1,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                               hp = h2n
                               pp1 = pp1n2
                               pp2 = pp2n2
                               pp3 = pp3n2
                               pp4 = pp4n2
                               pp5 = pp5n2
                               print("Okay")
                               print(pokemon2)
                        elif to == 3:
                            if pokemon3[0] == 1 and pokemon3[1] == 0:
                               pokemon3 = [1,1,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n]
                               print("Okay?")
                               h5n = hp
                               pp1n5 = pp1
                               pp2n5 = pp2
                               pp3n5 = pp3
                               pp4n5 = pp4
                               pp5n5 = pp5
                               pokemon5 = [1,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                               hp = h3n
                               pp1 = pp1n3
                               pp2 = pp2n3
                               pp3 = pp3n3
                               pp4 = pp4n3
                               pp5 = pp5n3
                               print("Okay")
                               print(pokemon3)
                        elif to == 4:
                            if pokemon4[0] == 1 and pokemon4[1] == 0:
                               pokemon4 = [1,1,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n]
                               print("Okay?")
                               h5n = hp
                               pp1n5 = pp1
                               pp2n5 = pp2
                               pp3n5 = pp3
                               pp4n5 = pp4
                               pp5n5 = pp5
                               pokemon5 = [1,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                               hp = h4n
                               pp1 = pp1n4
                               pp2 = pp2n4
                               pp3 = pp3n4
                               pp4 = pp4n4
                               pp5 = pp5n4
                               print("Okay")
                               print(pokemon4)
                        elif to == 6:
                           if pokemon6[0] == 1 and pokemon6[1] == 0:
                               pokemon6 = [1,1,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                               print("Okay?")
                               h5n = hp
                               pp1n5 = pp1
                               pp2n5 = pp2
                               pp3n5 = pp3
                               pp4n5 = pp4
                               pp5n5 = pp5
                               pokemon5 = [1,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                               hp = h6n
                               pp1 = pp1n6
                               pp2 = pp2n6
                               pp3 = pp3n6
                               pp4 = pp4n6
                               pp5 = pp5n6
                               print("Okay")
                               print(pokemon6)
                        else:
                            print("You have a max of 6 pokemon")
                       
                    else:
                        print("Not in your inventory")
                elif so == 6:
                    if pokemon6[0] == 1 and pokemon6[1] == 1:
                        if to == 1:
                            if pokemon1[0] == 1 and pokemon1[1] == 0:
                               pokemon1 = [1,1,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                               print("Okay?")
                               h6n = hp
                               pp1n6 = pp1
                               pp2n6 = pp2
                               pp3n6 = pp3
                               pp4n6 = pp4
                               pp5n6 = pp5
                               pokemon6 = [1,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                               hp = h1n
                               pp1 = pp1n1
                               pp2 = pp2n1
                               pp3 = pp3n1
                               pp4 = pp4n1
                               pp5 = pp5n1
                               print("Okay")
                               print(pokemon1)
                        elif to == 2:
                            if pokemon2[0] == 1 and pokemon2[1] == 0:
                               pokemon2 = [1,1,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                               print("Okay?")
                               h6n = hp
                               pp1n6 = pp1
                               pp2n6 = pp2
                               pp3n6 = pp3
                               pp4n6 = pp4
                               pp5n6 = pp5
                               pokemon6 = [1,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                               hp = h2n
                               pp1 = pp1n2
                               pp2 = pp2n2
                               pp3 = pp3n2
                               pp4 = pp4n2
                               pp5 = pp5n2
                               print("Okay")
                               print(pokemon2)
                        elif to == 3:
                            if pokemon3[0] == 1 and pokemon3[1] == 0:
                               pokemon3 = [1,1,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n]
                               print("Okay?")
                               h6n = hp
                               pp1n6 = pp1
                               pp2n6 = pp2
                               pp3n6 = pp3
                               pp4n6 = pp4
                               pp5n6 = pp5
                               pokemon6 = [1,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                               hp = h3n
                               pp1 = pp1n3
                               pp2 = pp2n3
                               pp3 = pp3n3
                               pp4 = pp4n3
                               pp5 = pp5n3
                               print("Okay")
                               print(pokemon3)
                        elif to == 4:
                            if pokemon4[0] == 1 and pokemon4[1] == 0:
                               pokemon4 = [1,1,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n]
                               print("Okay?")
                               h6n = hp
                               pp1n6 = pp1
                               pp2n6 = pp2
                               pp3n6 = pp3
                               pp4n6 = pp4
                               pp5n6 = pp5
                               pokemon6 = [1,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                               hp = h4n
                               pp1 = pp1n4
                               pp2 = pp2n4
                               pp3 = pp3n4
                               pp4 = pp4n4
                               pp5 = pp5n4
                               print("Okay")
                               print(pokemon4)
                        elif to == 5:
                           if pokemon5[0] == 1 and pokemon5[1] == 0:
                               pokemon5 = [1,1,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                               print("Okay?")
                               h6n = hp
                               pp1n6 = pp1
                               pp2n6 = pp2
                               pp3n6 = pp3
                               pp4n6 = pp4
                               pp5n6 = pp5
                               pokemon6 = [1,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                               hp = h5n
                               pp1 = pp1n5
                               pp2 = pp2n5
                               pp3 = pp3n5
                               pp4 = pp4n5
                               pp5 = pp5n5
                               print("Okay")
                               print(pokemon5)
                        else:
                            print("You have a max of 6 pokemon")
                       
                    else:
                        print("Not in your inventory")
            elif origc.lower() == "save" or origc.lower() == "sq":
                AuxFunctions.SaveGame(outputFile,name,hp,win,money,Powerup,opphp,pp1,pp2,pp3,pp4,pp5,diff,lig,blaster,blaster2,blaster3,blaster4,blaster_ammo,HPdecreaser,HPdecreaser2,HPdecreaser3,HPdecreaser4,arrow,hunger,cow,chicken,plantfood,deposit,moneybank,strdeposit,depoadd,withdraw,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6,h1n,h2n,h3n,h4n,h5n,h6n,pp1n1,pp1n2,pp1n3,pp1n4,pp1n5,pp1n6,pp2n1,pp2n2,pp2n3,pp2n4,pp2n5,pp2n6,pp3n1,pp3n2,pp3n3,pp3n4,pp3n5,pp3n6,pp4n1,pp4n2,pp4n3,pp4n4,pp4n5,pp4n6,pp5n1,pp5n2,pp5n3,pp5n4,pp5n5,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,power1n,power2n,power3n,power4n,power5n,power6n,totactiv,totalife,mypower,op,ppill)#another location at end
            elif origc.lower() == "attack" or origc.lower() == "a":
                result = AuxFunctions.Attack(hp,opphp,pp1,pp2,pp3,pp4,pp5,defc,win,opower,mypower,op,nametank,Powerup)
                hp = result[0]
                opphp = result[1]
                pp1 = result[2]
                pp2 = result[3]
                pp3 = result[4]
                pp4 = result[5]
                pp5 = result[6]
                defc = result[7]
                win = result[8]
            elif origc.lower() == "z":
                Attack(100, 100, 100, 100, 100, 100, 100, 100, 100)
            elif  origc.lower() == "inventory" or origc.lower() == "i" or origc.lower() == "inv":
                c = input("You opened your inventory, what will you do?(view, use)(v, or u")
                if c.lower() == "v" or c.lower() == "view":
                    print(money,"Dollars")
                    print(win,"wins")
                    print(ppill,"PP restoring pill(s).")
                    print(ppp,"potion(s).")
                    print(hppp,"hyper potion(s).")
                    print(ultrapp,"Ultra Ball(s).")
                    print(fppp,"Full Potion(s)")
                    print(frpp,"Full Restore(s)")
                    print(stone,"Stone(s)")
                    print(bould,"Boulder(s)")
                    print(blaster,"blaster(s), although you only need 1.")#nerf
                    print(blaster_ammo,"blaster_ammo(s).")
                    print(Powerup,"Powerup(s).")#sword
                    print(HPdecreaser,"HPdecreaser(s)")#bow
                    print(arrow,"arrow(s)")
                elif c.lower() == "u" or c.lower() == "use":
                    print("Your inventory items are:")
                    print("\tPP pills")
                    print("\tPotions(Heal 10 HP)")
                    print("\tHyper Potions(Heal 50 HP)")
                    print("\tFull Potions(100- 150 HP)")
                    print("\tFull Restores(100-150 HP + all restored PP)")
                    print("\tMagic Stones(Do small damage)(just type 'stone')")
                    print("\tMagic Rocks(Do medium damage)('rock')")
                    print("\tMagic Boulders(Do big damage('boulder')")
                    print("\tBlaster(Huge Damage)")
                    print("\tNOTE! NOTE!Powerup(Not in inventory, automatically applied)NOTE! NOTE!")
                    print("\tHPdecreaser(Lots of Damage, bit less than Blaster)")
                    cd = input("Which item will you use?")
                    if cd.lower() == "potion":
                        if ppp > 0:
                            hp = hp + 10
                            ppp = ppp - 1
                            print("Now you have", ppp,"potions left.")
                            print("Your health is now:")
                            print(hp)
                            input("but not for long...")
                            hp = hp - damage
                            criticalb(damage)
                            print("Your opponents strike lost you", damage,"points")
                            print("Right now")
                            print("%-19s%-10s"% ("Player","HP"))
                            print("%-19s%-10d"% ("You", hp))
                            print("%-19s%-10d"% ("(Opp.)" + nametank[op],opphp))
                        else:
                            print("Sorry, you are clean out of potions.")
                    elif cd.lower() == "hp" or cd.lower() == "hyper potion":
                        if hppp > 0:
                            hp = hp + 50
                            hppp = hppp - 1
                            print("Now you have",hppp,"potions left.")
                            print("Your health is now:")
                            print(hp)
                            input("but not for long...")
                            hp = hp - damage
                            criticalb(damage)
                            print("Your opponents strike lost you", damage,"points")
                            print("Right now")
                            print("%-19s%-10s"% ("Player","HP"))
                            print("%-19s%-10d"% ("You", hp))
                            print("%-19s%-10d"% ("(Opp.)" + nametank[op],opphp))
                        else:
                            print("Sorry, you already used your only Hyper Potion.")
                    elif cd.lower() == "pi" or cd.lower() == "pill" or cd.lower() == "pp pill":
                        if ppill > 0:
                            ppill = ppill - 1
                            pp1 = int(5)
                            pp2 = int(10)
                            pp3 = int(20)
                            pp4 = int(5)
                            pp5 = int(10)
                            print("All your PP has been restored, even your KO move now has 5 PP!")
                        else:
                            print("0 PP pills, sorry!")
                    elif cd.lower() == "fp" or cd.lower() == "full potion":
                          if fppp > 0:
                              hp = hp + fullpo
                              print("Your health has been restored by", fullpo,"HP.")
                          else:
                              print("Sorry, no full potions.")
                    elif cd.lower() == "fr" or cd.lower() == "full restore":
                        if frpp > 0:
                            hp = hp + fullpo
                            pp1 = int(10)
                            pp2 = int(15)
                            pp3 = int(25)
                            pp4 = int(5)
                            pp5 = int(15)
                            frpp = frpp - 1
                            print("That was very beneficial to you.")
                            print("Your hp is now",hp) 
                        else:
                            print("You have no full restores, but I encourage you to buy more.")
                    elif cd.lower() == "stone" or cd.lower() == "st":
                        if stone > 0:
                            stone = stone - 1
                            opphp = opphp - rstone
                            print("Your opponent's HP is now:",opphp)
                            print("Your attack startled your opponent, and it didn't attack back.")
                            print("Your hp is",hp)
                        else:
                            print("Sorry, you have no stones, but they only cost 10 dollars for 5.")
                    elif cd.lower() == "boulder" or cd.lower() == "bo":
                        if bould > 0:
                            bould = bould - 1
                            opphp = opphp - rbould
                        else:
                            print("Sorry, you have no boulders.")
                    elif cd.lower() == "rock" or cd.lower() == "ro":
                        if rock > 0:
                            rock = rock - 1
                            opphp = opphp - rrock
                            print("Your hp:",hp)
                            print("Your opponents hp",opphp)
                        else:
                            print("Sorry, you have no rocks.")
                    elif cd.lower() == "blaster" or cd.lower() == "g":
                        if blaster_ammo > 0:
                            if blaster > 0:
                                if blaster2 > 0:
                                    if blaster3 > 0:
                                        if blaster4 > 0:
                                            print("Wow, you have a 4th level blaster.")
                                            print("You will decimate your opponent.")
                                            blaster_ammo = blaster_ammo - 1
                                            opphp = opphp - rblaster4
                                            print("Your hp:",hp)
                                            print("Your opponents hp:",opphp)
                                        else:
                                            print("You have a 3rd level blaster!")
                                            print("Thats incredible!")
                                            blaster_ammo = blaster_ammo - 1
                                            opphp = opphp - rblaster3
                                            print("Your hp:",hp)
                                            print("Your opponents hp:",opphp)
                                    else:
                                        print("Very well, the blaster, level two was used.")
                                        blaster_ammo = blaster_ammo - 1
                                        opphp = opphp - rblaster2
                                        print("Your hp:",hp)
                                        print("Your opponents hp:",opphp)
                                else:
                                    print("So, you must use your 1st level blaster. Very well...")
                                    blaster_ammo = blaster_ammo - 1
                                    opphp = opphp - rblaster
                                    print("Your hp:",hp)
                                    print("Your opponents hp:",opphp)
                            else:
                                print("Old proverb: One does not simply shoot blaster ammo if he has no blaster.")
                        else:
                            print("Old proverb: One does not simply shoot a blaster if he has no blaster ammo.")
                    elif cd.lower() == "Powerup" or cd.lower() == "pu":
                        if Powerup > 0:
                            print("Hey punk, you don't understand, your Powerup is activated on your pokemons hands/paws.")
                            print("You can't do anythin' 'bout it anymore.")
                        else:
                            print("Famous proverb: One does not cut the beef with Powerup, when no Powerup is there to cut with.")
                    elif cd.lower() == "hpdecreaser" or cd.lower() == "decreaser" or cd.lower() == "hpd":
                        if arrow > 0:
                            if HPdecreaser > 0:
                                if HPdecreaser2 > 0:
                                    if HPdecreaser3 > 0:
                                        if HPdecreaser4 > 0:
                                            print("Wow, you have a 4th level HPdecreaser.")
                                            print("You will decimate your opponent.")
                                            arrow = arrow - 1
                                            opphp = opphp - rHPdecreaser4
                                            print("Your hp:",hp)
                                            print("Your opponents hp:",opphp)
                                        else:
                                            print("You have a 3rd level HPdecreaser!")
                                            print("Thats incredible!")
                                            arrow = arrow - 1
                                            opphp = opphp - rHPdecreaser3
                                            print("Your hp:",hp)
                                            print("Your opponents hp:",opphp)
                                    else:
                                        print("Very well,")
                                        print("Officer, I'm call on behalf of",name,"for animal(...well, pokemon) abuse.")
                                        time.sleep(1)
                                        arrow = arrow - 1
                                        opphp = opphp - rHPdecreaser2
                                        print("Your hp:",hp)
                                        print("Your opponents hp:",opphp)
                                else:
                                    print("So, you must use your 1st level HPdecreaser. Very well...")
                                    arrow = arrow - 1
                                    opphp = opphp - rHPdecreaser
                                    print("Your hp:",hp)
                                    print("Your opponents hp:",opphp)
                            else:
                                print("Old proverb: One does not simply shoot arrows if he has no HPdecreaser.")
                        else:
                            print("Old proverb: One does not simply shoot a HPdecreaser if he has no arrows.")

                    else:
                        print("Invalid option.Common error:mispelling")
            elif  origc.lower() == "run" or origc.lower() == "r":
                print("Fleeing the battle field.")
                opphp = 0
                money -= (hp - opphp)
                fail = 1
            elif origc.lower() == "help" or origc.lower() == "h":
                hh = input("What do you want to know?(overview, or 'o', playing points, or 'pp', and pokeballs, or 'po')If you are not picky just press any other key!")
                if hh.lower() == "o":
                    input("Pokemon is a game where you battle other pokemon. You win if your opponent loses all of his/her HP(or health points).")
                    print("""The goal is to try to keep your pokemon alive and defeat the other pokemon.
                            Another way to win is to catch your opponent's or wild pokemon in a poke-ball or an Ultra-ball.""")
                elif hh.lower() == "pp":
                    input("You have a certain amount times that you can use a move (PP, or playing points)if all PP for a certain move run out, then you can't use that move.")
                    input("Typically, stronger moves have smaller PP's, so you wouldn't be continuously destroying your opponent.")
                elif hh.lower() == "po":
                    print("Pokeballs are used to catch another pokemon. It makes that pokemon your own.")
                    time.sleep(.5)
                    print("When the opponent's pokemon has lower HP, then it is easier to catch.")
                    time.sleep(.45)
                    print("Ultra balls have a higher chance of catching.")
                    time.sleep(.3)
                    print("If you catch a pokemon, you get its stats, even if they are low.")
                else:
                    print(whoh)#wholehelp
                print("I hope this helped!")
            elif origc.lower() == "pokeball" or origc.lower() == "po" or origc.lower() == "poke" :
                pokec = input("Ultra or regular?")
                if pokec.lower() == "u" or pokec.lower() == "ultra":
                    if ultrapp > 0:
                        ultrapp = ultrapp - 1
                        if Pokeball.ultrahhh(moveffect) == True:
                            time.sleep(2)
                            print("You captured a pokemon!")
                            print("With an Ultra Ball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        elif Pokeball.ultrah(moveffect) == True:
                            print("You captured a pokemon!")
                            print("With an Ultra Ball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        elif Pokeball.ultrahhm(moveffect) == True:
                            print("You captured a pokemon!")
                            print("With an Ultra Ball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        elif Pokeball.ultrahbm(moveffect) == True:
                            print("You captured a pokemon!")
                            print("With an Ultra Ball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        elif Pokeball.ultrabm(moveffect) == True:
                            print("You captured a pokemon!")
                            print("With an Ultra Ball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        elif Pokeball.ultramm(moveffect) == True:
                            print("You captured a pokemon!")
                            print("With an Ultra Ball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        elif Pokeball.ultram(moveffect) == True:
                            print("You captured a pokemon!")
                            print("With an Ultra Ball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        elif Pokeball.ultraml(moveffect) == True:
                            print("You captured a pokemon!")
                            print("With an Ultra Ball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        elif Pokeball.ultral(moveffect) == True:
                            print("You captured a pokemon!")
                            print("With an Ultra Ball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        elif Pokeball.ultrarl(moveffect) == True:
                            print("You captured a pokemon!")
                            print("With an Ultra Ball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        else:
                            print("Sorry, even though it was an Ultra Ball, it didn't catch the pokemon.")
                            print("You have", ultrapp,"Ultra Balls left.")
                    else:
                        print("Sorry, no Ultra Balls left.")
                elif pokec.lower() == "r" or pokec.lower() == "regular":
                    if pokepp > 0:
                        pokepp = pokepp - 1
                        if Pokeball.pokeballs(moveffect) == True: 
                            print("You captured a pokemon!")
                            print("With a regular pokeball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        elif Pokeball.pokeballm(moveffect) == True:
                            print("You captured a pokemon!")
                            print("With a regular pokeball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        elif Pokeball.pokeballh(moveffect) == True:
                            print("You captured a pokemon!")
                            print("With a regular pokeball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        elif Pokeball.pokeballes(moveffect) == True:
                            print("You captured a pokemon!")
                            print("With a regular pokeball!")
                            print("Your opponent's HP before caught:",opphp)
                            c = Pokeballinput(h1n, h2n,h3n,h4n,h5n,h6n,opphp, opower, nametank,power1n,power2n,power3n,power4n,power5n,power6n,pp1n1, pp2n1,pp3n1,pp4n1,pp5n1,pp1n2, pp2n2,pp3n2,pp4n2,pp5n2,pp1n3, pp2n3,pp3n3,pp4n3,pp5n3,pp1n4, pp2n4,pp3n4,pp4n4,pp5n4,pp1n5, pp2n5,pp3n5,pp4n5,pp5n5,pp1n6, pp2n6 ,pp3n6,pp4n6,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
                            h1n = c[1]
                            h2n = c[2]
                            h3n = c[3]
                            h4n = c[4]
                            h5n = c[5]
                            h6n = c[6]
                            opphp = c[7]
                            pp1n1 = c[8]
                            pp2n1 = c[9]
                            pp3n1 = c[10]
                            pp4n1 = c[11]
                            pp5n1 = c[12]
                            pp1n2= c[13]
                            pp2n2= c[14]
                            pp3n2= c[15]
                            pp4n2= c[16]
                            pp5n2= c[17]
                            pp1n3= c[18]
                            pp2n3= c[19]
                            pp3n3= c[20]
                            pp4n3= c[21]
                            pp5n3= c[22]
                            pp1n4= c[23]
                            pp2n4= c[24]
                            pp3n4= c[25]
                            pp4n4= c[26]
                            pp5n4= c[27]
                            pp1n5= c[28]
                            pp2n5= c[29]
                            pp3n5= c[30]
                            pp4n5= c[31]
                            pp5n5= c[32]
                            pp1n6= c[33]
                            pp2n6= c[34]
                            pp3n6= c[35]
                            pp4n6= c[36]
                            pp5n6= c[37]
                            p1n= c[44]
                            p2n= c[45]
                            p3n= c[46]
                            p4n = c[47]
                            p5n = c[48]
                            p6n= c[49]
                            power1n= c[50]
                            power2n= c[51]
                            power3n= c[52]
                            power4n= c[53]
                            power5n= c[54]
                            power6n= c[55]
                            pokemon1= c[38]
                            pokemon2= c[39]
                            pokemon3= c[40]
                            pokemon4= c[41]
                            pokemon5= c[42]
                            pokemon6= c[43]
                        else:
                            print("You now have", pokepp,"pokeballs left.")    
                            print("Your pokeball technique didn't work",name,"your opponent broke free.")
                            print("Your  HP", hp)
                            print("Your opponent's HP ",opphp)
                            
                    else:
                        print("Your amount of pokeballs is too low, it is",pokepp)
                else:
                    print("Sorry, I only understand real options.")
                
            elif origc.lower() == "hint" or origc.lower() == "ht":
                AuxFunctions.hints(hp,opphp,pp1,pp2,pp3,pp4,pp5,name)
            elif origc.lower() == "summary" or origc.lower() == "sum":
                print("Your hp:",hp)
                print("Your opponent's hp:",opphp)
                print("Your money:",money)
                print("Your wins:",win)
                print("For more stats, visit Inventory -> View")
            else:    
                print("No comprendo")
    ############################################################################################################################################################################################################################################
        elif opphp <= 0 and totalife > 0 and totactiv > 0:
            mab += 1
            if opphp < 0:
                print("You have just defeated a pokemon, you may now:")
                print("\t\tGo to the Pokemon Center (pc) - heal your pokemon")
                print("\t\tSave - saves progress")
                print("\t\tGo to the bank - store money")
                print("\t\tGo to the market- trade items")
                print("\t\tGo to the Pokemon Store - Buy items for inventory")
                print("\t\tGo to the Pokemon Adoption Center - Get a pokemon!")
                print("\t\tExit the game")
                print("\t\t or Fight again!")
                origd = input("What's your choice?")
                
            else:
                print("You now may:")
                print("\t\tGo to the Pokemon Center (pc) - heal your pokemon")
                print("\t\tSave - saves progress")
                print("\t\tGo to the bank - store money")
                print("\t\tGo to the market- trade items")
                print("\t\tGo to the Pokemon Store - Buy items for inventory")
                print("\t\tGo to the Pokemon Adoption Center - Get a pokemon!")
                print("\t\tExit the game")
                print("\t\tor Fight again!")
                origd = input("What's your choice?")
            if mab == 1:
                money = money + (hp - opphp)
                if fail != 1:
                    win = win + 1
                    deposit = round(deposit * 1.1,2)
                    moneybank = round(deposit,2)
                    strdeposit = round(deposit,2)
                    deposit = moneybank
			fail = 0
            opphp = 0
            print("Your hp:",hp)
            print("Your opponent's hp.",opphp)
            print("Your money:",money)
            if origd.lower() == "pc" or origd.lower() == "pokemon center":
                banksult = AuxFunctions.PokemonCenter(money,h1n,h2n,h3n,h4n,h5n,h6n,hp)
                money = banksult[0]
                h1n = banksult[1]
                h2n = banksult[2]
                h3n = banksult[3]
                h4n = banksult[4]
                h5n = banksult[5]
                h6n = banksult[6]
                hp = banksult[7]
                pp1n1 = 5
                pp1n2 = 5
                pp1n3 = 5
                pp1n4 = 5
                pp1n5 = 5
                pp1n6 = 5
                ##########
                pp2n1 = 10
                pp2n2 = 10
                pp2n3 = 10
                pp2n4 = 10
                pp2n5 = 10
                pp2n6 = 10
                ##########
                pp3n1 = 20
                pp3n2 = 20
                pp3n3 = 20
                pp3n4 = 20
                pp3n5 = 20
                pp3n6 = 20
                ##########
                pp4n1 = 2
                pp4n2 = 2
                pp4n3 = 2
                pp4n4 = 2
                pp4n5 = 2
                pp4n6 = 2
                ##########
                pp5n1 = 10
                pp5n2 = 10
                pp5n3 = 10
                pp5n4 = 10
                pp5n5 = 10
                pp5n6 = 10
                ######
                pp1 = 5
                pp2 = 10
                pp3 = 20
                pp4 = 2
                pp5 = 10
            elif origd.lower() == "f" or origd.lower() == "fight" or origd.lower() == "arena":
                print("Welcome to the arena, here your pokemon will be put to the test against a random wild pokemon.")
                opphp = 100
                mab = 0
                op = random.randint(1,len(powers)-3)
                opower = powers[op]
                print("It is a(n)",nametank[op])
                print("Its power is",opower)         
            elif origd.lower() == "bank" or origd.lower() == "b":
                bankch = input("Deposit, Withdraw, or View?")
                if bankch.lower() == "withdraw" or bankch.lower() == "w":
                    if moneybank >= 0:
                        print("You have this much in the bank:",moneybank)
                        withdraw = float(input("How much?"))
                        if deposit - withdraw >= 0:
                            deposit -= withdraw
                            money = money  + withdraw
                        else:
                            print("You don't have enough money in the bank.")
                    else:
                        print("You have no money in the bank.")
                elif bankch.lower() == "deposit" or bankch.lower() == "d":
                    if money > 0:
                        print("You have this much money:",money)
                        print("Our interest rate is: 10% per month(yeah, we know it's a lot)")
                        if deposit > 0:
                            try:
                                depoadd = float(input("How much would you wish to add?"))
                            except ValueError:
                                depoadd = 0
                                print("Careful... That's not possible.")
                            if money - depoadd >= 0:
                                deposit += depoadd
                                money -= depoadd
                            else:
                                print("You don't have enough money.")
                        else:
                            deposit = float(input("How much will you deposit?"))
                            if money - deposit >= 0:
                                money -= deposit
                                deposit += strdeposit
                            
                            else:
                                print("You don't have enough money.")
                                deposit = 0
                    else:
                        print("You have no money to put in the bank.")
                elif bankch.lower() == "view" or bankch.lower() == "v":
                    AuxFunctions.PrintVar(deposit,moneybank,money,ppill,ppp,hppp,fppp,frpp,stone,bould,blaster,blaster_ammo,Powerup,HPdecreaser,HPdecreaser2,HPdecreaser3,HPdecreaser4,arrow,pokepp,ultrapp)
                else:
                    print("Not a real bank option.")
            elif origd.lower() == "e" or origd.lower() == "exit":
                print("Okay, you defeated",win,"pokemon in the end.")
                input()
                hp = -1 
                opphp = 1
            elif origd.lower() == "m" or origd.lower() == "market":
                print("We have:")
                print("\tSteak, Chicken, Wheat(each costing 100 dollars)")
                print("\tFrog Legs, Monkey Tail, both 600 dollars, Mario's Hat, a rare collector's item, for 100,000 dollars.")
                print("\tAnd More Coming Soon!")
                marketc = input("What's your choice?")
                if marketc.lower() == "chicken" or marketc.lower() == "c":
                    print("Chicken is cooking.")
                    chicken += 10
                    money -= 100
                elif marketc.lower() == "steak" or marketc.lower() == "s":
                    print("Steak grilling!")
                    cow += 10
                    money -= 100
                elif marketc.lower() == "wheat":
                    print("Wait, wheat, or do you want to wait a few seconds for bread?")
                    whe = input("So, Wheat or Bread?")
                    if whe.lower() == "bread":
                        print("Okay, one second, that will cost you 25 dollars more though.")
                        time.sleep(1)
                        print("...")
                        time.sleep(1)
                        print("Fresh out of the oven bread!")
                        bread += 3
                        money -= 125
                    else:
                        print("15 Wheat coming right up.")
                        wheat += 15
                        money -= 100
            elif origd.lower() == "pac" or origd.lower() == "pokemon adoption center":
                print("Welcome")
                if money >= 500:
                    rich = input("Do you want a high-class pokemon?(5000 coins)(Type \"H\"),\nan ultra-class pokemon (10000)(Type \"U\"), \nor a god pokemon(15000)(Type \"G\")\n if not, just ignore")
                    if rich == "":
                        money -= 500
                        if AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 1:
                            x = random.randint(0,len(nametank)-3)
                            p1n = nametank[x]
                            power1n = powers[x]
                            pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 2:
                            x = random.randint(0,len(nametank)-3)
                            h2n = 113
                            p2n = nametank[x]
                            power2n = powers[x]
                            pokemon2 = [1,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 3:
                            x = random.randint(0,len(nametank)-3)
                            h3n = 115
                            p3n = nametank[x]
                            power3n = powers[x]
                            pokemon3 = [1,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n] 
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 4:
                            x = random.randint(0,len(nametank)-3)
                            p4n = nametank[x]
                            power4n = powers[x]
                            pokemon4 = [1,0,h4n,pp1n4,pp2n4,pp3n4,pp4n4,pp5n4,p4n,power4n] 
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 5:
                            x = random.randint(0,len(nametank)-3)
                            p5n = nametank[x]
                            power5n = powers[x]
                            pokemon5 = [1,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 6:
                            x = random.randint(0,len(nametank)-3)
                            p6n = nametank[x]
                            power6n = powers[x]
                            pokemon6 = [1,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                        else:
                            print("All of your pokemon are full.")
                            money += 500
                            print("Money refunded.")
                    elif rich.lower() == "h":
                        money -= 3000 #5 thousand, not a typo
                        if AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 1:
                            x = 0
                            p1n = nametank[x]
                            power1n = powers[x]
                            pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 2:
                            x = 0
                            p2n = nametank[x]
                            power2n = powers[x]
                            pokemon2 = [1,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 3:
                            x = 0
                            p1n = nametank[x]
                            power1n = powers[x]
                            pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 4:
                            x = 0
                            p3n = nametank[x]
                            power3n = powers[x]
                            pokemon3 = [1,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n] 
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 5:
                            x = 0
                            p5n = nametank[x]
                            power5n = powers[x]
                            pokemon5 = [1,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 6:
                            x = 0
                            p6n = nametank[x]
                            power6n = powers[x]
                            pokemon6 = [1,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                        else:
                            print("All your pokemon are full.")
                            money += 5000
                            print("Money refunded.")
                    elif rich.lower() == "u":
                        money -= 6000 #10 thousand, not a typo
                        if AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 1:
                            x = 1
                            p1n = nametank[x]
                            power1n = powers[x]
                            pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 2:
                            x = 1
                            p2n = nametank[x]
                            power2n = powers[x]
                            pokemon2 = [1,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 3:
                            x = 1
                            p1n = nametank[x]
                            power1n = powers[x]
                            pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 4:
                            x = 1
                            p3n = nametank[x]
                            power3n = powers[x]
                            pokemon3 = [1,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n] 
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 5:
                            x = 1
                            p5n = nametank[x]
                            power5n = powers[x]
                            pokemon5 = [1,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 6:
                            x = 1
                            p6n = nametank[x]
                            power6n = powers[x]
                            pokemon6 = [1,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                        else:
                            print("All your pokemon are full.")
                            money += 10000
                            print("Money refunded.")
                    elif rich.lower() == "g":
                        money -= 6000 #15 thousand, not a typo
                        if AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 1:
                            x = 2
                            p1n = nametank[x]
                            power1n = powers[x]
                            pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 2:
                            x = 2
                            p2n = nametank[x]
                            power2n = powers[x]
                            pokemon2 = [1,0,h2n,pp1n2,pp2n2,pp3n2,pp4n2,pp5n2,p2n,power2n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 3:
                            x = 2
                            p1n = nametank[x]
                            power1n = powers[x]
                            pokemon1 = [1,0,h1n,pp1n1,pp2n1,pp3n1,pp4n1,pp5n1,p1n,power1n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 4:
                            x = 2
                            p3n = nametank[x]
                            power3n = powers[x]
                            pokemon3 = [1,0,h3n,pp1n3,pp2n3,pp3n3,pp4n3,pp5n3,p3n,power3n] 
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 5:
                            x = 2
                            p5n = nametank[x]
                            power5n = powers[x]
                            pokemon5 = [1,0,h5n,pp1n5,pp2n5,pp3n5,pp4n5,pp5n5,p5n,power5n]
                        elif AuxFunctions.PokemonLive(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6) == 6:
                            x = 2
                            p6n = nametank[x]
                            power6n = powers[x]
                            pokemon6 = [1,0,h6n,pp1n6,pp2n6,pp3n6,pp4n6,pp5n6,p6n,power6n]
                        else:
                            print("All your pokemon are full.")
                            money += 15000
                            print("Money refunded.")
                    else:
                        print("I do not understand.")
            elif origd.lower() == "boss":
                boss = 1
                opphp = 200
                op = random.randint(len(nametank)-2,len(nametank)-1)
                opower = powers[op]
                print("You are fighting", nametank[op])
                print("Its power is",opower)
            elif origd.lower() == "quest":
                AuxFunctions.Quest(hp,opphp,hunger,q1,q2,q3,cow,chicken,plantfood,distance)
            elif origd.lower() == "save":
                op = random.randint(0,len(nametank)-1)
                AuxFunctions.SaveGame(outputFile,name,hp,win,money,Powerup,opphp,pp1,pp2,pp3,pp4,pp5,diff,lig,blaster,blaster2,blaster3,blaster4,blaster_ammo,HPdecreaser,HPdecreaser2,HPdecreaser3,HPdecreaser4,arrow,hunger,cow,chicken,plantfood,deposit,moneybank,strdeposit,depoadd,withdraw,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6,h1n,h2n,h3n,h4n,h5n,h6n,pp1n1,pp1n2,pp1n3,pp1n4,pp1n5,pp1n6,pp2n1,pp2n2,pp2n3,pp2n4,pp2n5,pp2n6,pp3n1,pp3n2,pp3n3,pp3n4,pp3n5,pp3n6,pp4n1,pp4n2,pp4n3,pp4n4,pp4n5,pp4n6,pp5n1,pp5n2,pp5n3,pp5n4,pp5n5,pp5n6,p1n,p2n,p3n,p4n,p5n,p6n,power1n,power2n,power3n,power4n,power5n,power6n,totactiv, totalife,mypower,op,ppill)
            elif origd.lower() == "ps" or origd.lower() == "pokemon shop" or origd.lower() == "pokemon store":
                print("We have every item you can imagine:")
                shopd = input("So, view or buy?")
                if shopd.lower() == "buy" or shopd.lower() == "b":
                    if money <= 0:
                        print("You have no use here, for you have", money,"money.")
                    else:
                        shop2 = input("What will you buy?(dont know? look in 'view')Note:everything is SINGULAR -NO PLURALS.")
                        if shop2.lower() == "potion":
                            print("Okay, 1 potion")                        
                            if money - 20 > 0:
                                print("coming right up")
                                ppp = ppp + 4
                                money = money - 20
                            else:
                                print("...Not coming right up.") 
                        elif shop2.lower() == "hyper potion":
                            print("Sure.")
                            if money - 50 > 0:
                                print("coming right up")
                                hppp = hppp + 2
                                money = money - 50
                            else:
                                print("...Not coming right up.") 
                        elif shop2.lower() == "pp pill":
                            print("4 PP pills coming straight from our safe, and good Pokemon Pharmacy.")                       
                            if money - 50 > 0:
                                print("coming right up")
                                ppill = ppill + 4
                                money = money - 50
                            else:
                                print("...Not coming right up.") 
                        elif shop2.lower() == "full potion":
                            print("1 Full potion coming right up.")
                            if money - 50 > 0:
                                print("coming right up")
                                fppp = fppp + 1
                                money = money - 50
                            else:
                                print("...Not coming right up.") 
                        elif shop2.lower() == "full restore":
                            print("1 FULL RESTORE coming right up.")
                            if money - 75 > 0:
                                print("coming right up")
                                frpp = frpp + 1
                                money = money - 75
                            else:
                                print("...Not coming right up.") 
                        elif shop2.lower() == "stone":
                            print("5 stones")
                            if money - 20 > 0:
                                print("coming right up")
                                stone = stone + 5
                                money = money - 20
                            else:
                                print("...Not coming right up.") 
                        elif shop2.lower() == "rock":
                            print("3 rocks")                        
                            if money - 15 > 0:
                                print("Coming right up")
                                rock = rock + 3
                                money = money - 15
                            else:
                                print("...Not coming right up.")    
                        elif shop2.lower() == "boulder":
                            print("Two boulders, coming your way!")
                            if money - 45 > 0:
                                print("Coming right up")
                                bould = bould + 2
                                money = money - 45
                            else:
                                print("...Not coming right up.")
                        elif shop2.lower() == "blaster":
                            print("Hey kid, don't get in trouble with the police, 'cause they'll be after me!So just making sure, 1 blaster (and 15 blaster-ammo, if it's your first blaster)")
                            if money - 200 > 0:
                                if blaster > 0:
                                    if money - 200 > 0:
                                        if blaster2 > 0:
                                            if money - 200 > 0:
                                                if blaster3 > 0:
                                                    if money - 200 > 0:
                                                        print("You must want an upgrade.")
                                                        blaster4 = blaster4 + 1
                                                        money = money - 200
                                                        print("You have unlocked the final blaster.")
                                                    else:
                                                        print("You don't have enough money to buy a 4th lvl blaster.")
                                                else:
                                                    print("You have a bazooka.")
                                                    blaster3 = blaster3 + 1
                                                    money = money - 200
                                            else:
                                                print("You can't afford a Bazooka.")
                                        else:
                                            print("Then you must want an upgrade.")
                                            blaster2 = blaster2 + 1
                                            money = money - 200
                                            print("You have a second level blaster!(machine blaster)")
                                    else:
                                        print("You can't afford the upgrade(that's why you have a bank account).")
                                else:    
                                    print("Coming right up")
                                    money = money - 200
                                    blaster = blaster + 1
                                    blaster_ammo = blaster_ammo + 15
                            else:
                                print("...Not coming right up.")
                        elif shop2.lower() == "blaster ammo":
                            print("Okay kiddo, be safe, so 1 pack of 10 blaster-ammo")
                            if money - 20 > 0:
                                print("Coming right up")
                                blaster_ammo = blaster_ammo + 10
                                money = money - 20
                            else:
                                print("...Not coming right up.")
                        elif shop2.lower() == "powerup":
                            print("Okay, just make sure not to hurt anyone,so 1 Powerup")
                            if money - 100 > 0:
                                print("Coming right up")
                                money = money - 100
                                Powerup = Powerup + 1
                            else:
                                print("...Not coming right up.")
                        elif shop2.lower() == "hpdecreaser":
                            print("Hey kid, don't get in trouble with the police, 'cause they'll be after me!So just making sure, 1 HPdecreaser (and 10 arrows, if it's your first HPdecreaser)")
                            if money - 50 > 0:
                                if HPdecreaser > 0:
                                    if money - 50 > 0:
                                        if HPdecreaser2 > 0:
                                            if money - 50 > 0:
                                                if HPdecreaser3 > 0:
                                                    if money - 50 > 0:
                                                        print("You must want an upgrade.")
                                                        HPdecreaser4 = HPdecreaser4 + 1
                                                        money = money - 50
                                                        print("You have unlocked the final HPdecreaser.")
                                                    else:
                                                        print("You don't have enough money to buy a 4th lvl HPdecreaser.")
                                                else:
                                                    print("You have a super HPdecreaser.")
                                                    HPdecreaser3 = HPdecreaser3 + 1
                                                    money = money - 50
                                            else:
                                                print("You can't afford a Bazooka.")
                                        else:
                                            print("Then you must want an upgrade.")
                                            HPdecreaser2 = HPdecreaser2 + 1
                                            money = money - 50
                                            print("You have a second level HPdecreaser!(rapid HPdecreaser)")
                                    else:
                                        print("You can't afford the upgrade(that's why you have a bank account).")
                                else:    
                                    print("Coming right up")
                                    money = money - 50
                                    HPdecreaser = HPdecreaser + 1
                                    arrow = arrow + 10
                            else:
                                print("...Not coming right up.")
                        elif shop2.lower() == "arrow":
                            print("Okay, 20 arrows.")
                            if money - 30 > 0:
                                print("Coming right up")
                                money = money - 30
                                arrow = arrow + 20
                            else:
                                print("...Not coming right up.")
                        elif shop2.lower() == "pokeball":
                            print("Sure, 20 pokeballs")
                            if money - 75 > 0:
                                print("Coming right up.")
                                pokepp = pokepp + 20
                                money = money - 75
                            else:
                                print("...Not coming right up.")
                        elif shop2.lower() == "ultraball":
                            print("10 ultraballs")
                            if money - 100 > 0:
                                print("Coming right up.")
                                ultrapp = ultrapp + 10
                                money = money - 100
                            else:
                                print("...Not coming right up.")
                        else:
                            if shop2[-1:] == "s":
                                print("Oh! You typed it plural!")
                            else:
                                print("I have no clue what you're typing.")
                else: #view
                    print("""We have,pokeballs, ultraballs, potions, hyper-potions, Full potions, full restores, PP pill, stones, rocks, boulder, blasters, blaster_ammos, knives, HPdecreasers and arrows,
                    and more items being shipped .""")
                    print("Pokeballs, 20 for 75(catch pokemon)")
                    print("Ultraballs, 10 for 100(catch more effectively)")
                    print("Potions cost 20 for 4 potions.(restore health)")
                    print("Hyper-Potions cost 50 for 2.(restore even more)")
                    print("Full potions cost 50 for 1(restore more than any potion out there.")
                    print("Full Restore costs 75 for 1(restores as well as full and restores PP.")
                    print("PP pills cost 50 for 4( restore PP)")
                    print("Stones cost 10 for 5(do minimal damage, but your opponent doesn't attack back.")
                    print("Rocks cost 15 for 3(do more damage, and opponent doesn't attack back.")
                    print("Boulders cost 45 for 2(do much more damage, and opponent doesn't attack back.")
                    print("blasters cost 200 for blaster(comes with 15 blaster_ammos);it does an EXTREME amount of damage.\nUpgrades include: 2.0 blaster, Blaster 3.0, and finally, a one-of-a-kind Decimator.")
                    print("blaster_ammos cost 20 for 10(Ammo for the blaster to work).")
                    print("Powerups cost 100 for unlimited use. You obviously can't go and attack the wild pokemon yourself, so it boost your pokemon's strength.")
                    print("HPdecreasers cost 50 for HPdecreaser(with 10 arrows), do fair amount of damage.")
                    print("Arrows cost 30 for 20(ammo for HP-decreasers).")
                    time.sleep(0.5)
                    print("You have this much money to spend:", money)
            else:
                print("Sorry, I have no idea what you are saying.")
    if totalife <= 0 and totactiv <= 0:
        pokemon1[0] = a
        pokemon1[1] = b
        totalife = int(pokemon1[0]) + int(pokemon2[0]) + int(pokemon3[0]) + int(pokemon4[0]) + int(pokemon5[0]) + int(pokemon6[0])
        totactiv = int(pokemon1[1]) + int(pokemon2[1]) + int(pokemon3[1]) + int(pokemon4[1]) + int(pokemon5[1]) + int(pokemon6[1])
        input(str(totalife) + "totalife")
        input(str(totactiv) + "totactive")
        print(pokemon1[0],pokemon1[1])
        try:
            Player.stop()
        except NameError:
            print("There has been a serious error with the music brake system. We better call a mechanic.")
        print("Welcome to Pokemon Center Hospital")
        print("You are in the Emergency Room with your Pokeballs!")
        print("The head doctor stands before you.")
        print("He says:\nYour medical bill is high. You must lose 20 wins, and lose 200 dollars")
        while totalife <= 0 and totactiv <= 0:
            godsaid = input("Pay or don't")
            if godsaid.lower() == "pay":
                if win >= 20 and money >= 200:
                    print("You will pay.")
                    win -= 20
                    money -= 200
                    h1n = 100
                    hp = 100
                    pokemon1[0] = 1
                    pokemon1[1] = 1
                    print(pokemon1[0],pokemon1[1])
                    totalife = 1
                    totactiv = 1
                    a = pokemon1[0]
                    b = pokemon1[1]
                    break
                else:
                    print("You will be in debt but I will still charge you.")
                    win -= 20
                    money -= 200
                    pokemon1[1] = 1
                    pokemon1[0] = 1
                    h1n = 100
                    hp = 100
                    print(pokemon1[0],pokemon1[1])
                    a = pokemon1[0]
                    b = pokemon1[1]
                    totalife = 1
                    totactiv = 1
                    break
            else:
                print("xxx")
    while totactiv != totalife:
        totalife = pokemon1[0] + pokemon2[0] + pokemon3[0] + pokemon4[0] + pokemon5[0] + pokemon6[0]
        totactiv = pokemon1[1] + pokemon2[1] + pokemon3[1] + pokemon4[1] + pokemon5[1] + pokemon6[1]
        if totactiv == 0 and totalife > 0:
            if pokemon1[0] == 1:
                pokemon1[1] = 1
            else:
                if pokemon2[0] == 1:
                    pokemon2[1] = 1
                else:
                    if pokemon3[0] == 1:
                        pokemon3[1] = 1
                    else:
                        if pokemon4[0] == 1:
                            pokemon4[1] = 1
                        else:
                            if pokemon5[0] == 1:
                                pokemon5[1] = 1
                            else:
                                if pokemon6[0] == 1:
                                    pokemon6[1] = 1
                                else:
                                    print("Major Major glitch(line 2727) glitch, please reevaluate program.")
        
        elif totalife == 0 and totactiv == 1:
            print("Kinda strange glitch.")
            print("You see, I detected that you have 1 active pokemon but 0 alive pokemon.")
            print("I'll fix it though.")
            pokemon1[1] = 0
            pokemon2[1] = 0
            pokemon3[1] = 0
            pokemon4[1] = 0
            pokemon5[1] = 0
            pokemon6[1] = 0
            print("Good. Now no pokemon are alive or active.")
        else:
            if totalife > 0 and totactiv > 0:
                print()
            else:
                print("Major Major glitch(line 2697) glitch, please reevaluate program.")
        totalife = pokemon1[0] + pokemon2[0] + pokemon3[0] + pokemon4[0] + pokemon5[0] + pokemon6[0]
        totactiv = pokemon1[1] + pokemon2[1] + pokemon3[1] + pokemon4[1] + pokemon5[1] + pokemon6[1]    
        if totactiv == 0 and totalife > 0:
            print("You have zero pokemon active, but more than zero alive.")
