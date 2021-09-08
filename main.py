from dataclasses import dataclass
import random


@dataclass
class Enemies:
    name: str
    health: int
    exp: int
    gold: int
    attack: str
    damage: int


@dataclass
class Player:
    player_health: int
    player_health_capacity: int
    gold: int
    exp: int
    potions: list
    weapons: list
    armor: list
    spells: list
    mana: int
    mana_capacity: int
    punch: int


@dataclass
class Death:
    succ1: bool
    succ2: bool
    inc: bool
    locust1: bool
    locust2: bool
    flies: bool
    flies2: bool
    lilcounter: int
    beecounter: int


@dataclass
class ItemPickup:
    lr5: bool
    lr8: bool
    gr3: bool
    gr4: bool
    gr5: bool
    gr9: bool
    gr12: bool
    gr13: bool


def playername() -> str:
    not_player_name = input("Name: ")
    if not_player_name == "Nate":
        print("You are not yet allowed to play this game.")
        quit()
    elif not_player_name == "Dante":
        print("A classic. Proceed.")
        player_name = not_player_name
    else:
        print("Ew, no.  We aren't using that.")
        player_name = input("Name: ")
        while player_name == not_player_name:
            print("I said pick a new one.")
            player_name = input("Name: ")
    return player_name


def item_pickup(player: Player, item_bools: ItemPickup, location: str) -> bool:
    if location == "Lust R5":
        item = "Lesser Health Potion"
        item_type = "potion"
        item_bool = item_bools.lr5
    elif location == "Lust R8":
        item = "Legendary 24 in. Sub"
        item_type = "weapon"
        item_bool = item_bools.lr8
    elif location == "Gluttony R3":
        item = "Mysterious Potion"
        item_type = "potion"
        item_bool = item_bools.gr3
    elif location == "Gluttony R4":
        item = "plate of spaghett"
        item_type = "food"
        item_bool = item_bools.gr4
    elif location == "Gluttony R5":
        item = "plate of spaghett"
        item_type = "food"
        item_bool = item_bools.gr5
    elif location == "Gluttony R9":
        item = "Cooked Turkey"
        item_type = "food"
        item_bool = item_bools.gr9
    elif location == "Gluttony R12":
        item = "Lo Mein"
        item_type = "food"
        item_bool = item_bools.gr12
    elif location == "Gluttony R13":
        item = "Fly Swatter"
        item_type = "weapon"
        item_bool = item_bools.gr13
    if item_bool == False:
        action = input("You see something on the table.  Do you take it?\n> ")
        if action == "Yes":
            if item_type == "weapon":
                player.weapons.append(item)
                item_bool = True
                print("You picked up a", item)
            elif item_type == "potion":
                player.potions.append(item)
                item_bool = True
                print("You picked up a", item)
            elif item_type == "armor":
                player.armor.append(item)
                item_bool = True
                if item == "Steel Armor":
                    player.player_health_capacity = (
                        player.player_health_capacity + 25)
                else:
                    player.player_health_capacity = (
                        player.player_health_capacity + 50)
                print("You put on the", item)
            elif item_type == "spell":
                player.spells.append(item)
                item_bool = True
                print("You have learned", item)
            elif item_type == "food":
                player.exp = (player.exp + 20)
                item_bool = True
                print(
                    "You ate the", item,
                    ", and it fills you with uncopywritten determination.  Exp + 20"
                )
        elif action == "No":
            print("fine then.  You take nothing.")
        else:
            print("You cant", action, "the", item)
            print("Guess you don't want it")
    return item_bool


limbo_info = "A pale white forest lays before you with a pale blue glow srounding you and the forest.  You feel a strange sensation around you as your body is enveloped in the strange blue light. \n\nYou can go to:\nOld Town\nCathedral\nDecent"

old_town_info = "A strange town in a strange place.  You see mostly just houses, but there is a sign pointing down at a reasonbly kept up building called 'Bill and Dave's Item and Magic Shoppe'\n\nYou can go to:\nCathedral\nShop\nDecent"

