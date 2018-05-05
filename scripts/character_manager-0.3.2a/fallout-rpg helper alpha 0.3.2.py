#coding:utf8

# This program is meant to help people to play fallout-rpg, a french
# pen and paper rpg http://www.fallout-rpg.com/
# Character function uses balanced rules of extraz93 http://dan.comb.free.fr/

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Copyright (C) 2016  Teemsis - teemsis@live.fr

from random import randint
from Tkinter import *
 
def character():  
    clear_character()
    global FO, EN, AG, PE, IN, CH, C
    try:
        FO = int(entry_fo.get())
        if FO < 1:
            FO = 1
            entry_fo.delete(0, END)
            entry_fo.insert(0, '1')
        if FO > 10:
            FO = 10
            entry_fo.delete(0, END)
            entry_fo.insert(0, '10')
    except:
        entry_fo.delete(0, END)
        entry_fo.insert(0, '1')
        FO = 1
    
    try:
        EN = int(entry_en.get())
        if EN < 1:
            EN = 1
            entry_en.delete(0, END)
            entry_en.insert(0, '1')
        if EN > 10:
            EN = 10
            entry_en.delete(0, END)
            entry_en.insert(0, '10')
    except:
        entry_en.delete(0, END)
        entry_en.insert(0, '1')
        EN = 1
    
    try:
        AG = int(entry_ag.get())
        if AG < 1:
            AG = 1
            entry_ag.delete(0, END)
            entry_ag.insert(0, '1')
        if AG > 10:
            AG = 10
            entry_ag.delete(0, END)
            entry_ag.insert(0, '10')
    except:
        entry_ag.delete(0, END)
        entry_ag.insert(0, '1')
        AG = 1
    
    try:
        PE = int(entry_pe.get())
        if PE < 1:
            PE = 1
            entry_pe.delete(0, END)
            entry_pe.insert(0, '1')
        if PE > 10:
            PE = 10
            entry_pe.delete(0, END)
            entry_pe.insert(0, '10')
    except:
        entry_pe.delete(0, END)
        entry_pe.insert(0, '1')
        PE = 1
    
    try:
        IN = int(entry_in.get())
        if IN < 1:
            IN = 1
            entry_in.delete(0, END)
            entry_in.insert(0, '1')
        if IN > 10:
            IN = 10
            entry_in.delete(0, END)
            entry_in.insert(0, '10')
    except:
        entry_in.delete(0, END)
        entry_in.insert(0, '1')
        IN = 1
    
    try:
        CH = int(entry_ch.get())
        if CH < 1:
            CH = 1
            entry_ch.delete(0, END)
            entry_ch.insert(0, '1')
        if CH > 10:
            CH = 10
            entry_ch.delete(0, END)
            entry_ch.insert(0, '10')
    except:
        entry_ch.delete(0, END)
        entry_ch.insert(0, '1')
        CH = 1
    
    try:
        C  = int(entry_c.get())
        if C < 1:
            C = 1
            entry_c.delete(0, END)
            entry_c.insert(0, '1')
        if C > 10:
            C = 10
            entry_c.delete(0, END)
            entry_c.insert(0, '10')
    except:
        entry_c.delete(0, END)
        entry_c.insert(0, '1')
        C = 1
    
    s =            'Force               ' + str(FO)
    s = s + '\n' + 'Endurance           ' + str(EN)
    s = s + '\n' + 'Agilité             ' + str(AG)
    s = s + '\n' + 'Perception          ' + str(PE)
    s = s + '\n' + 'Intelligence        ' + str(IN)
    s = s + '\n' + 'Charisme            ' + str(CH)
    s = s + '\n' + 'Chance              ' + str(C)
    text_character_primary.insert('1.0', s)
    text_character_primary.pack()    
    
    s =            'Chance critique             ' + str(C)
    s = s + '\n' + 'Chance critique de tir      ' + str(C)
    s = s + '\n' + 'Classe d\'armure             ' + str((AG+EN)/2)
    s = s + '\n' + 'Dégâts de melee             ' + str(max(FO/2, 1))
    s = s + '\n' + 'Force morale                ' + str((CH+IN)/2)
    pa = (5, 6, 6, 7, 7, 8, 8, 9, 9, 10)
    s = s + '\n' + 'Points d\'actions            ' + str(pa[AG-1])
    po = (2, 5, 5, 10, 10, 20, 20, 40, 40, 60)
    s = s + '\n' + 'Portée                      ' + str(po[PE-1]) + 'm'
    s = s + '\n' + 'Résistance aux poisons      ' + str(5*EN)
    s = s + '\n' + 'Résistance aux radiations   ' + str(2*EN)
    text_character_secondary.insert('1.0', s)
    text_character_secondary.pack() 
    
    s =            'Armes lég./moyennes     ' + str(5+(2*AG)+(2*PE)) + '%'
    s = s + '\n' + 'Armes lourdes           ' + str(5+(2*FO)+EN) + '%'
    s = s + '\n' + 'Corps à corps           ' + str(10 + 2*EN + 2*FO + AG) + '%'
    s = s + '\n' + 'Armes blanches          ' + str(10 + 2*EN + 2*AG + FO) + '%'
    s = s + '\n' + 'Lancer                  ' + str(10 + 2*AG + 2*PE) + '%'
    s = s + '\n' + 'Physique                ' + str(10 + 2*EN + 2*FO + AG) + '%'	
    s = s + '\n' + 'Perception              ' + str(10 + 4*PE + IN) + '%'
    s = s + '\n' + 'Manipulation            ' + str(5+2*AG+IN) + '%'
    s = s + '\n' + 'Soins                   ' + str(5+2*IN+AG) + '%'
    s = s + '\n' + 'Pièges                  ' + str(5+2*AG+PE) + '%'
    s = s + '\n' + 'Discrétion              ' + str(5+2*AG+2*C+IN) + '%'
    s = s + '\n' + 'Discours                ' + str(5+2*CH+IN) +'%'
    s = s + '\n' + 'Réflexion               ' + str(10+5*IN) + '%'
    s = s + '\n' + 'Pilotage                ' + str(5+2*AG+PE) + '%'	
    s = s + '\n' + 'Jeu                     ' + str(10+3*C) + '%'
    s = s + '\n' + 'Commerce                ' + str(5+CH+IN+C) + '%'
    s = s + '\n' + 'Vol                     ' + str(5+2*AG+C) + '%'	
    s = s + '\n' + 'Survie                  ' + str(5+EN+IN+PE) + '%'
    text_character_skills.insert('1.0', s)
    text_character_skills.pack()    
    
    s =            'Santé               ' + str(15+FO+2*EN)
    s = s + '\n' + 'Charge normale      ' + str(20 + 5*FO)
    s = s + '\n' + 'Charge temporaire   ' + str(20 + 10*FO)
    s = s + '\n' + 'Charge maximale     ' + str(20 + 15*FO)
    text_character_others.insert('1.0', s)
    text_character_others.pack()

