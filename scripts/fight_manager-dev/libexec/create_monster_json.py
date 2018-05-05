#!/usr/bin/env python
from argparse import ArgumentParser
import json

parser = ArgumentParser(description="Create a monster as json file to data/monsters.")

parser.add_argument('--name', type=str, help='name [NOT OPTIONAL]')
parser.add_argument('--hp', type=int, help='number of HP', default=10, nargs='?')
parser.add_argument('--ap', type=int, help='number of action points', default=0, nargs='?')
parser.add_argument('--moral', type=int, help='moral strenght', default=0, nargs='?')
parser.add_argument('--crit', type=int, help='critical hit', default=0, nargs='?')
parser.add_argument('--ac', type=int, help='natural armor class', default=0, nargs='?')
parser.add_argument('--armor', type=str, help='armor', default='No_Armor', nargs='?')
parser.add_argument('--att', type=str, help='attack (%%)', default='No_Armor', nargs='?')
parser.add_argument('--distance', type=int, help='max distance to shot without malus', default=1, nargs='?')
parser.add_argument('--weapon', type=str, help='weapon of the monster', default='No_Weapon', nargs='?')
parser.add_argument('--melee', type=int, help='melee dommages bonus', default=0, nargs='?')

args = parser.parse_args()

if args.name is None:
	print(parser.print_help())
	exit(1)

monster = dict()
monster['name'] = args.name
monster['hp'] = args.hp
monster['ap'] = args.ap
monster['moral'] = args.moral
monster['crit'] = args.crit
monster['ac'] = args.ac
monster['armor'] = dict()
monster['att'] = args.att
monster['distance'] = args.distance
monster['weapon'] = dict()
monster['melee'] = args.melee

with open('../data/armors/' + args.armor + '.json', 'r') as fp:
	monster['armor'] = json.load(fp)

with open('../data/weapons/' + args.weapon + '.json', 'r') as fp:
	monster['weapon'] = json.load(fp)

print('== Monster [ ' + args.name + ' ] created ==')
print(monster)

with open("../data/monsters/" + args.name + '.json', 'w') as fp:
	json.dump(monster, fp)