cathedral_info = "Walking towards a clearing, you see a cathedral that has been burnt down, but the ash from the surrounding field had seemed to give the burnt wood a ghastly white tint.  An old man stands at the pulpit. \n\nYou can got to: \nOld Town\nDecent\nOld Man"

shop_info = "You walk into the shop and notice two men bickering back and forth. One named Dave, the other Bill"

bill_info = """Hi, I'm Bill. I have so many items that are way better than my brother's dumb magic stuff.  Browse my wares.

Lesser Healing Potion - 20 gold
Healing Potion - 30 gold
Greater Healing Potion - 40 gold
Steel Armor - 100 gold
Mythril Armor - 200 gold
Steel Sword - 100 gold
Mythril Sword - 200 gold
"""


def bills_shop(player: Player) -> None:
    purchase = ""
    while purchase != "Q":
        purchase = input("Purchase: ").title()
        if purchase == "Lesser Healing Potion" and player.gold >= 20:
            player.potions.append("Lesser Healing Potion")
            player.gold = (player.gold - 20)
        elif purchase == "Healing Potion" and player.gold >= 30:
            player.potions.append("Healing Potion")
            player.gold = (player.gold - 30)
        elif purchase == "Greater Healing Potion" and player.gold >= 40:
            player.potions.append("Greater Healing Potion")
            player.gold = (player.gold - 40)
        elif purchase == "Steel Armor" and player.gold >= 100:
            player.armor.append("Steel Armor")
            player.gold = (player.gold - 100)
        elif purchase == "Mythril Armor" and player.gold >= 200:
            player.armor.append("Mythril Armor")
            player.gold = (player.gold - 200)
        elif purchase == "Steel Sword" and player.gold >= 100:
            player.weapons.append("Steel Sword")
            player.gold = (player.gold - 100)
        elif purchase == "Mythril Sword" and player.gold >= 200:
            player.weapons.append("Mythril Sword")
            player.gold = (player.gold - 200)
        else:
            print("invalid transaction")
        print("Gold:", player.gold)
        print("Exp:", player.exp)
        print("Potions:")
        for potion in player.potions:
            print(potion)
        print("\nWeapons:")
        for weapon in player.weapons:
            print(weapon)
        print("\nArmor:")
        for armors in player.armor:
            print(armors)
        print("\nSpells:")
        for spell in player.spells:
            print(spell)
        print("\n")


dave_info = """Im Dave, Nice to meet ya.  Here's my wares but, be warned: I only trade knowledge.

Lesser Mana Potion - Exp 10
Mana Potion - Exp 20
Greater Mana Potion - Exp 30
Fireball - Exp 40
Lightning - Exp 50
Frostbite - Exp 60
Ragnarok - Exp 1000
"""


def daves_shop(player: Player) -> None:
    purchase = ""
    while purchase != "Q":
        purchase = input("Purchase: ").title()
        if purchase == "Lesser Mana Potion" and player.exp >= 10:
            player.potions.append("Lesser Mana Potion")
            player.exp = (player.exp - 10)
        elif purchase == "Mana Potion" and player.exp >= 20:
            player.potions.append("Mana Potion")
            player.exp = (player.exp - 20)
        elif purchase == "Greater Mana Potion" and player.exp >= 30:
            player.potions.append("Greater Mana Potion")
            player.exp = (player.exp - 30)
        elif purchase == "Fireball" and player.exp >= 40:
            player.spells.append("Fireball")
            player.exp = (player.exp - 40)
        elif purchase == "Lightning" and player.exp >= 50:
            player.spells.append("Lightning")
            player.exp = (player.exp - 50)
        elif purchase == "Frostbite" and player.exp >= 60:
            player.spells.append("Frostbite")
            player.exp = (player.exp - 60)
        elif purchase == "Ragnarok" and player.exp >= 1000:
            player.spells.append("Ragnarok")
            player.exp = (player.exp - 1000)
        else:
            print("invalid transaction")
        print("\nGold:", player.gold)
        print("Exp:", player.exp)
        print("Potions:")
        for potion in player.potions:
            print(potion)
        print("\nWeapons:")
        for weapon in player.weapons:
            print(weapon)
        print("\nArmor:")
        for armors in player.armor:
            print(armors)
        print("\nSpells:")
        for spell in player.spells:
            print(spell)
        print("\n")


