#!/usr/bin/env python
from argparse import ArgumentParser
import json

parser = ArgumentParser(description="Create a weapon as json file to data/weapons.")

parser.add_argument('--name', type=str, help='name of weapon [NOT OPTIONAL]')
parser.add_argument('--dices', type=int, help='number of damages dices', default=1, nargs='?')
parser.add_argument('--bonus', type=int, help='bonus of damages', default=0, nargs='?')
parser.add_argument('--spe_dices', type=int, help='number of special damages dices', default=0, nargs='?')
parser.add_argument('--spe_bonus', type=int, help='bonus of special damages', default=0, nargs='?')
parser.add_argument('--distance', type=int, help='max hitting distance (meters)', default=1, nargs='?')
parser.add_argument('--loader', type=int, help='loader capacity', default=1, nargs='?')
parser.add_argument('--ammo_per_shot', type=int, help='number of ammo used per shot', default=1, nargs='?')
parser.add_argument('--spe_ammo_per_shot', type=int, help='number of ammo used per special shot', default=0, nargs='?')
parser.add_argument('--ap', type=int, help='number of action point', default=3, nargs='?')
parser.add_argument('--spe_ap', type=int, help='number of action point for special', default=3, nargs='?')
parser.add_argument('--dmg_type', type=str, help='damages type (norm, laser, plasm, pois, expl)', default='norm', nargs='?')

args = parser.parse_args()

if args.name is None:
	print(parser.print_help())
	exit(1)

weapon = dict()
weapon['name'] = args.name
weapon['dices'] = args.dices
weapon['bonus'] = args.bonus
weapon['spe_dices'] = args.spe_dices
weapon['spe_bonus'] = args.spe_bonus
weapon['distance'] = args.distance
weapon['loader'] = args.loader
weapon['ammo_per_shot'] = args.ammo_per_shot
weapon['spe_ammo_per_shot'] = args.spe_ammo_per_shot
weapon['ap'] = args.ap
weapon['spe_ap'] = args.spe_ap
weapon['dmg_type'] = args.dmg_type

print('== Weapon [ ' + args.name + ' ] created ==')
print(weapon)

with open("../data/weapons/" + args.name + '.json', 'w') as fp:
	json.dump(weapon, fp)
