import random

# Create 3 different dictionaries with stuffie powers, names, attack, health etc.

# AYDINTOPIA

aydin_s1 = {"name": "mr turtle widdles",
            "health": 100,
            "damage": 70,
            "power": "psi"
            }

aydin_s2 = {"name": "cookie",
            "health": 90,
            "damage": 80,
            "power": "feline"
            }

aydin_s3 = {"name": "sandwich",
            "health": 100,
            "damage": 75,
            "power": "feline"
            }

# __________________________B_O_R_D_E_R_____________________________
# CHANTELLE


chantelle_s1 = {"name": "moonbeam",
                "health": 100,
                "damage": 70,
                "power": "spirtual"
                }

chantelle_s2 = {"name": "twinkle",
                "health": 105,
                "damage": 65,
                "power": "beauty"
                }

chantelle_s3 = {"name": "octi",
                "health": 100,
                "damage": 70,
                "power": "ink"
                }

# --------------NURSE BRIE'S STUFFIEMON CLINIC-----#

brie_s1 = {"name": "Dorito",
           "health": 150,
           "damage": 50,
           "power": "feline",
           "second_power": "cuteness"
           }

# ---------------------UNIVERSAL BORDER-------------------
bries_den = []

# Player2 stuffymon is a list of dictionaries that belong to Chantelle's stuffiemons
player2_stuffymon = [chantelle_s1, chantelle_s2, chantelle_s3]

# Player1 stuffymon is a list of dictionaries that belong to Aydin's stuffiemons
player1_stuffymon = [aydin_s1, aydin_s2, aydin_s3]

active_battle = []

nextStuffiemon = ""

print("Are you ready for a duel?!?!?")
# Create an input that asks what number stuffie to play first, 1, 2, 3
# Player1
print()
p = input("which stuffymon do you choose? (not ones that dont exist)")
print()

if (p == "1"):
    print(player1_stuffymon[0]["name"] + " is ready to duel!")
    player1_stuffymon.remove(aydin_s1)
    active_battle.append(aydin_s1)

elif (p == "2"):
    print(player1_stuffymon[1]["name"] + " is ready to duel!")
    player1_stuffymon.remove(aydin_s2)
    active_battle.append(aydin_s2)

else:
    print(player1_stuffymon[2]["name"] + " is ready to duel!")
    player1_stuffymon.remove(aydin_s3)
    active_battle.append(aydin_s3)

print()
# Player2
player_two = input("Which stuffymon would like to play and is ready?!good luck!! ")

if (player_two == "1"):
    print(player2_stuffymon[0]["name"] + " is ready to duel!")
    player2_stuffymon.remove(chantelle_s1)
    active_battle.append(chantelle_s1)

elif (player_two == "2"):
    print(player2_stuffymon[1]["name"] + " is ready to duel!")
    player2_stuffymon.remove(chantelle_s2)
    active_battle.append(chantelle_s2)

else:
    print(player2_stuffymon[2]["name"] + " is ready to duel!")
    player2_stuffymon.remove(chantelle_s3)
    active_battle.append(chantelle_s3)

# aydin, chantelle
while ((active_battle[0]["health"] > 0) and (active_battle[1]["health"] > 0)):

    print()
    # active_battle = [aydin_s1, chantelle_s2]
    aydin_damage = random.randint(0, (active_battle[0]["damage"]))
    print(active_battle[0]["name"] + " uses this much damage: ", aydin_damage)

    active_battle[1]["health"] = active_battle[1]["health"] - aydin_damage

    if (active_battle[1]["health"] < 0):
        active_battle[1]["health"] = 0

    print(active_battle[1]["name"] + " has this much health left: ", (active_battle[1]["health"]))

    if (active_battle[1]["health"] == 0):
        print("Nurse Brie will accept this stuffiemon!")
        nextStuffiemon = "Chantelle"
        bries_den.append(active_battle[1])
        active_battle.remove(active_battle[1])
        break

    print()

    chantelle_damage = random.randint(0, (active_battle[0]["damage"]))
    print(active_battle[1]["name"] + " uses this much damage: ", chantelle_damage)
    active_battle[0]["health"] = (active_battle[0]["health"] - chantelle_damage)
    if (active_battle[0]["health"] < 0):
        active_battle[0]["health"] = 0
    print(active_battle[0]["name"] + " has this much health left: ", (active_battle[0]["health"]))

    if (active_battle[0]["health"] == 0):
        print("Nurse Brie will accept this stuffiemon!")
        nextStuffiemon = "Aydin"
        bries_den.append(active_battle[0])
        active_battle.remove(active_battle[0])
        break

# if nextStuffiemon is equal to Aydin,  create an input that asks aydin which pokemon does he want to play next from 1-2

# elif nextStuffiemon is equal to Chantelle, create an input that asks Chantelle which pokemon does she want to play next from 1-2
print()
print("Since you lost the duel pick another stuffiemon to play! (not ones that dont exist)")
if (nextStuffiemon == "Aydin"):
    q = input("which stuffymon do you choose? (not the one you already chose)")
elif (nextStuffiemon == "Chantelle"):
    c = input("Which pokemon would you want to choose? ")