old_man_info = f"Welcome to the church of the Lord."

dtl1_info = "You approach this random flight of stairs that is decending downward in the earth.  From it a pink and purple haze seeps out.  Its light illmuminates the area around it in a magenta fog.  You take your first steps into the stair well and the hatch doors swing shut.\n\nYou can go to:\nLust R1."

dungeon_lust_r1 = "You enter a room with floors of stone.  It is dimly lit with the purple haze and you reach for the wall.  Upon touch your hand feels quite wet with the dampness of the walls extending to the humidity.\n\nYou can go to:\nLust R2"

dungeon_lust_r2 = "The halls now start to widen a bit futher ahead\n\nYou can go to:\nLust R1\nLust R3"

dungeon_lust_r3 = "You get to a crossroads with three possible entrances.  To the left you hear cackling.  To the right: silence.  Up in front, though, you feel immense power.\nYou can go to:\nLust R2\nLust R4\nLust R6\nLust R8"

dungeon_lust_r4 = "A room filled with mirrors and perfumes.\nYou can go to:\nLust R3\nLust R5"

dungeon_lust_r5 = "There is nothing but pillows here.\nYou can go to:\nLust R4"

dungeon_lust_r6 = "There is nothing here.\nYou can go to:\nLust R3\nLust R7"

dungeon_lust_r7 = "A wild mess of a room lays before you with clothes thrown about, trash scattered everywhere, and a single mattress on the floor.\nYou can go to:\nLust R6"

dungeon_lust_r8 = "A room in which you found a trusty sandwich.\nYou can go to:\nLust R3\nLust R9"

dungeon_lust_r9 = """You feel immense amount power coming from the door ahead of you.\nYou can go to:\nLust R8\nLilith's Playroom"""

lilith_playroom = "A intresting room filled with lavish pillows, a decarative mirror,and other such neccesties for the Queen of Lust.  You could probably live here if you wanted to due the niceness of the room.\n\nYou can go to:\nLust R9\nGluttony R1"

dungeon_glut_r1 = "As you step down futher into the dungeon you smell rancid meat filling the lime green walls of stone.\nYou can go to:\nGluttony R6\nGluttony R2"

dungeon_glut_r2 = "A long corridor stands before you with rotten sausage links pinned to the green wall.\nYou can go to:\nGluttony R1\nGluttony R3"

dungeon_glut_r3 = "As you walk in through the hallway you come into a room with a butcher's block in the center of the room with a lot of questionable meat in boxes and on nearby tables.\nYou can go to:\nGluttony R2"

dungeon_glut_r4 = "A dinning table with food lays before you. \nYou can go to:\nGluttony R6\nGluttony %5"

dungeon_glut_r5 = "In this room you found a wonderful plate of spaghett on a wonderful candle-lit table.\nYou can go to:\nGluttony R4"

dungeon_glut_r6 = "A small room lays before you with the same rancid smell as the first room, but it has more of a fruity smell compared to the rest of the rooms (which have a more meaty smell).  There are three doors.\nYou can go to:\nGluttony R1\nGluttony R4\nGluttony R7"

dungeon_glut_r7 = "As you open the door up you see and swarm of flies eating lots of rotten fruit.\nYou can go to:\nGluttony R6\nGluttony R8"

dungeon_glut_r8 = "Along this hallway you spot several old paintings depicting fruit and various other foods, with yet still the smell of rancid fruit getting closer. \nYou can go to:\nGluttony R7\nGluttony R10\nGluttony R13"

dungeon_glut_r9 = "A thanksgiving themed dining room lays before you, decorated with turkeys, pilgrims, and familes holding hands.\nYou can go to:\nGluttony R10"

dungeon_glut_r10 = "You enter a long and narrow hallway.  Lining the walls are rotten food of various kindsr.  They range from fruit to meat and even milk? \nYou can go to:\nGluttony R8\nGluttony R9\nGluttony R11"

dungeon_glut_r11 = "As you head down this narrow hallway you see the body of the large locust that you slayed.  It is at least 8ft long in size and had glowing red eyes..  You can go to:\nGluttony R10"

