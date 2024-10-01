'''The Gladiator by Daniel Scott.
This is a game where the player must fight different enemies.
After each round, the player earns gold which can be spent
on weapons and armor. The game ends when the player dies.'''

#RNG.
from random import randint
#Equipment parent class.
class Equipment(object):
    def __init__(self, name, cost, defense):
        self.name = name
        self.cost = cost
        self.defense = defense

nothing = Equipment('nothing', 0, 0)

#Weapons subclass.
class Weapon(Equipment):
    '''Weapons constructor. Includes name, power, hands needed, and cost.
    other variables will be defined in each subclass as needed.'''
    def __init__(self, name, power, cost):
        self.name = name
        self.power = power
        self.cost = cost

rustySword = Weapon('Rusty Sword', 1, 0)
metalSword = Weapon('Metal Sword', 5, 25)
vorpalSword = Weapon('Vorpal Sword', 50000, 0)

#Shields.
class Shield(Equipment):
    #Shields constructor. Includes its name, cost, and chance to block.
    def __init__(self, name, block, cost):
        self.name = name
        self.block = block
        self.cost = cost

potLid = Shield('Pot Lid', 2, 0)

#Armor.
class Armor(Equipment):
    #Armor constructor. Includes name, armor rating, slot, and cost.
    def __init__(self, name, defense, cost):
        self.name = name
        self.defense = defense
        self.cost = cost

prisonClothes = Armor('Prison Clothes', 1, 0)

#Helmets.
class Helmet(Equipment):
    def __init__(self, name, defense, cost):
        self.name = name
        self.defense = defense
        self.cost = cost

#Shoes.
class Shoes(Equipment):
    def __init__(self, name, defense, speed, cost):
        self.name = name
        self.defense = defense
        self.speed = speed
        self.cost = cost

prisonSandals = Shoes('Prisoner Shoes', 1, 5, 0)

#The items.
class Item(object):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class HealthPotion(Item):
    def __init__(self, name, hp, cost):
        self.name = name
        self.hp = hp
        self.cost = cost

class ManaPotion(Item):
    def __init__(self, name, mp, cost):
        self.name = name
        self.mp = mp
        self.cost = cost

lesserHealthPotion = HealthPotion('Lesser Health Potion', 10, 30)
lesserManaPotion = ManaPotion('Lesser Mana Potion', 10, 50)

class SpellScroll(Item):
    def __init__(self, name, spellName, cost):
        self.name = name
        self.spellName = spellName
        self.cost = cost

