# problem link : https://www.codetree.ai/missions/8/problems/special-character?&utm_source=clipboard&utm_medium=text

# solution 1
import sys

string = input()

count = dict()

for elem in string:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

for elem in string:
    if count[elem] == 1:
        print(elem)
        sys.exit()

print('None')

# solution 2

import sys
from collections import defaultdict

string = input()

count = defaultdict(lambda: 0)

for elem in string:
    count[elem] += 1

for elem in string:
    if count[elem] == 1:
        print(elem)
        sys.exit()

print('None')