dungeon_glut_r12 = "A chinese themed dining room lays before you\nYou can go to:\nGluttony R13"

dungeon_glut_r13 = "This is the room where you found a nice and trusty fly swatter.  Funnily enough, you see several flies in this room.\nYou can go to:\nGluttony R8\nGluttony R12\nGluttony R14"

dungeon_glut_r14 = """As you proceed to the end a rather digusting and rancid smell is getting closer.\nYou can go to:\nGluttony R13\nBeelzebub's Feast"""

beelzebubs_feast = "A large dining hall fit for a king lays before you, although you don't see a delicious banquette.  Instead you see corpses of past humans who have challenged the Great king of Gluttony."


def is_valid_transition(succ1: Enemies, succ2: Enemies, inc: Enemies,
                        locust1: Enemies, locust2: Enemies, flies: Enemies,
                        flies2: Enemies, lilith: Enemies, beelzebub: Enemies,
                        player: Player, location: str, destination: str,
                        item_bools: ItemPickup, dead: Death) -> bool:
    if location == "Limbo":
        return (destination == "Old Town" or destination == "Cathedral"
                or destination == "Decent")
    elif location == "Old Town":
        return (destination == "Cathedral" or destination == "Decent"
                or destination == "Shop")
    elif location == "Shop":
        return (destination == "Bill" or destination == "Dave"
                or destination == "Old Town")
    elif location == "Dave":
        return (destination == "Bill" or destination == "Shop")
    elif location == "Bill":
        return (destination == "Dave" or destination == "Shop")
    elif location == "Old Man":
        return destination == "Cathedral" or destination == "Old Town"
    elif location == "Cathedral":
        return (destination == "Old Town" or destination == "Old Man"
                or destination == "Decent")
    elif location == "Decent":
        return destination == "Lust R1"
    elif location == "Lust R1":
        return destination == "Lust R2"
    elif location == "Lust R2":
        return destination == "Lust R3" or destination == "Lust R1" or destination == "Limbo"
    elif location == "Lust R3":
        return destination == "Lust R2" or destination == "Lust R4" or destination == "Lust R6" or destination == "Lust R8"
    elif location == "Lust R4":
        return destination == "Lust R5" or destination == "Lust R3" or destination == "Limbo"
    elif location == "Lust R5":
        return destination == "Lust R4"
    elif location == "Lust R6":
        return destination == "Lust R3" or destination == "Lust R7"
    elif location == "Lust R7":
        return destination == "Lust R6" or destination == "Limbo"
    elif location == "Lust R8":
        return destination == "Lust R9" or destination == "Lust R3"
    elif location == "Lust R9":
        return destination == "Lust R8" or destination == """Liliths Playroom"""
    elif location == """Liliths Playroom""":
        return destination == "Lust R9" or destination == "Gluttony R1" or destination == "Limbo"
    elif location == "Gluttony R1":
        return destination == "Gluttony R2" or destination == "Gluttony R6"
    elif location == "Gluttony R2":
        return destination == "Gluttony R1" or destination == "Gluttony R3" or destination == "Limbo"
    elif location == "Gluttony R3":
        return destination == "Gluttony R2"
    elif location == "Gluttony R4":
        return destination == "Gluttony R5" or destination == "Gluttony R6" or destination == "Limbo"
    elif location == "Gluttony R5":
        return destination == "Gluttony R4"
    elif location == "Gluttony R6":
        return destination == "Gluttony R4" or destination == "Gluttony R6" or destination == "Gluttony R7"
    elif location == "Gluttony R7":
        return destination == "Gluttony R8" or destination == "Gluttony R6" or destination == "Limbo"
    elif location == "Gluttony R8":
        return destination == "Gluttony R7" or destination == "Gluttony R13" or destination == "Gluttony R10" or destination == "Gluttony 7"
    elif location == "Gluttony R9":
        return destination == "Gluttony R10"
    elif location == "Gluttony R10":
        return destination == "Gluttony R11" or destination == "Gluttony R9" or destination == "Gluttony R8"
    elif location == "Gluttony R11":
        return destination == "Gluttony R10" or destination == "Limbo"
    elif location == "Gluttony R12":
        return destination == "Gluttony R13"
    elif location == "Gluttony R13":
        return destination == "Gluttony R14" or destination == "Gluttony R8" or destination == "Gluttony R12"
    elif location == "Gluttony R14":
        return destination == "Gluttony R13" or destination == """Beelzebubs Feast""" or destination == "Limbo"
    elif location == """Beelsebubs Feast""":
        if destination == "Limbo":
            player_death(succ1, succ2, inc, locust1, locust2, flies, flies2,
                         lilith, beelzebub, player, item_bools, dead)
        return destination == "Limbo" or destination == "Gluttony R14"
    return False