#The player.
class Player(object):
    inventory = {}
    equipment = {
        'Weapon' : rustySword,
        'Shield' : potLid,
        'Helmet' : nothing,
        'Armor' : prisonClothes,
        'Shoes' : prisonSandals}
    spells = {
        'Heal Wounds' : False,
        'Rising Anger' : False,
        'Flamethrower' : False,
        'Mana Siphon' : False,
        'Health Drain' : False}
    #Player constructor. Includes the player's stats, items, and gold.
    def __init__(self, name, level, xp, neededXP, hp, maxHP, mp, maxMP, att, \
    defense, agi, intelligence, wis, status, glory, gold):
        self.name = name
        self.level = level
        self.xp = xp
        self.neededXP = neededXP
        self.hp = hp
        self.maxHP = maxHP
        self.mp = mp
        self.maxMP = maxMP
        self.att = att
        self.defense = defense
        self.agi = agi
        self.intelligence = intelligence
        self.wis = wis
        self.status = status
        self.glory = glory
        self.gold = gold

    #Method to set HP.
    def increaseHP(self, value):
        self.hp = self.hp + value
        if self.hp > self.maxHP:
            self.hp = self.maxHP

    #Method to decrease HP.
    def lowerHP(self, value):
        self.hp = self.hp - value

    #Method to set HP to a certain value.
    def setHP(self, value):
        self.hp = value

    #Method to increase HP. Used when leveling up.
    def increaseMaxHP(self):
        self.hp = self.hp + 6
        self.maxHP = self.maxHP + 6
        print "Your HP increased by 6."

    #Method to lower MP. Used when casting magic.
    def decreaseMP(self, value):
        self.mp = mp - value
        if self.mp < 0:
            self.mp = 0

    #Method to increase MP. Some magic may be able to steal MP.
    def increaseMP(self, value):
        self.mp = self.mp + value
        if self.mp > self.maxMP:
            self.mp = self.maxMP

    def setMP(self, value):
        self.mp = value

    #Method to increase MP. Used when leveling up.
    def increaseMaxMP(self):
        self.mp = self.mp + 4
        self.maxMP = self.maxMP + 4
        print "Your MP increased by 4."

    #Methods to increase stats. Used when leveling up.
    def increaseAtt(self):
        self.att = self.att + 4
        print "Your attack increased by 4."

    def increaseDef(self):
        self.defense = self.defense + 3
        print "Your defense increased by 3."

    def increaseAgi(self):
        self.agi = self.agi + 3
        print "your agility increased by 3."
        
    def increaseInt(self):
        self.intelligence = self.intelligence + 1
        print "Your intelligence increased by 1."

    def increaseWis(self):
        self.wis = self.wis + 2
        print "Your wisdom has increased by 2."
        print ""

    #The following methods set the player's equipment.
    def equipWeapon(self, Weapon):
        if Weapon in self.inventory:
            if self.equipment['Weapon'] != Weapon:
                #Puts the players old item back in the inventory.
                #If it's not in the inventory, it will put a copy in there.
                if self.equipment['Weapon'] not in self.inventory:
                    self.inventory[self.equipment['Weapon']] = 1
                else:
                    #If the player already has one, one more is added.
                    self.inventory[self.equipment['Weapon']] = \
                    self.inventory[self.equipment['Weapon']] + 1
                #Changes the player's equipped item.
                self.equipment['Weapon'] = Weapon
                #Removes 1 of the equipped item from the inventory.
                self.inventory[Weapon] = self.inventory[Weapon] - 1
                #If there is no more of the item, it is removed.
                if self.inventory[Weapon] == 0:
                    del self.inventory[Weapon]
                print "You equip the %s. to your main hand." % Weapon.name
                print ""
            else:
                print "You already have that equipped!"
                print ""
        else:
            print "You don\'t have that weapon!"
            print ""
    
    def equipShield(self, Shield):
        if Shield in self.inventory:
            if self.equipment['Shield'] != Shield:
                if self.equipment['Shield'] not in self.inventory:
                    self.inventory[self.equipment['Shield']] = 1
                else:
                    self.inventory[self.equipment['Shield']] = \
                    self.inventory[self.equipment['Shield']] + 1
                self.equipment['Shield'] = Shield
                self.inventory[Shield] = self.inventory[Shield] - 1
                if self.inventory[Shield] == 0:
                    del self.inventory[Shield]
                print "You equip the %s to your off hand." % Shield.name
                print ""
            else:
                print "You already have that equipped!"
                print ""
        else:
            print "You don\'t have that shield!"
            print ""

    def equipHelmet(self, Helmet):
        if Head in self.inventory:
            if self.equipment['Helmet'] != Helmet:
                if self.equipment['Helmet'] == nothing:
                    self.equipment['Helmet'] = Helmet
                    self.inventory[Helmet] = self.inventory[Helmet] - 1
                    if self.inventory[Helmet] == 0:
                        del self.inventory[Helmet]
                else:
                    if self.equipment['Helmet'] not in self.inventory:
                        self.inventory[self.equipment['Helmet']] = 1
                    else:
                        self.inventory[self.equipment['Helmet']] = \
                        self.inventory[self.equipment['Helmet']] + 1
                    self.equipment['Helmet'] = Helmet
                    self.inventory[Helmet] = self.inventory[Helmet] - 1
                    if self.inventory[Helmet] == 0:
                        del self.inventory[Helmet]
                print "You put on the %s." % Helmet.name
                print ""
            else:
                print "You already have that equipped!"
                print ""
        else:
            print "You don\'t have that helmet!"
            print ""

    def equipArmor(self, Armor):
        if Armor in self.inventory:
            if self.equipment['Armor'] != Armor:
                if self.equipment['Weapon'] not in self.inventory:
                    self.inventory[self.equipment['Armor']] = 1
                else:
                    self.inventory[self.equipment['Armor']] = \
                    self.inventory[self.equipment['Armor']] + 1
                self.equipment['Armor'] = Armor
                self.inventory[Armor] = self.inventory[Armor] - 1
                if self.inventory[Armor] == 0:
                    del self.inventory[Armor]
                print "You equip the %s." % Armor.name
                print ""
            else:
                print "You already have that equipped!"
                print ""
        else:
            print "You don\'t have that armor!"
            print ""

    def equipShoes(self, Shoes):
        if Shoes in self.inventory:
            if self.equipment['Shoes'] != Shoes:
                if self.equipment not in self.inventory:
                    self.inventory[self.equipment['Shoes']] = 1
                else:
                    self.inventory[self.equipment['Shoes']] = \
                    self.inventory[self.equipment['Shoes']] + 1
                self.equipment['Shoes'] = Shoes
                self.inventory[Shoes] = self.inventory[Shoes] - 1
                if self.inventory[Shoes] == 0:
                    del self.inventory[Shoes]
                print "You equip the %s." % Shoes.name
                print ""
            else:
                print "You already have that equipped!"
                print ""
        else:
            print "You don\'t have those shoes!"
            print ""

    #This method sets status ailments that the player may get in battle.
    def setStatus(self, string):
        self.status = string

    '''Method to increase glory. Glory is increased after each battle.
    If you have enough glory, Jupiter might be merciful...'''
    def gainGlory(self, value):
        self.glory = self.glory + value

    #This method halves glory if Jupiter decides to revive you when you die.
    def halveGlory(self):
        self.glory = self.glory / 2

    #This method increases your gold. Gold is gained from fighting monsters.
    def gainGold(self, value):
        self.gold = self.gold + value
        print "You gained %s gold." % value

    #This method decreases gold. Used when buying weapons, items, or armor.
    def spendGold(self, value):
        self.gold = self.gold - value

    #This adds an item to your inventory.
    def getItem(self, item):
        if item not in self.inventory:
            self.inventory[item] = 1
        else:
            self.inventory[item] = self.inventory[item] + 1

    #This method increases XP needed to level. Called when leveling up.
    def newNeededXP(self):
        self.neededXP = self.neededXP + (self.neededXP * 1.5)

    #This method levels up the player.
    def levelUp(self):
        self.level = self.level + 1
        print "Congratulations! You reached level %s!" % self.level
        self.increaseMaxHP()
        self.increaseMaxMP()
        self.increaseAtt()
        self.increaseDef()
        self.increaseAgi()
        self.increaseInt()
        self.increaseWis()
        print ""
        if self.level < 20:
            self.newNeededXP()
            if self.xp > self.neededXP:
                self.levelUp()

    #Method for player to gain XP. XP is gained from fighting monsters.
    def gainXP(self, value):
        self.xp = self.xp + value
        print "You gained %s experience points." % value
        if self.level < 20:
            if self.xp > self.neededXP:
                self.levelUp()

