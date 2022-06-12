import random as rnd

"""
Pokemon Damage Calculator


A Lv. 90 Charizard (Fire/Flying, Sp. Atk: 205) attacks a Lv. 95
Feraligatr (Water, Sp. Def: 188) with Fire Blast, a Fire-type move
with a Power of 110 and gains a same-type attack bonus.. It hits
the target normally but deals a not very effective damage. The
weather on the field is normal. Given the following conditions,
determine how much damage Charizard’s attack will deal.

"""

print('\n\t\tPOKEMON CALCULATOR')

level = 100
SAtt = 110
Sdef = 90
power = 120
targets = 1
weather = 1
badge = 1
critical = 1,2
critics= rnd.choice(critical)
rands = 0.85,1
randss = rnd.choice(rands)
stab = 1
Type = 1
burn = 1
other = 1

Modifier = targets * weather * badge * critics * randss * stab * Type * burn * other

Damage = ((((((2*level)/5)+2) * power * SAtt / Sdef)/50)+2) * Modifier

print ('\n\tDamage: ' , Damage, '\n')