def print_info(player_name: str, location: str, player: Player, dead: Death,
               item_bools: ItemPickup, succ1: Enemies, succ2: Enemies,
               inc: Enemies, locust1: Enemies, locust2: Enemies,
               flies: Enemies, flies2: Enemies, lilith: Enemies,
               beelzebub: Enemies) -> None:
    if location == "Limbo":
        print(limbo_info)
    elif location == "Old Town":
        print(old_town_info)
    elif location == "Cathedral":
        print(cathedral_info)
    elif location == "Bill":
        print(bill_info)
        bills_shop(player)
    elif location == "Dave":
        print(dave_info)
        daves_shop(player)
    elif location == "Shop":
        print(shop_info)
    elif location == "Old Man":
        level_up(player)
    elif location == "Decent":
        print(dtl1_info)
    elif location == "Lust R1":
        print(dungeon_lust_r1)
    elif location == "Lust R2":
        if dead.succ1 == False:
            play_round(player_name, location, player, item_bools, dead, succ1)
        if player.player_health > 0:
            print(dungeon_lust_r2)
    elif location == "Lust R3":
        print(dungeon_lust_r3)
    elif location == "Lust R4":
        if dead.inc == False:
            play_round(player_name, location, player, item_bools, dead, inc)
        if player.player_health > 0:
            print(dungeon_lust_r4)
    elif location == "Lust R5":
        if item_bools.lr5 == False:
            item_bools.lr5 = item_pickup(player, item_bools, "Lust R5")
        for potion in player.potions:
            print(potion)
        print(dungeon_lust_r5)
    elif location == "Lust R6":
        print(dungeon_lust_r6)
    elif location == "Lust R7":
        if dead.succ2 == False:
            play_round(player_name, location, player, item_bools, dead, succ2)
        if player.player_health > 0:
            print(dungeon_lust_r7)
    elif location == "Lust R8":
        if item_bools.lr8 == False:
            item_bools.lr8 = item_pickup(player, item_bools, "Lust R8")
        print(dungeon_lust_r8)
    elif location == "Lust R9":
        print(dungeon_lust_r9)
    elif location == """Liliths Playroom""":
        if dead.lilcounter < 1:
            play_round(player_name, location, player, item_bools, dead, lilith)
            dead.lilcounter = (dead.lilcounter + 1)
        if player.player_health > 0:
            print(lilith_playroom)
    elif location == "Gluttony R1":
        print(dungeon_glut_r1)
    elif location == "Gluttony R2":
        if dead.locust1 == False:
            play_round(player_name, location, player, item_bools, dead, flies)
        if player.player_health > 0:
            print(dungeon_glut_r2)
    elif location == "Gluttony R3":
        if item_bools.gr3 == False:
            item_bools.gr3 = item_pickup(player, item_bools, "Gluttony R3")
        print(dungeon_glut_r3)
    elif location == "Gluttony R4":
        if item_bools.gr4 == False:
            item_bools.gr4 = item_pickup(player, item_bools, "Gluttony R4")
        print(dungeon_glut_r4)
    elif location == "Gluttony R5":
        if item_bools.gr5 == False:
            item_bools.gr5 = item_pickup(player, item_bools, "Gluttony R5")
        print(dungeon_glut_r5)
    elif location == "Gluttony R6":
        print(dungeon_glut_r6)
    elif location == "Gluttony R7":
        if dead.flies == False:
            play_round(player_name, location, player, item_bools, dead, flies)
        if player.player_health > 0:
            print(dungeon_glut_r7)
    elif location == "Gluttony R8":
        print(dungeon_glut_r8)
    elif location == "Gluttony R9":
        if item_bools.gr9 == False:
            item_bools.gr9 = item_pickup(player, item_bools, "Gluttony R9")
        print(dungeon_glut_r9)
    elif location == "Gluttony R10":
        print(dungeon_glut_r10)
    elif location == "Gluttony R11":
        if dead.flies2 == False:
            play_round(player_name, location, player, item_bools, dead, flies2)
        if player.player_health > 0:
            print(dungeon_glut_r11)
    elif location == "Gluttony R12":
        if item_bools.gr12 == False:
            item_bools.gr12 = item_pickup(player, item_bools, "Gluttony R12")
        print(dungeon_glut_r12)
    elif location == "Gluttony 13":
        if item_bools.gr13 == False:
            item_bools.gr13 = item_pickup(player, item_bools, "Gluttony R13")
        print(dungeon_glut_r13)
    elif location == "Gluttony R14":
        if dead.locust2 == False:
            play_round(player_name, location, player, item_bools, dead,
                       locust2)
        if player.player_health > 0:
            print(dungeon_glut_r14)
    elif location == """Beelzebubs Feast""":
        if dead.beecounter < 1:
            play_round(player_name, location, player, item_bools, dead,
                       beelzebub)
            dead.beecounter = (dead.beecounter + 1)
        if player.player_health > 0:
            print(beelzebubs_feast)