#Monsters class.
class Monster(object):
    #Monster constructor. Includes its name, stats, and rewards for killing.
    def __init__(self, name, monsterType, hp, maxHP, mp, maxMP, att, defense, \
    agi, intelligence, wis, gold, xp, glory, item, dropRate):
        self.name = name
        self.monsterType = monsterType
        self.hp = hp
        self.maxHP = maxHP
        self.mp = mp
        self.maxMP = maxMP
        self.att = att
        self.defense = defense
        self.agi = agi
        self.intelligence = intelligence
        self.wis = wis
        self.gold = gold
        self.xp = xp
        self.glory = glory
        self.item = item
        self.dropRate = dropRate

    def lowerHP(self, damage):
        self.hp = self.hp - damage

    #This will set the monster's HP to its maximum at the start of a new battle.
    def resetHP(self):
        self.hp = self.maxHP

    def lowerMP(self, damage):
        self.mp = self.mp - damage

    def resetMP(self):
        self.mp = self.maxMP

#Sets the player's name before initializing the player object.
playerName = raw_input("Greetings, player! What is thy name? ")
gladiator = Player(playerName, 1, 0, 100, 12, 12, 4, 4, 8, 4, 1, 1, 1, \
'Normal', 0, 0)

#The game's intro sequence.
def main():
    print ""
    print "Greetings %s!" % gladiator.name
    print "You have been found guilty by the Roman Empire."
    print "Your punishment: Death in the Colliseum! But you are not weak."
    print "Those who can slay the guardian will be pardoned."
    print "This is your only hope! Can you survive the Colliseum?"
    print "Can you face the mightiest foe and earn your freedom?"
    print "Go now, and fight for glory!"
    print ""
    cell()