def level_up():
    global IN, EN
    button_character_levelup.config(text='Passage de niveau (+'+str(10+IN)+'%)\n (+'+str(3+(EN/2))+'pv)')

def localisation():
	r = randint(1, 100)
	if (r <= 5):
		s = 'Yeux'
	elif (r <= 10):
		s = 'Entrejambes'
	elif (r <= 25):
		s = 'Tête/cou'
	elif (r <= 31):
		s = 'Bras droit'
	elif (r <= 40):
		s = 'Bras gauche'
	elif (r <= 50):
		s = 'Jambe droite'
	elif (r <= 60):
		s = 'Jambe gauche'
	elif (r <= 80):
		s = 'Torse droit'
	else:
		s = 'Torse gauche'
	s = s + '\n'
	text_dices.insert('1.0', s)
	text_dices.pack()

def roll6():
	text_dices.insert('1.0', str(randint(1, 6))+'\n')

def roll100():
	text_dices.insert('1.0', str(randint(1, 100))+'\n')

def clear_dices():
	text_dices.delete('1.0', END)

def clear_character():
    button_character_levelup.config(text='Passage de niveau')
    text_character_primary.delete('1.0', END)
    text_character_secondary.delete('1.0', END)
    text_character_skills.delete('1.0', END)
    text_character_others.delete('1.0', END)