def input_destination_or_q(succ1: Enemies, succ2: Enemies, inc: Enemies,
                           locust1: Enemies, locust2: Enemies, flies: Enemies,
                           flies2: Enemies, lilith: Enemies,
                           beelzebub: Enemies, player_name: str,
                           player: Player, location: str, item_bools,
                           dead) -> str:
    if player.player_health <= 0:
        player_death(succ1, succ2, inc, locust1, locust2, flies, flies2,
                     lilith, beelzebub, player, item_bools, dead)
        restart = input(
            f"What will {player_name} do now?  Go back to limbo [Limbo] or quit[q]?\n>"
        )
        if restart == "q":
            location = "Q"
        elif restart == "Limbo":
            location = "Limbo"
            print(limbo_info)
        else:
            print("invaild input")
    while True:
        print(f"Where would {player_name} like to go? [q to quit]")
        destination = input("> ").title()
        if destination == "Q" or is_valid_transition(
                succ1, succ2, inc, locust1, locust2, flies, flies2, lilith,
                beelzebub, player, location, destination, item_bools, dead):
            return destination
        else:
            print(
                f"{player_name} cannot go to {destination.title()} from {location.title()}."
            )


def play_round(player_name: str, location: str, player: Player,
               item_bools: ItemPickup, dead: Death, enemy: Enemies) -> str:
    while enemy.health > 0 and player.player_health > 0:
        print(f"{player_name} health:", player.player_health)
        print(f"{enemy.name} health:", enemy.health)
        print(f"{enemy.name} blocks your path!")
        action = input(
            f"What will {player_name} do?\nAttack\nMagic\nItem\n> ").title()
        if action == "Attack" or action == "":
            for weapon in player.weapons:
                print(weapon)
            attack1 = input("> ").title()
            if attack1 == "":
                enemy.health = (enemy.health - player.punch)
            elif attack1 == "Legendary 24 In. Sub":
                enemy.health = enemy.health - 1
            if attack1 == "Iron Sword" and "Iron Sword" in player.weapons:
                enemy.health = enemy.health - random.randint(10, 30)
            elif attack1 == "Steel Sword" and "Steel Sword" in player.weapons:
                enemy.health = enemy.health - random.randint(20, 40)
            elif attack1 == "Mythril Sword" and "Mythril Sword" in player.weapons:
                enemy.health = enemy.health - random.randint(30, 50)
            elif attack1 == "Fly Swatter" and "Fly Swatter" in player.weapons:
                if enemy.name == "Hoard of Flies" or enemy.name == "Beelzebub":
                    enemy.health = enemy.health - random.randint(35, 55)
                else:
                    enemy.health = enemy.health - random.randint(15, 25)
            else:
                print("Invalid attack")
        elif action == "Magic":
            for spell in player.spells:
                print(spell)
            magic = input("> ").title()
            if magic == "Fireball" and player.mana >= 5 and "Fireball" in player.spells:
                print(f"{player_name} cast Fireball!")
                enemy.health = enemy.health - random.randint(20, 35)
            elif magic == "Lightning" and player.mana >= 10 and "Lightning" in player.spells:
                print(f"{player_name} cast Lightning!")
                enemy.health = enemy.health - random.randint(35, 45)
            elif magic == "Frostbite" and player.mana >= 20 and "Frostbite" in player.spells:
                print(f"{player_name} cast Frostbite!")
                enemy.health = enemy.health - random.randint(45, 55)
            elif magic == "Ragnarok" and player.mana >= 50 and "Ragnarok" in player.spells:
                print("You cast Ragnarok!")
                enemy.health = enemy.health * 0
            elif magic == "Dia" and player.mana >= 10 and "Dia" in player.spells:
                print("You healed. + 30 HP")
                player.player_health = (player.player_health + 30)
                if player.player_health > player.player_health_capacity:
                    player.player_health = player.player_health_capacity
            else:
                print(f"{player_name} can't cast {magic}")
        elif action == "Item":
            for potion in player.potions:
                print(potion)
            use = input("What will you use?").title
            if use == "Lesser Healing Potion":
                player.potions.remove("Lesser Healing Potion")
                player.player_health = player.player_health + 25
                if player.player_health > player.player_health_capacity:
                    player.player_health = player.player_health_capacity
                print("You healed 25 HP")
            elif use == "Healing Potion":
                player.potions.remove("Healing Potion")
                player.player_health = player.player_health + 55
                if player.player_health > player.player_health_capacity:
                    player.player_health = player.player_health_capacity
                print("You healed 55 hp.")
            elif use == "Greater Healing Potion":
                player.potions.remove("Greater Healing Potion")
                player.player_health = player.player_health_capacity
                print("HP fully restored.")
            elif use == "Lesser Mana Potion":
                player.potions.remove("Lesser Mana Potion")
                player.mana = player.mana + 10
                if player.mana > player.mana_capacity:
                    player.mana = player.mana_capacity
                print("You restored 10 mana.")
            elif use == "Mana Potion":
                player.potions.remove("Mana Potion")
                player.mana = player.mana + 30
                if player.mana > player.mana_capacity:
                    player.mana = player.mana_capacity
                print("You restored 30 mana.")
            elif use == "Greater Mana Potion":
                player.potions.remove("Greater Mana Potion")
                player.mana = player.mana_capacity
                print("You restored all of your mana.")
            elif use == "Mysterious Potion":
                chance = random.randint(0, 100)
                if chance < 1:
                    player.exp = player.exp + 2000
                    print("You gained 2000 EXP")
                elif chance < 51:
                    player.player_health_capacity = player.player_health_capacity + 30
                    player.player_health = player.player_health + 30
                    print("You gained 30 HP")
                elif chance > 50:
                    player.player_health = player.player_health - 40
                    print("You lost 40 HP")
            else:
                print(f"{player_name} cant use {use} here!")
        else:
            print(f"{player_name} can't", action, "the enemy!!")
        if enemy.health > 0:
            print(f"{enemy.name} {enemy.attack}!")
            player.player_health = (player.player_health - enemy.damage)
            print(f"It deals {enemy.damage}")
        elif enemy.health <= 0:
            print(f"{enemy.name} has died")
        if player.player_health <= 0:
            print(f"{player_name} died.")
            location = "Limbo"
        elif enemy.health <= 0:
            player.exp = player.exp + enemy.exp
            player.gold = player.gold + enemy.gold
            print("Exp:", player.exp)
            print("Gold:", player.gold)
            if enemy.name == "Lilith":
                player.potions.append("Greater Healing Potion")
            elif enemy.name == "Beelzebub":
                player.exp = player.exp + 1000
    return location


