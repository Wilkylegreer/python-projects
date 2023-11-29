from random import random, randint
import time

print('Type "help" for a list of commands\n')


class normal_enemy:
    enemy_count = 0
    enemies = []

    def __init__(self, name, health, damage_minmax, description):
        self.name = name
        self.health = health
        self.damage_minmax = damage_minmax
        self.description = description
        __class__.enemies.append(self)
        normal_enemy.enemy_count += 1

    def observe(self):
        print("\n\nIt's a " + self.name, "with " + str(self.health), "health, an accuracy of " + str(self.damage_minmax[0]), "and " + str(self.damage_minmax[1]), "strength!\n",
              "Description:", self.description)
        return


dummy = normal_enemy("Dummy", 10, damage_minmax=(0, 0),
                     description="It's a dummy, dummy.")
skeleton = normal_enemy("Skeleton", 25, damage_minmax=(3, 5), description="A bony creature, usually found wondering about in the woods or during the night. They aren't very strong, \
but their ability to stand is impressive, considering their significant lack of muscle tissue")
zombie = normal_enemy("Zombie", 40, damage_minmax=(
    1, 14), description="A dead creature risen from the land of the forgotten. It is extremely unpredictable seeing as their brain has rot quite significantly")

command_list = ['atk', 'attack', 'fight', 'pass', 'sleep',
                'help', 'observe', 'block', 'defend', 'status']
help_text = "\nList of commands:\n\natk or attack: Attacks your opponent, dealing a random amount of damage\nfight: Enter a fight with a random opponent\npass or sleep: Pass your turn\nobserve: Observe your current opponent\nblock or defend: Halves your damage taken, but ends your turn. Always rounded down\nstatus: Displays your current health, as well as your opponent's\ndummy: dummy"

score = 0
enemy_hitpoints = 0
hitpoints = 100
maxhitpoints = 100
max_passes = 5
damage_minmax = 1, 10
misspercent = [5, 0]
misspercent[1] = misspercent[0]*12
in_fight = False


def status():
    global in_fight
    if hitpoints <= 0:
        in_fight = False
        print('\nYou lost\n')
        time.sleep(0.5)
        exit()
    print("\nYou have", hitpoints, "out of", maxhitpoints, "hp remaining")
    if in_fight == True:
        print("\nYour opponent has", enemy_hitpoints,
              "out of", active_enemy.health, "hp remaining")
    if u_input in command_list[9]:
        print("\nYour probability of missing is", misspercent[0], "out of 100. Your accuracy is",
              damage_minmax[0], "and you have", damage_minmax[1], "strength\n\nYour current score is", score)

# Preparations and pre-maingame events above this
# Main gameplay loop bellow this


while True:
    pass_counter = 0
    while in_fight == False:
        u_input = input('What would you like to do? >>> ').lower()
        if u_input in command_list[5] or u_input in command_list[9]:
            if u_input in command_list[9]:
                status()
            elif u_input in command_list[5]:
                print(help_text)
        else:
            if u_input in command_list[2] and in_fight == False:
                active_enemy = normal_enemy.enemies[randint(
                    1, normal_enemy.enemy_count - 1)]
                print('You encounter a wild', active_enemy.name + '!')
                in_fight = True
            elif in_fight == False and u_input not in command_list:
                if u_input == 'dummy':
                    active_enemy = normal_enemy.enemies[0]
                    in_fight = True
                else:
                    print(
                        'unknown command. Be sure to type "help" into the console for a list of commands')
            elif in_fight == False:
                print("You can't", u_input, "while outside of battle")

    pass_dialogue = ["\nI'd recommend doing something while a " + active_enemy.name + ' is trying to murder you, but sure',
                     "\nReally? Look. I won't stop you, but I am really questioning your strategical abilities right now...",
                     "\nHave you considered attacking by any chance? Hell, you could just block dude. Did you even know that was a mechanic? Have you even read the help page?",
                     "\n Here, since you just won't get the hint: " + '\n ' + help_text + '\n '
                     "\n \n Ok. That's it. I'm not letting you pass any more \n "
                     ""]

    if in_fight == True:
        enemy_hitpoints = active_enemy.health

    while in_fight == True:
        if active_enemy == normal_enemy.enemies[0]:
            print('dummy')
        turn_end = False
        is_blocking = False
        damage_dealt = 0
        damage_taken = 0
        u_input = input("What would you like to do? >>> ").lower()
        if u_input in command_list:
            if u_input in command_list[0:2]:
                turn_end = True
                damage_dealt = randint(damage_minmax[0], damage_minmax[1])
                if randint(1, 100) <= misspercent[0]:
                    print('\nYou missed!')
                else:
                    print('\nYou dealt ' + str(damage_dealt), 'damage!')
                    enemy_hitpoints -= damage_dealt
            if u_input in command_list[5]:
                print(help_text)
            if u_input in command_list[3:5] and pass_counter < max_passes - 1:
                print(pass_dialogue[pass_counter])
                pass_counter += 1
                turn_end = True
            elif u_input in command_list[3:5]:
                print('no.')
            if u_input in command_list[6]:
                active_enemy.observe()
            if u_input in command_list[7:9]:
                is_blocking = True
                turn_end = True
            if u_input in command_list[9]:
                status()
        else:
            print(
                'unknown command. Be sure to type "help" into the console for a list of commands')
        if turn_end == True:
            if enemy_hitpoints <= 0:
                print("\nVictory!\n")
                score += 1
                print('You return to your adventurey duties',
                      '\n\ntype "help" into the console for a list of commands')
                in_fight = False
                active_enemy = ""
            else:
                damage_taken = randint(
                    active_enemy.damage_minmax[0], active_enemy.damage_minmax[1])
                print('\nYour turn has ended\n')
                if is_blocking == True:
                    damage_taken /= 2
                    print('\nYou blocked half of the dealt damage!\n')
                print(active_enemy.name, "dealt", int(damage_taken), "damage!")
                hitpoints -= int(damage_taken)
                status()
