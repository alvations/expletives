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
['abortion', 'abuse', 'addict', 'addicts', 'adult', 'africa', 'african', 'american', 'angry', 'arab', 'arabs', 'arousal', 'arouse', 'aroused', 'arouses', 'arousing', 'asian', 'assassin', 'assassinate', 'assassination', 'assault', 'attack', 'australian', 'axe', 'babe', 'babies', 'backdoor', 'backseat', 'beast', 'beat', 'bell', 'bible', 'bigger', 'black', 'blind', 'bombs', 'bra', 'breast', 'breasts', 'bum', 'buried', 'burn', 'cancer', 'carnage', 'catholic', 'cemetery', "children's", 'chinese', 'church', 'cigarette', 'cocktail', 'color', 'colored', 'coloured', 'conservative', 'conspiracy', 'corruption', 'crack', 'cracker', 'crime', 'crimes', 'criminal', 'criminals', 'dead', 'deb', 'deeper', 'demon', 'deposit', 'desire', 'destroy', 'devil', 'die', 'died', 'dies', 'dirty', 'disease', 'diseases', 'dive', 'dome', 'drunk', 'drunken', 'dumb', 'enemy', 'ethiopian', 'ethnic', 'european', 'explosion', 'failed', 'failure', 'fairies', 'fairy', 'faith', 'fat', 'fetus', 'finger', 'food', 'fire', 'firing', 'fraud', 'german', 'get', 'gin', 'golem', 'hand', 'hard', 'harder', 'hate', 'have', 'hell', 'hijack', 'horn', 'illegal', 'israel', "israel's", 'israeli', 'itch', 'jade', 'jam', 'japanese', 'kill', 'killed', 'killer', 'killing', 'kills', 'laid', 'lies', 'love', 'mad', 'mafia', 'middle', 'mother', 'naked', 'nasty', 'one', 'palestinian', 'pawn', 'peck', 'pixie', 'pot', 'primetime', 'radical', 'shoot', 'shooting', 'sick', 'slave', 'stupid', 'terror', 'terrorist', 'toilet', 'torture', 'twinkIe', 'snatch', 'snigger', 'sniggered', 'sniggering', 'sniper', 'sob', 'son']
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
