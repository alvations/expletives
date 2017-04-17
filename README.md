# Expletives

Install:

```
pip install -U expletives
```

Usage:

```
>>> from expletives import badwords
>>> sorted(badwords)[:10]
[u'*damn', u'*dyke', u'*fuck*', u'*shit*', u'*whore*', u'2 girls 1 cup', u'2g1c', u'4chan', u'4r5e', u'5h1t']
>>> sorted(badwords)[-10:]
[u'zigabo', u'zipper', u'zipper sniffer', u'zipperhead', u'zippersniffer', u'zoopHilia', u'zoophilen', u'zoophilia', u'zoophilian', u'\U0001f595']

>>> from expletives import okayish
>>> okayish
[u'God', u'Mr', u'abortion', u'abuse', u'addict', u'addicts', u'adult', u'africa', u'african', u'amateur', u'american', u'angry', u'arab', u'arabs', u'are', u'arousal', u'arouse', u'aroused', u'arouses', u'arousing', u'asian', u'assassin', u'assassinate', u'assassination', u'assault', u'athletes foot', u'athletesfoot', u'attack', u'australian', u'axe', u'babe', u'babies', u'backdoor', u'backseat', u'beast', u'beat', u'bell', u'bible', u'bigger', u'black', u'blind', u'bombs', u'bra', u'breast', u'breasts', u'bum', u'buried', u'burn', u'cancer', u'carnage', u'catholic', u'cemetery', u"children's", u'chin', u'chinese', u'christian', u'church', u'cigarette', u'cocktail', u'color', u'colored', u'coloured', u'communist', u'conservative', u'conspiracy', u'corruption', u'crabs', u'crack', u'cracker', u'crime', u'crimes', u'criminal', u'criminals', u'dead', u'death', u'deb', u'deeper', u'demon', u'deposit', u'desire', u'destroy', u'devil', u'die', u'died', u'dies', u'dirty', u'disease', u'diseases', u'dive', u'dome', u'drug', u'drunk', u'drunken', u'dumb', u'enemy', u'ethiopian', u'ethnic', u'european', u'execute', u'executed', u'execution', u'explosion', u'failed', u'failure', u'fairies', u'fairy', u'faith', u'fat', u'fear', u'fetus', u'fight', u'finger food', u'fire', u'firing', u'fraud', u'funeral', u'german', u'get', u'gin', u'girls', u'git', u'glory', u'god', u'golem', u'gun', u'hand', u'hard', u'harder', u'hate', u'have', u'hell', u'hijack', u'hmm', u'hole', u'hook', u'horn', u'hostage', u'illegal', u'israel', u"israel's", u'israeli', u'itch', u'jade', u'jam', u'japanese', u'jew', u'jewish', u'john', u'joint', u'jugs', u'k mart', u'kid', u'kill', u'killed', u'killer', u'killing', u'kills', u'kink', u'laid', u'latin', u'leg', u'lies', u'lingerie', u'lotion', u'love', u'lust', u'lusting', u'mad', u'mafia', u'master', u'mexican', u'middle', u'mideast', u'minority', u'moles', u'mother', u'murder', u'murderer', u'muslim', u'naked', u'nasty', u'nigerian', u'nigerians', u'nuke', u'one', u'palestinian', u'pawn', u'peck', u'period', u'pixie', u'placenta', u'pot', u'poverty', u'premature', u'primetime', u'propaganda', u'protestant', u'racial', u'racist', u'radical', u'radicals', u'refugee', u'reject', u'remains', u'robber', u'satan', u'screw', u'scum', u'servant', u'shoot', u'shooting', u'sick', u'slave', u'snatch', u'snigger', u'sniggered', u'sniggering', u'sniper', u'sob', u'son', u'stupid', u'suicide', u'swallow', u'terror', u'terrorist', u'third', u'tied up', u'toilet', u'tongue', u'tool', u'torture', u'trojan', u'twinkIe', u'violence', u'whiskey', u'wide', u"women's"]
>>> really_badwords = set(badwords).difference(okayish)
>>> sorted(really_badwords)[:10]
['*damn', '*dyke', '*fuck*', '*shit*', '*whore*', '2 girls 1 cup', '2g1c', '4chan', '4r5e', '5h1t']
```

<!--
Tools
====

 - https://www.drupal.org/project/profanity
 - http://search.cpan.org/~tbone/Regexp-Common-profanity_us-4.112150/
 - http://banbuilder.com




Sources
====

 - https://www.reddit.com/r/3dshacks/comments/52ynpz/changes_to_the_bad_word_list_on_111034/
 - https://www.buzzfeed.com/alexfinnis/the-100-most-brilliantly-british-swear-words-in-existence
 - http://wordlist.aspell.net

-->