#The main menu, where the player can prepare for their fights.
def cell():
    print "You are now in your cell. There is a number of things you can do."
    print "Will you:"
    print "1. Face your next enemy in the arena."
    print "2. Challenge the guardian of the arena. (You will not win this...)"
    print "3. Shop for items and equipment. (Unimplemented.)"
    print "4. Manage your equipment and items. (Unimplemented.)"
    print "5. Check your stats."
    print "6. Sleep in your bunk."
    print "7. Forfeit, and return to real life."
    choice = input("Please make a selection. ")
    print ""
    while choice < 1 or choice > 7  or choice == 3:
        if choice == 3:
            print "Sorry, that isn't implemented yet."
            choice = input("Please select another option. ")
        else:
            choice = input("Select an option from the menu! ")
            print ""
    if choice == 1:
        print "Okay."
        print "You step out into the arena to face your next foe."
        combatStart()
    elif choice == 2:
        print "You demand to face the guardian of the arena."
        print "The guard laughs and says 'Nice knowing you!'"
        print "When you step out into the arena, the Emporer shouts,"
        print "'Bring out the Jabberwocky!' At first you laugh at the name."
        print "Your laughter is cut short when you see a terrifying purple"
        print "monstrosity with a millions legs and eyes. You feel as though"
        print "you don't stand a snowball's chance in Hell against this thing."
        '''The player can only fight the final boss
        if they have the Vorpal Sword equipped.'''
        if gladiator.equipment['Weapon'] == vorpalSword:
            print "Suddenly, as if responding to the abomination before you,"
            print "the sword suddenly goes 'snicker-snack'."
            print "The Jabberwocky suddenly looks frightened."
            print "You think you found the creature's weakness."
            jabberwocky = Monster('Jabberwocky', 'Abomination', \
            1000, 1000, 0, 0, 50, 50, 0, 0, 0, 0, 0, 0, nothing, 0)
            combat(jabberwocky)
        else:
            print "The Jabberwocky unceremoniously tramples you underfoot."
            badEnd()
    elif choice == 4:
        print "Okay."
        itemMenu()
    elif choice == 5:
        print "Okay."
        checkStats()
    elif choice == 6:
        print "Okay."
        rest()
    elif choice == 7:
        print "Okay."
        badEnd()

#Combat initialization module will randomly instantiate a monster.
def combatStart():
        monster = randint(1, 3)
        if monster == 1:
            skeletonSoldier = Monster('Skeleton Soldier', 'Undead', \
            12, 12, 0, 0, 9, 5, 1, 1, 1, 25, 10, 1, metalSword, 25)
            print "Your next opponent is a Skeleton Soldier. Fight!"
            print ""
            combat(skeletonSoldier)
        elif monster == 2:
            myrmecolion = Monster('Myrmecolion', 'Abomination', \
            8, 8, 5, 5, 8, 3, 5, 1, 1, 0, 5, 0, lesserHealthPotion, 50)
            print "Your next opponent is a Myrmecolion. Fight!"
            print ""
            combat(myrmecolion)
        elif monster == 3:
            lich = Monster('Lich', 'Undead', \
            9, 9, 20, 20, 6, 6, 2, 4, 10, 20, 25, 2, lesserManaPotion, 10)
            print "Your next opponent is a Lich. Fight!"
            print ""
            combat(lich)
    
