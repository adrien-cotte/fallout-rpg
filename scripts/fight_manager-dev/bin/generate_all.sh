#!/bin/bash

dir=$(dirname $0)
cd $dir
./generate_weapons.sh
./generate_armors.sh
./generate_monsters.sh
echo "== [ DONE ] =="
echo "== Fallou-rpg data generated in $(realpath ../data)"
