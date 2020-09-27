#!/usr/bin/env python

"""recaman_sequence.py: This little script calculates the Recaman Sequence."""
__author__      = "Frank Hoffmann"

iterations = 75     # how many numbers do you need?
                    # on my computer the max is ~9223372036854775807

seen = []           # to collect all seen
seen.append(0)      # we start at zero, so this is seen :)

n = 0

for k in range(1,iterations):
    if (n-k not in seen) and not (n-k < 0):   # back first if possible
        n -= k
        seen.append(n)
        #print("Backwards",k,n)
        #print(n)
    else:
        n += k
        seen.append(n)
        #print("Forward",k,n)
        #print(n)

print(seen)
