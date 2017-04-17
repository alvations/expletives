# -*- coding: utf-8 -*-

from __future__ import print_function
import io
import os
import re
import sys

dirname = 'data/'

# Theses are not exactly the word lists we are looking...
nonstandard_wordlists = ['chic-fil-a.txt', 'facebook-2013-search.txt',
                        'lssu-2017.txt', 'lssu-till2016.txt']

all_bad_words = set()
for filename in os.listdir(dirname):
    if filename in nonstandard_wordlists:
        continue
    with io.open(dirname+filename, 'r', encoding='utf8') as fin:
        for line in fin:
            if line.startswith('#'):
                continue
            word = re.split(u'\(|\[|-', line.strip())[0].strip()
            if word:
                all_bad_words.add(word)

# A list of words that I think it's okay. - LL.
okayish = ['God', 'Mr', 'abortion', 'abuse', 'addict', 'addicts', 'adult',
'africa', 'african', 'amateur', 'american', 'angry', 'arab', 'arabs', 'are',
'arousal', 'arouse', 'aroused', 'arouses', 'arousing', 'asian', 'assassin',
'assassinate', 'assassination', 'assault', 'athletes foot', 'athletesfoot',
'attack', 'australian', 'axe', 'babe', 'babies', 'backdoor', 'backseat',
'beast', 'beat', 'bell', 'bible', 'bigger', 'black', 'blind', 'bombs', 'bra',
'breast', 'breasts', 'bum', 'buried', 'burn', 'cancer', 'carnage', 'catholic',
'cemetery', "children's", 'chin', 'chinese', 'christian', 'church', 'cigarette',
'cocktail', 'color', 'colored', 'coloured', 'communist', 'conservative',
'conspiracy', 'corruption', 'crabs', 'crack', 'cracker', 'crime', 'crimes',
'criminal', 'criminals', 'dead', 'death', 'deb', 'deeper', 'demon', 'deposit',
'desire', 'destroy', 'devil', 'die', 'died', 'dies', 'dirty', 'disease',
'diseases', 'dive', 'dome', 'drug', 'drunk', 'drunken', 'dumb', 'enemy',
'ethiopian', 'ethnic', 'european', 'execute', 'executed', 'execution',
'explosion', 'failed', 'failure', 'fairies', 'fairy', 'faith', 'fat', 'fear',
'fetus', 'fight', 'finger food', 'fire', 'firing', 'fraud', 'funeral', 'german',
'get', 'gin', 'girls', 'git', 'glory', 'god', 'golem', 'gun', 'hand', 'hard',
'harder', 'hate', 'have', 'hell', 'hijack', 'hmm', 'hole', 'hook', 'horn',
'hostage', 'illegal', 'israel', "israel's", 'israeli', 'itch', 'jade', 'jam',
'japanese', 'jew', 'jewish', 'john', 'joint', 'jugs', 'k mart', 'kid', 'kill',
'killed', 'killer', 'killing', 'kills', 'kink', 'laid', 'latin', 'leg', 'lies',
'lingerie', 'lotion', 'love', 'lust', 'lusting', 'mad', 'mafia', 'master',
'mexican', 'middle', 'mideast', 'minority', 'moles', 'mother', 'murder',
'murderer', 'muslim', 'naked', 'nasty', 'nigerian', 'nigerians', 'nuke',
'one', 'palestinian', 'pawn', 'peck', 'period', 'pixie', 'placenta', 'pot',
'poverty', 'premature', 'primetime', 'propaganda', 'protestant', 'racial',
'racist', 'radical', 'radicals', 'refugee', 'reject', 'remains', 'robber',
'satan', 'screw', 'scum', 'servant', 'shoot', 'shooting', 'sick', 'slave',
'snatch', 'snigger', 'sniggered', 'sniggering', 'sniper', 'sob', 'son',
'stupid', 'suicide', 'swallow', 'terror', 'terrorist', 'third', 'tied up',
'toilet', 'tongue', 'tool', 'torture', 'trojan', 'twinkIe', 'violence',
'whiskey', 'wide', "women's"]

with io.open('expletives/big_bad_words.py', 'w', encoding='utf8') as fout:
    print (u'# -*- coding: utf-8 -*-', file=fout)
    print (u'from __future__ import unicode_literals', file=fout)
    print (u'badwords = ' + str(all_bad_words), file=fout)
    print (u'okayish = ' + str(okayish), file=fout)


with io.open('expletives/okay_words.py', 'w', encoding='utf8') as fout:
    print (u'# -*- coding: utf-8 -*-', file=fout)
    print (u'from __future__ import unicode_literals', file=fout)
    print (u'okayish = ' + str(okayish), file=fout)
