#!/usr/bin/env python

import os, sys, inspect
from time import sleep
from argparse import ArgumentParser
import json
from random import randint

# imports for command line history and autocompletion
import readline
import rlcompleter
readline.parse_and_bind("tab: completion")

libdir = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../lib")))
sys.path.insert(0, libdir)
from Monster import Monster

if __name__ == '__main__':
	parser = ArgumentParser(description='Manage a monster during a fight.')
	parser.add_argument('json', type=str, help='monster data json file to manage')
	args = parser.parse_args()

	monster = Monster(args.json)	
	while(True):
		os.system('clear')
		monster.display()
		try:
			exec("monster." + raw_input("\n[Action command]$ "))
		except:
			print("[COMMAND ERROR]")
			sleep(1)
			continue