def player_death(succ1: Enemies, succ2: Enemies, inc: Enemies,
                 locust1: Enemies, locust2: Enemies, flies: Enemies,
                 flies2: Enemies, lilith: Enemies, beelzebub: Enemies,
                 player: Player, item_bools: ItemPickup, dead: Death) -> None:
    succ1.health = 50
    succ2.health = 60
    inc.health = 55
    locust1.health = 85
    locust2.health = 95
    flies.health = 100
    flies2.health = 300
    lilith.health = 100
    beelzebub.health = 200
    item_bools.lr5 = False
    item_bools.lr8 = False
    item_bools.gr3 = False
    item_bools.gr4 = False
    item_bools.gr5 = False
    item_bools.gr9 = False
    item_bools.gr12 = False
    item_bools.gr13 = False
    dead.succ1 = False
    dead.succ2 = False
    dead.inc = False
    dead.locust1 = False
    dead.locust2 = False
    dead.flies = False
    dead.flies2 = False
    dead.lilcounter = 0
    dead.beecounter = 0
    player.player_health = player.player_health_capacity


def level_up(player: Player) -> None:
    levelup = ""
    while levelup != "No":
        levelup = input(
            "Would you like to gain the Lords knowledge?  {Yes} or {No}\n> ")
        if player.exp > 50 and levelup == "Yes":
            player.exp = player.exp - 50
            player.player_health_capacity = (player.player_health_capacity +
                                             50)
            player.mana_capacity = (player.mana_capacity + 10)
            player.punch = (player.punch + 5)
            player.player_health = player.player_health_capacity
            print(player.player_health_capacity)
            print(player.mana_capacity)
        elif levelup == "No":
            print(
                "Ok child, come again when you seek enlightment.\nYou can go to:\nCathedral"
            )
        else:
            print("Sorry Child, come again when you have more knowledge.")


