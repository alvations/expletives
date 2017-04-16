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

with io.open('expletives/big_bad_words.py', 'w', encoding='utf8') as fout:
    print ('# -*- coding: utf-8 -*-', file=fout)
    print ('from __future__ import unicode_literals', file=fout)
    print ('badwords = '+str(all_bad_words), file=fout)