###############################################################################
# Initialization                                                              #
###############################################################################

FO = 1
EN = 1
AG = 1
PE = 1
IN = 1
CH = 1
C  = 1

###############################################################################
# Title bar                                                                   #
###############################################################################

root = Tk()
root.wm_title("Fallout-rpg helper alpha 0.3.2 by Teemsis")

###############################################################################
# Frames management                                                           #
###############################################################################

frame_0 = Frame(root)
frame_0_0 = Frame(frame_0)
frame_0_1 = Frame(frame_0)
frame_1 = Frame(root)
frame_1_0 = Frame(frame_1)
frame_1_1 = Frame(frame_1)
frame_2 = Frame(root)

content_character_buttons = Frame(frame_1_0)

content_character_clear = Frame(frame_1_0)
content_character_text = Frame(frame_1_0)

content_notes_text = Frame(frame_1_1)

content_dices_buttons = Frame(frame_1_1)
content_dices_clear = Frame(frame_1_1)
content_dices_text = Frame(frame_1_1)

content_credit = Frame(frame_2)

content_character_buttons.pack(pady=20)

content_notes_text.pack(pady=20)

content_dices_buttons.pack()
content_dices_text.pack()
content_dices_clear.pack()

content_character_text.pack()
content_character_clear.pack()

content_credit.pack()

frame_0_0.pack(side=LEFT)
frame_0_1.pack(side=LEFT)
frame_0.pack()
frame_1_0.pack(side=LEFT, padx=20)
frame_1_1.pack(side=LEFT, padx=20)
frame_1.pack()
frame_2.pack()

###############################################################################
# Credits                                                                     #
###############################################################################

Label(content_credit, text='Règles du jeu de rôle -> http://www.fallout-rpg.com/').pack(side='left')
Label(content_credit, text='|').pack(side='left')
Label(content_credit, text='Ajustements d\'après extaz93 -> http://dan.comb.free.fr/').pack(side='right')

###############################################################################
# Character                                                                   #
###############################################################################

content_character_attributs = Frame(content_character_buttons)
content_attribut_label = Frame(content_character_attributs)
content_attribut_entry = Frame(content_character_attributs)

Label(content_attribut_label, text="FO").pack(side=LEFT)
Label(content_attribut_label, text="EN").pack(side=LEFT, padx=1)
Label(content_attribut_label, text="AG").pack(side=LEFT, padx=1)
Label(content_attribut_label, text="PE").pack(side=LEFT, padx=1)
Label(content_attribut_label, text="IN").pack(side=LEFT, padx=1)
Label(content_attribut_label, text="CH").pack(side=LEFT, padx=1)
Label(content_attribut_label, text="C").pack(side=LEFT, padx=1)
content_attribut_label.pack()

entry_fo = Entry(content_attribut_entry, width=2)
entry_fo.insert(1, str(FO))
entry_fo.pack(side=LEFT, padx=3)
entry_en = Entry(content_attribut_entry, width=2)
entry_en.insert(0, str(EN))
entry_en.pack(side=LEFT, padx=3)
entry_ag = Entry(content_attribut_entry, width=2)
entry_ag.insert(0, str(AG))
entry_ag.pack(side=LEFT, padx=3)
entry_pe = Entry(content_attribut_entry, width=2)
entry_pe.insert(0, str(PE))
entry_pe.pack(side=LEFT, padx=3)
entry_in = Entry(content_attribut_entry, width=2)
entry_in.insert(0, str(IN))
entry_in.pack(side=LEFT, padx=3)
entry_ch = Entry(content_attribut_entry, width=2)
entry_ch.insert(0, str(CH))
entry_ch.pack(side=LEFT, padx=3)
entry_c = Entry(content_attribut_entry, width=2)
entry_c.insert(0, str(C))
entry_c.pack(side=LEFT, padx=3)
content_attribut_entry.pack()

content_character_attributs.pack()

button_create_character = Button(content_character_buttons, text='Création d\'un personnage', command=character)
button_create_character.pack()
button_character_levelup = Button(content_character_buttons, text='Passage de niveau', command=level_up)
button_character_levelup.pack()

