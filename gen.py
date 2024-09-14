#!/usr/bin/env python
from math import floor
from random import choices, randint
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--file', default=None)
parser.add_argument('-k', '--haystack-len', type=int, required=True)
parser.add_argument('-n', '--needle-len', type=int, required=True)
parser.add_argument('--query-count', type=int, default=1)
parser.add_argument('-w', '--worst-case', action='store_true', default=False)

args = parser.parse_args()

file = args.file
needle_len = args.needle_len
haystack_len = args.haystack_len
qsize = args.query_count

os.makedirs("inputs", exist_ok=True)
if file is None:
    file = f'entrada-{haystack_len}.txt'

file = f'inputs/{file}'

import string

def random_text(len: int) -> str:
    return ''.join(choices(string.ascii_letters, k=len))

worst_case = args.worst_case

with open(file, 'w') as f:
    if worst_case:
        needle = 'y'*(needle_len-1)+'x'
    else:
        needle = random_text(needle_len)

    # haystack
    chunk_size = 4096

    total = haystack_len-needle_len
    chunk_count = floor(total/chunk_size)
    scrap = total%chunk_size

    for chunk_length in [chunk_size]*chunk_count+[scrap]:
        if worst_case:
            f.write('y'*chunk_length)
        else:
            f.write(random_text(chunk_length))

    f.write(needle)
    f.write('\n')
    #end haystack

    f.write(f"{needle}\n")
    f.write(f"{qsize}\n")
    f.write(f"1 {haystack_len}\n")
    for _ in range(qsize-1):
        end = randint(0, haystack_len)
        start = randint(0, end)
        f.write(f"{start} {end}\n")