#Main combat module.
def combat(monster):
    while gladiator.hp > 0 and monster.hp > 0:
        #If the player is gaurding this will be True.
        guarding = False
        choice = False
        #If the player can't make a valid choice, this will loop.
        while choice == False:
            option = 0
            option = combatMenu(option)
            if option == 1 or option == 3:
                choice = True
            elif option == 2:
                spell = spellMenu()
                if spell != 0:
                    choice = True
            elif option == 4:
                item = combatItem()
                if item != 0:
                    choice = True
        #This determines what action the enemy will take.
        monsterChoice = randint(0, 1)
        if option == 1:
            print ""
            print "You swing to attack!"
            #RNG decides if attack will hit or miss.
            toHit = randint(1, 100)
            #Monster's agility determines if it dodges or not.
            if toHit > monster.agi:
                damage = playerDamage(monster)
                #If the skeleton blocks, you do half your damage to it.
                if monsterChoice == 1 and monster.name == 'Skeleton Soldier':
                    damage = damage / 2
                #You do at least 1 damage to any enemy if you hit.
                if damage < 1:
                    damage = 1
                monster.lowerHP(damage)
                print "You do %s damage to the %s!" % (damage, monster.name)
                #Breaks the loop if the monster dies.
                if monster.hp <= 0:
                    break
            else:
                print "You missed!"
        elif option == 2:
            spell = castMagic(monster)
        elif option == 3:
            guarding = True
            print ""
            print "You guard against your opponent's attack."
        elif option == 4:
            useItem(monster)
        #Choice 0 is always the monster's basic attack.
        if monsterChoice == 0:
            print ""
            print "The %s attacks!" % monster.name
            toHit = randint(1, 100)
            evasion = playerEvasion()
            if toHit > evasion:
                block = playerBlock()
                toBlock = randint(1, 100)
                if toBlock <= block:
                    print "You blocked its attack!"
                    print ""
                else:
                    damage = monsterDamage(monster)
                    if guarding == True:
                        damage = damage / 2
                    if damage < 1:
                        damage = 1
                    gladiator.lowerHP(damage)
                    print "The %s does %s damage!" % (monster.name, damage)
                    print ""
                    if gladiator.hp <= 0:
                        mercyOfJupiter()
            else:
                print "The %s missed!" % monster.name
                print ""
        #Choice 1 is dependant on the type of monster.
        elif monsterChoice == 1:
            if monster.name == 'Skeleton Soldier':
                print ""
                print "The Skeleton Soldier is guarding..."
                print ""
            elif monster.name == 'Myrmecolion':
                #The Myrmecolion is meant to be the weakest enemy in game.
                #Its "special action" is worthless.
                print ""
                print "The myrmecolion tries to growl. It doesn't work."
                print ""
            elif monster.name == 'Lich':
                print ""
                print "The Lich reaches out to touch you..."
                #The Lich's touch attack deals half its magic damge 3 times.
                magicDamage = monsterMagicDamage(monster) / 2
                for attack in range(0, 3):
                    gladiator.lowerHP(magicDamage)
                    print "The Lich does %s damage." % magicDamage
                ""
            elif monster.name == 'Jabberwocky':
                print ""
                print "The Jabberwocky thrashes about!"
                #The Jabberwocky's thrash attack does half its damage 3 times.
                damage = monsterDamage(monster) / 2
                for attack in range(0, 3):
                    gladiator.lowerHP(damage)
                    print "The Jabberwocky does %s damage." % damage
                ""
    if gladiator.hp < 0:
        badEnd()
    elif monster.name == 'Jabberwocky':
        goodEnd()
    else:
        youWin(monster)

def combatMenu(choice):
    #Combat menu.
    print "Choose an action from the following:"
    print "1. Attack!"
    print "2. Cast magic. (Unimplemented)"
    print "3. Guard."
    print "4. Use an item. (Not fully implemented)"
    choice = input("What will you do? ")
    #Error trap.
    while choice < 1 or choice > 4:
        print ""
        choice = input("Please choose a valid option. ")
    #Returns the value of choice to 'combat()'.
    return choice
  

