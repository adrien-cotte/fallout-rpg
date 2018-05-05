#!/bin/bash

libexec=$(dirname $0)/../libexec

$libexec/create_armor_json.py --name "No_Armor"

$libexec/create_armor_json.py --name "Jacket"       --ac 5 --thresh 1 --norm 5  --laser 5  --fire 5  --plasm 5  --expl 0 --elec 0 --pois 0 --rad 0 --malus 0 --area 1
$libexec/create_armor_json.py --name "Jacket_v2"    --ac 7 --thresh 2 --norm 10 --laser 10 --fire 10 --plasm 10 --expl 0 --elec 5 --pois 0 --rad 0 --malus 0 --area 1

$libexec/create_armor_json.py --name "Leather"      --ac 15 --thresh 5 --norm 20 --laser 15 --fire 15 --plasm 10 --expl 10 --elec 10 --pois 0 --rad 0 --malus 0 --area 1
$libexec/create_armor_json.py --name "Leather_v2"   --ac 18 --thresh 6 --norm 25 --laser 20 --fire 20 --plasm 15 --expl 15 --elec 15 --pois 0 --rad 0 --malus 5 --area 1
