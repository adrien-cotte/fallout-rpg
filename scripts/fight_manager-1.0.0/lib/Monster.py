#!/usr/bin/env ipython

import sys
from argparse import ArgumentParser
import json
from random import randint
from time import sleep
from math import ceil

class Monster:

    """ Contructor """
    def __init__(self, monster_json):
        with open(monster_json) as fp:
            data = json.load(fp)
        self._name = data['name']
        self._hp = data['hp']
        self._eyes = 5
        self._head = 15
        self._body_l = 25
        self._body_r = 30
        self._arm_l = 20
        self._arm_r = 20
        self._crotch = 10
        self._leg_l = 20
        self._leg_r = 20
        self._ammo = data['weapon']['loader']
        self._data = data

    """ Display functions """
    def displayHeader(self):
        print("\n== " + self._name + " ==")

    def displayState(self):
        print("\n== State " + self.getState() + " ==")

    def displayHealth(self):
        if self._hp < self._data['hp']:
            sys.stdout.write("\033[93m")
            if self._hp <= 0:
                sys.stdout.write("\033[91m")
        print("\n== Health [" + str(self._hp) + "/" + str(self._data['hp']) + "] ==")
        sys.stdout.write("\033[0m")
        if self._eyes < 5:
            sys.stdout.write("\033[93m")
            if self._eyes <= 0:
                sys.stdout.write("\033[91m")
        print("Eyes          [" + str(self._eyes) + "/5]")
        sys.stdout.write("\033[0m")
        if self._head < 15:
            sys.stdout.write("\033[93m")
            if self._head <= 0:
                sys.stdout.write("\033[91m")
        print("Head         [" + str(self._head) + "/15]")
        sys.stdout.write("\033[0m")
        if self._body_r < 30 or self._body_l < 25:
            sys.stdout.write("\033[93m")
            if self._body_r <= 0 or self._body_l <= 0:
                sys.stdout.write("\033[91m")
        print("Body     [" + str(self._body_r) + "/30] [" + str(self._body_l) + "/25]")
        sys.stdout.write("\033[0m")
        if self._arm_r < 20 or self._arm_l < 20:
            sys.stdout.write("\033[93m")
            if self._arm_r <= 0 or self._arm_l <= 0:
                sys.stdout.write("\033[91m")
        print("Arms     [" + str(self._arm_r) + "/20] [" + str(self._arm_l) + "/20]")
        sys.stdout.write("\033[0m")
        if self._crotch < 10 :
            sys.stdout.write("\033[93m")
            if self._crotch <= 0:
                sys.stdout.write("\033[91m")
        print("Crotch       [" + str(self._crotch) + "/10]")
        sys.stdout.write("\033[0m")
        if self._leg_r < 20 or self._leg_l < 20:
            sys.stdout.write("\033[93m")
            if self._leg_r <= 0 or self._leg_l <= 0:
                sys.stdout.write("\033[91m")
        print("Legs     [" + str(self._leg_r) + "/20] [" + str(self._leg_l) + "/20]")
        sys.stdout.write("\033[0m")

    def displayStats(self):
        print("\n== Stats (summary) ==")
        str_ac = "CA [" + str(self._data['ac'] + self._data['armor']['ac']) + "]"
        str_moral = "MORAL [" + str(self._data['moral']) + "]"
        str_ap = "AP [" + str(self._data['ap']) + "]"
        str_att = "ATT [" + str(self._data['att']) + " %]"
        str_dist = "DIST [" + str(self._data['distance']) + " m]"
        str_melee = "MELEE [" + str(self._data['melee']) + "]"
        print(str_ac + " | " + str_moral + " | " + str_ap + " | " + str_melee + " | " + str_att + " | " + str_dist)

    def displayWeapon(self):
        print("\n== Weapon ==")
        weapon = self._data['weapon']
        print(weapon['name'] +" (" + str(weapon['ap']) + "/" + str(weapon['spe_ap']) + ") - [" + str(self._ammo) + "/" + str(weapon['loader']) + "] -> " + str(weapon['distance']) + " m")

    def displayCommands(self):
        print('\n== Commands list ==')
        print("att(malus=0)        -- Returns attack score and damages applying malus")
        print("spe(malus=0)        -- Returns attack score and damages applying malus with special attack")
        print("att_<part>_<side>() -- Like att() but on <part> <side> with malus [att_eyes, att_arm_l etc ...]")
        print("dmg[_<type>](i)     -- Random part takes <type> i damages [dmg_l (laser), dmg_p (plasma) etc ...]")
        print("<part>[_<side>](i)  -- <side> <part> takes i damages [eyes, arm_l, leg_r etc ...]")
        print("reload()            -- Reload weapon")
        print("list()              -- List all commands")

    def display(self):
        self.displayHeader()
        self.displayState()
        self.displayHealth()
        self.displayStats()
        self.displayWeapon()
        self.displayCommands()

    """ Attack commands """
    def att(self, malus=0, part='random'):
        str_out = ""
        malus += int(self._data['armor']['malus'])
        # Use ammo
        if self._data['weapon']['ammo_per_shot'] > self._ammo:
            raw_input("Loader is empty, you should use reload() !")
            return
        self._ammo -= self._data['weapon']['ammo_per_shot']
        # Check part crit and malus
        crit = self._data['crit']
        if part == 'eyes':
            crit += 40
            malus += 40
        elif part == 'head':
            crit += 30
            malus += 30
        elif part =='crotch':
            crit += 40
            malus += 40
        elif part =='arm_r':
            crit += 20
            malus += 20
        elif part =='arm_l':
            crit += 20
            malus += 20
        elif part =='leg_r':
            crit += 10
            malus += 10
        elif part =='leg_l':
            crit += 10
            malus += 10
        elif part =='body_r':
            crit += 0
            malus += 0
        elif part =='body_l':
            crit += 0
            malus += 0
        # Check attack roll
        att = randint(1, 100)
        if att > (int(self._data['att']) - malus):
            str_out = "[FAILURE]"
            # Critical hit
            if att >= 97:
                str_out += " with [CRITICAL] effect"
        else:
            # Damages done
            dices = int(self._data['weapon']['dices'])
            dmg = int(self._data['weapon']['bonus'])
            for i in range(dices):
                dmg += randint(1, 6)
            str_out += "Deals [" + str(dmg) + "] (" + str(self._data['weapon']['dmg_type']) + ") damages on"
            # Select part
            if part == 'random':
                x = randint(1, 100)
            else:
                x = max
            if 1 <= x <= 5 or part == 'eyes':
                str_out += " [EYES]"
            elif 6 <= x <= 10 or part == 'crotch':
                str_out += " [CROTCH]"
            elif 11 <= x <= 25 or part == 'head':
                str_out += " [HEAD]"
            elif 26 <= x <= 31 or part == 'arm_r':
                str_out += " [RIGHT ARM]"
            elif 32 <= x <= 40 or part == 'arm_l':
                str_out += " [LEFT ARM]"
            elif 41 <= x <= 50 or part == 'leg_r':
                str_out += " [RIGHT LEG]"
            elif 51 <= x <= 60 or part == 'leg_l':
                str_out += " [LEFT LEG]"
            elif 61 <= x <= 80 or part == 'body_r':
                str_out += " [RIGHT BODY]"
            elif 81 <= x <= 100 or part == 'body_l':
                str_out += " [LEFT BODY]"
            # Critical hit
            if att <= crit:
                str_out += " with [CRITICAL] effect"
        raw_input(str_out + " !")

    def att_eyes(self, malus=0):
        self.att(malus, 'eyes')

    def att_head(self, malus=0):
        self.att(malus, 'head')

    def att_crotch(self, malus=0):
        self.att(malus, 'crotch')
    
    def att_arm_r(self, malus=0):
        self.att(malus, 'arm_r')
    
    def att_arm_l(self, malus=0):
        self.att(malus, 'arm_l')

    def att_leg_r(self, malus=0):
        self.att(malus, 'leg_r')
    
    def att_leg_l(self, malus=0):
        self.att(malus, 'leg_l')
    
    def att_body_r(self, malus=0):
        self.att(malus, 'body_r')
    
    def att_body_l(self, malus=0):
        self.att(malus, 'body_l')
    
    # Special attack
    def spe(self, malus=0, part='random'):
        # Check if special attack exists
        if self._data['weapon']['spe_ap'] == 0:
            raw_input("Your weapon doesn't have special attack!")
        str_out = ""
        malus += int(self._data['armor']['malus'])
        # Use ammo
        if self._data['weapon']['spe_ammo_per_shot'] > self._ammo:
            raw_input("You need more bullets, you should use reload() !")
            return
        self._ammo -= self._data['weapon']['spe_ammo_per_shot']
        # Check part crit and malus
        crit = self._data['crit']
        if part == 'eyes':
            crit += 40
            malus += 40
        elif part == 'head':
            crit += 30
            malus += 30
        elif part =='crotch':
            crit += 40
            malus += 40
        elif part =='arm_r':
            crit += 20
            malus += 20
        elif part =='arm_l':
            crit += 20
            malus += 20
        elif part =='leg_r':
            crit += 10
            malus += 10
        elif part =='leg_l':
            crit += 10
            malus += 10
        elif part =='body_r':
            crit += 0
            malus += 0
        elif part =='body_l':
            crit += 0
            malus += 0
        # Check attack roll
        att = randint(1, 100)
        if att > (int(self._data['att']) - malus):
            str_out = "[FAILURE]"
            # Critical hit
            if att >= 97:
                str_out += " with [CRITICAL] effect"
        else:
            # Damages done
            dices = int(self._data['weapon']['spe_dices'])
            dmg = int(self._data['weapon']['spe_bonus'])
            for i in range(dices):
                dmg += randint(1, 6)
            str_out += "Deals [" + str(dmg) + "] (" + str(self._data['weapon']['dmg_type']) + ") damages on"
            # Select part
            if part == 'random':
                x = randint(1, 100)
            else:
                x = max
            if 1 <= x <= 5 or part == 'eyes':
                str_out += " [EYES]"
            elif 6 <= x <= 10 or part == 'crotch':
                str_out += " [CROTCH]"
            elif 11 <= x <= 25 or part == 'head':
                str_out += " [HEAD]"
            elif 26 <= x <= 31 or part == 'arm_r':
                str_out += " [RIGHT ARM]"
            elif 32 <= x <= 40 or part == 'arm_l':
                str_out += " [LEFT ARM]"
            elif 41 <= x <= 50 or part == 'leg_r':
                str_out += " [RIGHT LEG]"
            elif 51 <= x <= 60 or part == 'leg_l':
                str_out += " [LEFT LEG]"
            elif 61 <= x <= 80 or part == 'body_r':
                str_out += " [RIGHT BODY]"
            elif 81 <= x <= 100 or part == 'body_l':
                str_out += " [LEFT BODY]"
            # Critical hit
            if att <= crit:
                str_out += " with [CRITICAL] effect"
        raw_input(str_out + " !")
        pass

    """ Damage taken command """
    def dmg(self, i, dmg_type='norm', part='random'):
        # Threshold
        if i <= int(self._data['armor']['thresh']):
            raw_input("Damages fully absorbed by armor !")
            return
        # Absorption
        absorption = int(ceil(i * (float(self._data['armor'][dmg_type]) / 100)))
        # Part
        area = int(self._data['armor']['area'])
        if part == 'random':
            x = randint(1, 100)
        else:
            x = max
        if (1 <= x <= 5) or (part == 'eyes'):
            if area == 2 :
                i -= absorption
                print("[" + str(absorption) + "] damages absorbed by armor !")
            self._eyes -= i
            part = "[EYES]"
        elif (6 <= x <= 10) or (part == 'crotch'):
            if area == 2 :
                i -= absorption
                print("[" + str(absorption) + "] damages absorbed by armor !")
            self._crotch -= i
            part = "[CROTCH]"
        elif (11 <= x <= 25) or (part == 'head'):
            if area == 2 :
                i -= absorption
                print("[" + str(absorption) + "] damages absorbed by armor !")
            self._head -= i
            part = "[HEAD]"
        elif (26 <= x <= 31) or (part == 'arm_r'):
            if area > 0 :
                i -= absorption
                print("[" + str(absorption) + "] damages absorbed by armor !")
            self._arm_r -= i
            part = "[RIGHT ARM]"
        elif (32 <= x <= 40) or (part == 'arm_l'):
            if area > 0 :
                i -= absorption
                print("[" + str(absorption) + "] damages absorbed by armor !")
            self._arm_l -= i
            part = "[LEFT ARM]"
        elif (41 <= x <= 50) or (part == 'leg_r'):
            if area == 2 :
                i -= absorption
                print("[" + str(absorption) + "] damages absorbed by armor !")
            self._leg_r -= i
            part = "[RIGHT LEG]"
        elif (51 <= x <= 60) or (part == 'leg_l'):
            if area == 2 :
                i -= absorption
                print("[" + str(absorption) + "] damages absorbed by armor !")
            self._leg_l -= i
            part = "[LEFT LEG]"
        elif (61 <= x <= 80) or (part == 'body_r'):
            if area > 0 :
                i -= absorption
                print("[" + str(absorption) + "] damages absorbed by armor !")
            self._body_r -= i
            part = "[RIGHT BODY]"
        elif (81 <= x <= 100) or (part == 'body_l'):
            if area > 0 :
                i -= absorption
                print("[" + str(absorption) + "] damages absorbed by armor !")
            self._body_l -= i
            part = "[LEFT BODY]"
        # HP
        self._hp -= i
        raw_input("[" + str(i) + "] damages taken in " + part + " !")

    def dmg_n(self, i):
        self.dmg(i, 'norm')
    
    def dmg_l(self, i):
        self.dmg(i, 'laser')
    
    def dmg_p(self, i):
        self.dmg(i, 'plasm')

    def eyes(self, i, dmg_type='norm'):
        self.dmg(i, dmg_type, 'eyes')

    def head(self, i, dmg_type='norm'):
        self.dmg(i, dmg_type, 'head')

    def body_l(self, i, dmg_type='norm'):
        self.dmg(i, dmg_type, 'body_l')

    def body_r(self, i, dmg_type='norm'):
        self.dmg(i, dmg_type, 'body_r')

    def arm_l(self, i, dmg_type='norm'):
        self.dmg(i, dmg_type, 'arm_l')

    def arm_r(self, i, dmg_type='norm'):
        self.dmg(i, dmg_type, 'arm_r')

    def crotch(self, i, dmg_type='norm'):
        self.dmg(i, dmg_type, 'crotch')

    def leg_l(self, i, dmg_type='norm'):
        self.dmg(i, dmg_type, 'leg_l')

    def leg_r(self, i, dmg_type='norm'):
        self.dmg(i, dmg_type, 'leg_r')

    """ Utils methods """
    def reload(self):
        self._ammo = self._data['weapon']['loader']
        raw_input("Weapon reloaded !")
    
    def list(self):
        ls = dir(Monster)
        ls.remove('__doc__')
        ls.remove('__init__')
        ls.remove('__module__')
        raw_input(ls)

    def isOk(self):
        b = self._hp > 0
        b = b and self._eyes > 0
        b = b and self._head > 0
        b = b and self._body_l > 0
        b = b and self._body_r > 0
        b = b and self._arm_l > 0
        b = b and self._arm_r > 0
        b = b and self._crotch > 0
        b = b and self._leg_l > 0
        b = b and self._leg_r > 0
        return b
    
    def getState(self):
        # [ O.K ]
        state = '[\033[92m O.K \033[0m]'
        # [ K.O ]
        if self._crotch <= 0 or self._arm_r <=0 or self._arm_l <= 0 or self._body_r <= 0 or self._body_l <= 0 or self._leg_r <= 0 or self._leg_l <= 0:
            state = '[\033[93m K.O \033[0m]'
        # [ x_x ]
        if self._hp <= 0 or self._eyes <= 0 or self._head <= 0:
            state = '[\033[91m x_x \033[0m]'
        return state
