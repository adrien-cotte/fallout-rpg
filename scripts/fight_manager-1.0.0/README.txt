=== DESCRIPTIONS ===
This software is meant to help Fallout-rpg fights management.
You need to source 'env.sh' and create you database (json) before running 'manage' command.

== bin ==
    env.sh:
        file to source before using software
    generate:
        generate json files in data
    manage:
        start software, need a monster json file (cf. data/monsters) to run

== data ==
= armors =
    Contains all armors json files, cf libexec/create_armor_json.py.
= monsters =
    Contains all monsters json files, cf libexec/create_monster_json.py.
= weapons =
    Contains all weapons json files, cf libexec/create_weapon_json.py.

== lib ==
    Monster.py:
        contains Monster class, this is currently the core of the software

== libexec ==
    create_armor_json.py:
        create an armor as json file to data/armors, with:
          --name        name of armor 
          --ac          armor class
          --thresh      damage threshold
          --norm        normal type resistance
          --laser       laser type resistance
          --fire        fire type resistance
          --plasm       plasma type resistance
          --expl        explosion type resistance
          --elec        electricity/IEM resistance
          --pois        poison resistance
          --rad         radiation resistance
          --malus       malus per action (%)
          --area        protected area : body(0) body+arms(1) all (2)
    create_monster_json.py
        create a monster as json file to data/monsters, with:
          --name        name 
          --hp          number of HP
          --ap          number of action points
          --moral       moral strenght
          --crit        critical hit
          --ac          natural armor class
          --armor       armor
          --att         attack (%)
          --distance    max distance to shot without malus
          --weapon      weapon of the monster
    create_weapon_json.py
        create a weapon as json file to data/weapons, with:
          --name                name of weapon 
          --dices               number of damages dices
          --bonus               bonus of damages
          --spe_dices           number of special damages dices
          --spe_bonus           bonus of special damages
          --distance            max hitting distance (meters)
          --loader              loader capacity
          --ammo_per_shot       number of ammo used per shot
          --spe_ammo_per_shot   number of ammo used per special shot
          --ap                  number of action point
          --spe_ap              number of action point for special
          --dmg_type            damages type (norm, laser, plasm, pois, expl)

=== EXAMPLE ===
$ source ./bin/env.sh
$ generate
$ manage ./data/monsters/Humain_1-3_No_Weapon_No_Armor.json
