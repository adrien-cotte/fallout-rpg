#!/usr/bin/env python
from argparse import ArgumentParser
import json

parser = ArgumentParser(description="Create an armor as json file to data/armors.")

parser.add_argument('--name', type=str, help='name of armor [NOT OPTIONAL]')
parser.add_argument('--ac', type=int, help='armor class', default=0, nargs='?')
parser.add_argument('--thresh', type=int, help='damage threshold', default=0, nargs='?')
parser.add_argument('--norm', type=int, help='normal type resistance', default=0, nargs='?')
parser.add_argument('--laser', type=int, help='laser type resistance', default=0, nargs='?')
parser.add_argument('--fire', type=int, help='fire type resistance', default=0, nargs='?')
parser.add_argument('--plasm', type=int, help='plasma type resistance', default=0, nargs='?')
parser.add_argument('--expl', type=int, help='explosion type resistance', default=0, nargs='?')
parser.add_argument('--elec', type=int, help='electricity/IEM resistance', default=0, nargs='?')
parser.add_argument('--pois', type=int, help='poison resistance', default=0, nargs='?')
parser.add_argument('--rad', type=int, help='radiation resistance', default=0, nargs='?')
parser.add_argument('--malus', type=int, help='malus per action (%%)', default=0, nargs='?')
parser.add_argument('--area', type=int, help='protected area : body(0) body+arms(1) all (2)' , default=0, nargs='?')

args = parser.parse_args()

if args.name is None:
	print(parser.print_help())
	exit(1)

armor = dict()
armor['name'] = args.name
armor['ac'] = args.ac
armor['thresh'] = args.thresh
armor['norm'] = args.norm
armor['laser'] = args.laser
armor['fire'] = args.fire
armor['plasm'] = args.plasm
armor['expl'] = args.expl
armor['elec'] = args.elec
armor['pois'] = args.pois
armor['rad'] = args.rad
armor['malus'] = args.malus
armor['area'] = args.area

print('== Armor [ ' + args.name + ' ] created ==')
print(armor)

with open("../data/armors/" + args.name + '.json', 'w') as fp:
	json.dump(armor, fp)