button_clear_character = Button(content_character_clear, text='Clear personnage', command=clear_character)
button_clear_character.pack()


content_character_text_0 = Frame(content_character_text)
content_character_text_1 = Frame(content_character_text)
content_character_text_2 = Frame(content_character_text)
padx_0_char_txt = 10
pady_0_char_txt = 1
padx_1_char_txt = 1
pady_1_char_txt = 1
padx_2_char_txt = 30
pady_2_char_txt = 50

content_character_primary = Frame(content_character_text_0)
label_character_primary = Label(content_character_primary, text='Attributs primaires')
label_character_primary.pack()
text_character_primary = Text(content_character_primary, height=7, width=23)
text_character_primary.insert('1.0', '')
text_character_primary.pack()
content_character_primary.pack(side=LEFT, padx=padx_0_char_txt, pady=pady_0_char_txt)

content_character_secondary = Frame(content_character_text_0)
label_character_secondary = Label(content_character_secondary, text='Attributs secondaires')
label_character_secondary.pack()
text_character_secondary = Text(content_character_secondary, height=9, width=31)
text_character_secondary.insert('1.0', '')
text_character_secondary.pack()
content_character_secondary.pack(side=LEFT, padx=padx_0_char_txt, pady=pady_0_char_txt)

content_character_skills = Frame(content_character_text_2)
label_character_skills = Label(content_character_skills, text='Compétences')
label_character_skills.pack()
text_character_skills = Text(content_character_skills, height=18, width=28)
text_character_skills.insert('1.0', '')
text_character_skills.pack()
content_character_skills.pack(side=LEFT, padx=padx_2_char_txt, pady=pady_2_char_txt)

content_character_knowledges = Frame(content_character_text_2)
label_character_knowledges = Label(content_character_knowledges, text='Connaissances')
label_character_knowledges.pack()
text_character_knowledges = Text(content_character_knowledges, height=18, width=28)
text_character_knowledges.insert('1.0', '')
text_character_knowledges.pack()
content_character_knowledges.pack(side=LEFT, padx=padx_2_char_txt, pady=pady_2_char_txt)

content_character_others = Frame(content_character_text_0)
label_character_others = Label(content_character_others, text='Autres')
label_character_others.pack()
text_character_others = Text(content_character_others, height=4, width=23)
text_character_others.insert('1.0', '')
text_character_others.pack()
content_character_others.pack(side=LEFT, padx=padx_0_char_txt, pady=pady_0_char_txt)

content_character_text_0.pack()
content_character_text_1.pack()
content_character_text_2.pack()

###############################################################################
# Dices                                                                       #
###############################################################################

button_d100 = Button(content_dices_buttons, text='1d100', command=roll100)
button_d100.pack(side='left')
button_target = Button(content_dices_buttons, text='Membre touché', command=localisation)
button_target.pack(side='left')
button_d6 = Button(content_dices_buttons, text='1d6', command=roll6)
button_d6.pack(side='right')

button_clear_dices = Button(content_dices_clear, text='Clear jets de dés', command=clear_dices)
button_clear_dices.pack()

scrollbar_dices = Scrollbar(content_dices_text)
text_dices = Text(content_dices_text, yscrollcommand=scrollbar_dices.set, height=8, width=18)
scrollbar_dices.config(command=text_dices.yview)
scrollbar_dices.pack(side='right', fill='y')
text_dices.insert('1.0', '')
text_dices.pack()

###############################################################################
# Notes                                                                       #
###############################################################################

label_notes = Label(content_notes_text, text='Notes')
label_notes.pack(side=TOP)
scrollbar_notes = Scrollbar(content_notes_text)
text_notes = Text(content_notes_text, yscrollcommand=scrollbar_notes.set, height=35)
scrollbar_notes.config(command=text_dices.yview)
scrollbar_notes.pack(side='right', fill='y')
text_notes.insert('1.0', '')
text_notes.pack()

###############################################################################
# Finalize                                                                    #
###############################################################################

root.state('zoomed')
root.mainloop()