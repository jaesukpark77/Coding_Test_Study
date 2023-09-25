# problem link : https://www.codetree.ai/missions/8/problems/special-character?&utm_source=clipboard&utm_medium=text

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