def playerDamage(monster):
    damage = gladiator.att + gladiator.equipment['Weapon'].power \
    - monster.defense
    return damage

def playerEvasion():
    evasion = gladiator.agi + gladiator.equipment['Shoes'].speed
    return evasion

def playerBlock():
    block = gladiator.equipment['Shield'].block
    return block

def monsterDamage(monster):
    damage = monster.att - gladiator.defense \
    - gladiator.equipment['Helmet'].defense \
    - gladiator.equipment['Armor'].defense \
    - gladiator.equipment['Shoes'].defense
    return damage

def monsterMagicDamage(monster):
    damage = monster.intelligence - gladiator.wis
    return damage

#Module for the cast magic menu.
def castMagic(monster):
    print "Whoops, this isn't implemented yet. Try again later!"
    return 

def useItem(monster):
    print "Whoops, this isn't implemented yet. Try again later!"
    return 

#Module for the use item menu.
def spellMenu():
    print ""
    print "This menu isn't finished yet. Try again later!"
    print ""
    return 0

def combatItemMenu():
    print ""
    print "This menu isn't finished yet. Try again later!"
    print ""
    return 0

def youWin(monster):
    #A victory message is displayed, and you gain XP, gold, and glory.
    #Glory is a hidden stat. If it's high enough, you may get a second chance.
    print "You defeated the %s!" % monster.name
    gladiator.gainXP(monster.xp)
    gladiator.gainGold(monster.gold)
    gladiator.gainGlory(monster.glory)
    chance = randint(1, 100)
    #If you roll lower than the monster's drop rate, you get an item from it.
    if chance <= monster.dropRate:
        #This adds the item to the player's inventory.
        if monster.item not in gladiator.inventory:
            gladiator.inventory[monster.item] = 1
        else:
            gladiator.inventory[monster.item] = \
            gladiator.inventory[monster.item] + 1
        print "The monster dropped a %s. You take it!" % monster.item.name
    print "The crowd goes wild and throw flowers to you. You pick one up."
    print "The Emperor has a sour look. With a motion, you are escorted"
    print "back to your prison cell..."
    print ""
    cell()

def itemMenu():
    print "What would you like to do?"
    print "1. Use an item."
    print "2. Equip an item."
    print "3. Back to the main menu."
    choice = input("Please choose an option. ")
    while choice < 1 or choice > 3:
        choice = input("Please choose a valid option. ")
    if choice == 1:
        print ""
        useItemMenu()
    elif choice == 2:
        print ""
        equipmentMenu()
    elif choice == 3:
        print ""
        cell()

def useItemMenu():
    print "You can use:"
    print "1. Lesser Health Potion"
    print "2. Lesser Mana Potion"
    print "3. Spell Scrolls"
    print "4. Back to the previous menu."
    choice = input("Choose one: ")
    while choice < 1 and choice > 4:
        choice = input("Please select a valid option. ")
    if choice == 1:
        if lesserHealthPotion in gladiator.inventory:
            print ""
            print "You use the Lesser Health Potion."
            print "Your HP increases by 10!"
            print ""
            gladiator.increaseHP(lesserHealthPotion.hp)
            gladiator.inventory[lesserHealthPotion] = \
            gladiator.inventory[lesserHealthPotion] - 1
            if gladiator.inventory[lesserHealthPotion] == 0:
                del gladiator.inventory[lesserHealthPotion]
            useItemMenu()
        else:
            print ""
            print "You don\'t even have that item!"
            print ""
            useItemMenu()
    elif choice == 2:
        if lesserManaPotion in gladiator.inventory:
            print ""
            print "You use the Lesser Mana Potion."
            print "Your MP increases by 10!"
            print ""
            gladiator.increaseMP(lesserManaPotion.mp)
            gladiator.inventory[lesserManaPotion] = \
            gladiator.inventory[lesserManaPotion] - 1
            if gladiator.inventory[lesserManaPotion] == 0:
                del gladiator.inventory[lesserManaPotion]
            useItemMenu()
        else:
            print ""
            print "You don\'t even have that item!"
            print ""
            useItemMenu()
    elif choice == 3:
        print ""
        print "Spells haven\'t been implemented yet. Check back later!"
        print ""
        useItemMenu()
    else:
        print ""
        itemMenu()

