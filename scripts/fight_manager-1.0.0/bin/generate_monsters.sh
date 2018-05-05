#!/bin/bash

libexec=$(dirname $0)/../libexec

$libexec/create_monster_json.py --name "Humain_1-3_No_Weapon_No_Armor"      --hp 36 --ap 8 --moral 3 --crit 2 --ac 5 --melee 3 --att 60 --distance 10 --weapon "No_Weapon"      --armor "No_Armor"
$libexec/create_monster_json.py --name "Humain_1-3_Sig_Sauer_P220_Jacket"   --hp 36 --ap 8 --moral 3 --crit 2 --ac 5 --melee 3 --att 60 --distance 10 --weapon "Sig_Sauer_P220" --armor "Jacket"
$libexec/create_monster_json.py --name "Humain_1-3_Colt_6520_Jacket_v2"     --hp 36 --ap 8 --moral 3 --crit 2 --ac 5 --melee 3 --att 60 --distance 10 --weapon "Colt_6520"      --armor "Jacket_v2"
$libexec/create_monster_json.py --name "Humain_1-3_Beretta_Leather"         --hp 36 --ap 8 --moral 3 --crit 2 --ac 5 --melee 3 --att 60 --distance 10 --weapon "Beretta_M92FS"  --armor "Leather"
$libexec/create_monster_json.py --name "Humain_1-3_Beretta_Leather_v2"      --hp 36 --ap 8 --moral 3 --crit 2 --ac 5 --melee 3 --att 60 --distance 10 --weapon "Beretta_M92FS"  --armor "Leather_v2"
$libexec/create_monster_json.py --name "Humain_1-3_Skorpion_Leather_v2"     --hp 36 --ap 8 --moral 3 --crit 2 --ac 5 --melee 3 --att 60 --distance 10 --weapon "Skorpion"       --armor "Leather_v2"
