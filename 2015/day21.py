import itertools
import copy
from math import ceil

ITEMS = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""


weapons = dict(
    dagger=dict(cost=8, damage=4),
    shortsword=dict(cost=10, damage=5),
    warhammer=dict(cost=25, damage=6),
    longsword=dict(cost=40, damage=7),
    greataxe=dict(cost=74, damage=8),
)
armor = dict(
    leather=dict(cost=13, armor=1),
    chainmail=dict(cost=31, armor=2),
    splintmail=dict(cost=53, armor=3),
    bandedmail=dict(cost=75, armor=4),
    platedmail=dict(cost=102, armor=5),
    none=dict(cost=0, armor=0)
)
rings = dict(
    damage1=dict(cost=25, damage=1),
    damage2=dict(cost=50, damage=2),
    damage3=dict(cost=100, damage=3),
    defense1=dict(cost=20, armor=1),
    defense2=dict(cost=40, armor=2),
    defense3=dict(cost=80, armor=3),
    none=dict(cost=0, armor=0)
)


def dmg(atk_damage, dfd_armor):
    return max(1, atk_damage - dfd_armor)


player_turn = False
player = dict(damage=0, armor=0, hp=100)
boss = dict(damage=9, armor=2, hp=103)

runs = []
for weaponname, weaponstats in weapons.items():
    run = {'cost': weaponstats['cost'], 'stuff': [weaponname]}

    for armorname, armorstats in armor.items():
        run['cost'] += armorstats['cost']
        run['stuff'].append(armorname)

        for chosenrings in itertools.chain(
                itertools.combinations(rings.items(), 1),
                itertools.combinations(rings.items(), 2)
        ):
            run['player'] = player.copy()
            run['boss'] = boss.copy()

            run['player']['damage'] += weaponstats['damage'] + \
                sum(r.get('damage', 0) for (n, r) in chosenrings)
            run['player']['armor'] += armorstats['armor'] + \
                sum(r.get('armor', 0) for (n, r) in chosenrings)

            for n, r in chosenrings:
                run['cost'] += r['cost']
                run['stuff'].append(n)

            run['player_turns_to_win'] = ceil(run['boss']['hp'] / dmg(
                run['player']['damage'], run['boss']['armor']))

            run['boss_turns_to_win'] = ceil(run['player']['hp'] / dmg(
                run['boss']['damage'], run['player']['armor']))

            run['win'] = run['player_turns_to_win'] <= run['boss_turns_to_win']

            runs.append(copy.deepcopy(run))

            for n, r in chosenrings:
                run['cost'] -= r['cost']
                run['stuff'].pop()

        run['cost'] -= armorstats['cost']
        run['stuff'].pop()

print(runs)
print('part 1:', min(
    filter(lambda r: r['win'], runs), key=lambda r: r['cost']))
print('part 2:', max(
    filter(lambda r: not r['win'], runs), key=lambda r: r['cost']))