def equipmentMenu():
    print "Here are your slots:"
    print "1. Weapon."
    print "2. Shield."
    print "3. Helmet."
    print "4. Armor."
    print "5. Shoes."
    print "6. Back to the Previous Menu."
    choice = input("Please choose one: ")
    while choice < 1 or choice > 6:
        choice = input("Please select a valid option. ")
    if choice == 1:
        print ""
        equipWeapon()
    elif choice == 2 or choice == 3 or choice == 4 or choice == 5:
        print "There's currently no other items of that type."
        print "Check back later!"
        equipmentMenu()
    else:
        itemMenu()

def equipWeapon():
    print "You can equip one of the following:"
    print "1. Rusty Sword."
    print "2. Metal Sword."
    print "3. Vorpal Sword."
    print "4. Back to previous menu."
    choice = input("Please choose one: ")
    while choice < 1 or choice > 4:
        choice = input("Please enter a valid option. ")
    if choice == 1:
        print ""
        gladiator.equipWeapon(rustySword)
        equipWeapon()
    elif choice == 2:
        print ""
        gladiator.equipWeapon(metalSword)
        equipWeapon()
    elif choice == 3:
        print ""
        gladiator.equipWeapon(vorpalSword)
        equipWeapon()
    else:
        print ""
        equipmentMenu()
        
def checkStats():
    print "%s" % gladiator.name
    print "Level: %s" % gladiator.level
    print "XP: %s/%s" % (gladiator.xp, gladiator.neededXP)
    print "HP: %s/%s" % (gladiator.hp, gladiator.maxHP)
    print "MP: %s/%s" % (gladiator.mp, gladiator.maxMP)
    print "Weapon: %s" % gladiator.equipment['Weapon'].name
    print "Shield: %s" % gladiator.equipment['Shield'].name
    print "Helmet: %s" % gladiator.equipment['Helmet'].name
    print "Armor: %s" % gladiator.equipment['Armor'].name
    print "Shoes: %s" % gladiator.equipment['Shoes'].name
    print "Attack: %s" % gladiator.att
    print "Defense: %s" % gladiator.defense
    print "Agility: %s" % gladiator.agi
    print "Intelligence: %s" % gladiator.intelligence
    print "Wisdom: %s" % gladiator.wis
    #The Glory stat will be removed from this feature in the final.
    print "Status: %s" % gladiator.status
    print "Glory: %s" % gladiator.glory
    print "Gold: %s" % gladiator.gold
    print ""
    cell()

def rest():
    print "You lay down in your bunk bed. It's not comfortable but it'll do."
    print "Your HP, MP, and status have been restored."
    print ""
    gladiator.setHP(gladiator.maxHP)
    gladiator.setMP(gladiator.maxMP)
    gladiator.setStatus('Normal')
    cell()

def mercyOfJupiter():
    chance = randint(1, 100)
    if chance < gladiator.glory:
        print "As you feel your life fading away, you hear Jupiter speak."
        print "He proclaims: 'Come on, you can do better than that!"
        print "Arise, mortal!' With a strike of lightning you feel alive!"
        print ""
        gladiator.halveGlory
        gladiator.setHP(player.maxHP)
        gladiator.setMP(player.maxMP)
        gladiator.setStatus('Normal')

def badEnd():
    print "Your life is forfeit and you are fed to the Lions. Game over."
    print ""
    input("Thank you for playing. Press Enter to close.")

def goodEnd():
    print "At long last, the dreadful Jabberwocky has been defeated!"
    print "O frabjous day! Callooh! Callay!"
    print "You have fought your way out of the arena and earned your freedom!"
    print "... But the Emperor doesn't seem too pleased..."
    print "The guards reluctantly let you leave but you have a feeling"
    print "that you will need to watch your back from now on."
    print ""
    print "Congratulations! You won the game!"
    print "Programming code by Daniel Scott."
    input("Thank you for playing! Press Enter to close.")

main()
