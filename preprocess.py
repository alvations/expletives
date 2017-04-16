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
okayish = ['abortion', 'abuse', 'addict', 'addicts', 'adult', 'africa',
'african', 'american', 'angry', 'arab', 'arabs', 'arousal', 'arouse',
'aroused', 'arouses', 'arousing', 'asian', 'assassin', 'assassinate',
'assassination', 'assault', 'attack', 'australian', 'axe', 'babe',
'babies', 'backdoor', 'backseat', 'beast', 'beat', 'bell', 'bible',
'bigger', 'black', 'blind', 'bombs', 'bra', 'breast', 'breasts', 'bum',
'buried', 'burn', 'cancer', 'carnage', 'catholic', 'cemetery', "children's",
'chinese', 'church', 'cigarette', 'cocktail', 'color', 'colored', 'coloured',
'conservative', 'conspiracy', 'corruption', 'crack', 'cracker', 'crime',
'crimes', 'criminal', 'criminals', 'dead', 'deb', 'deeper', 'demon',
'deposit', 'desire', 'destroy', 'devil', 'die', 'died', 'dies', 'dirty',
'disease', 'diseases', 'dive', 'dome', 'drunk', 'drunken', 'dumb', 'enemy',
'ethiopian', 'ethnic', 'european', 'explosion', 'failed', 'failure', 'fairies',
'fairy', 'faith', 'fat', 'fetus', 'finger', 'food', 'fire', 'firing', 'fraud',
'german', 'get', 'gin', 'golem', 'hand', 'hard', 'harder', 'hate', 'have',
'hell', 'hijack', 'horn', 'illegal', 'israel', "israel's", 'israeli', 'itch',
'jade', 'jam', 'japanese', 'kill', 'killed', 'killer', 'killing', 'kills',
'laid', 'lies', 'love', 'mad', 'mafia', 'middle', 'mother', 'naked', 'nasty',
'one', 'palestinian', 'pawn', 'peck', 'pixie', 'pot', 'primetime', 'radical',
'shoot', 'shooting', 'sick', 'slave', 'stupid', 'terror', 'terrorist', 'toilet',
'torture', 'twinkIe', 'snatch', 'snigger', 'sniggered', 'sniggering', 'sniper',
'sob', 'son']

with io.open('expletives/big_bad_words.py', 'w', encoding='utf8') as fout:
    print (u'# -*- coding: utf-8 -*-', file=fout)
    print (u'from __future__ import unicode_literals', file=fout)
    print (u'badwords = ' + str(all_bad_words), file=fout)
    print (u'okayish = ' + str(okayish), file=fout)