def main() -> None:
    dead = Death(False, False, False, False, False, False, False, 0, 0)
    item_bools = ItemPickup(False, False, False, False, False, False, False,
                            False)
    succ1 = Enemies("The Blonde Succubus", 50, random.randint(15, 25),
                    random.randint(25, 35), "claws you",
                    random.randint(10, 15))
    inc = Enemies("The Incubus", 55, random.randint(25, 30),
                  random.randint(25, 35), "claws you", random.randint(10, 15))
    succ2 = Enemies("The Ginger Succubus", 60, random.randint(15, 25),
                    random.randint(25, 35), "claws you",
                    random.randint(10, 15))
    locust1 = Enemies("The Green Locust", 85, random.randint(35, 45),
                      random.randint(45, 55), "mauls you with its mandibles",
                      random.randint(12, 18))
    locust2 = Enemies("The Brown Locust", 95, random.randint(35, 45),
                      random.randint(45, 55), "mauls you with its mandibles",
                      random.randint(20, 30))
    flies = Enemies("The hoard of Flies", 100, random.randint(55, 60),
                    random.randint(60, 70), "forms a fist and punches you",
                    random.randint(14, 19))
    flies2 = Enemies("The Hoard of Flies", 300, random.randint(55, 60),
                     random.randint(60, 70),
                     "forms a hammer and grand-slam smashes you",
                     random.randint(14, 19))
    lilith = Enemies("Lilith", 100, random.randint(100, 200),
                     random.randint(200, 300), "drains your soul",
                     random.randint(25, 30))
    beelzebub = Enemies(
        "Beelzebub", 200, random.randint(200, 250), random.randint(400, 600),
        "spits stomach acid that melts your skin and smells so awful you gag",
        random.randint(100, 150))
    player = Player(50, 50, 10, 20, [], ["Iron Sword"], [],
                    ["Dia"], 10, 10, 5)
    location = "Limbo"
    player_name = playername()
    print("Welcome", player_name)
    while True:

        print_info(player_name, location, player, dead, item_bools, succ1,
                   succ2, inc, locust1, locust2, flies, flies2, lilith,
                   beelzebub)
        destination = input_destination_or_q(succ1, succ2, inc, locust1,
                                             locust2, flies, flies2, lilith,
                                             beelzebub, player_name, player,
                                             location, item_bools, dead)
        if destination == "Q":
            break
        else:
            location = destination


if __name__ == "__main__":
    main()
