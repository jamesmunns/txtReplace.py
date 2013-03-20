#!/usr/bin/env python2
import argparse
import os
import re

args_setup = argparse.ArgumentParser(description='Recursive Text Replacement')

args_setup.add_argument('--path',    '-p', type=str, default=os.getcwd(), help='Parent Path to recursively travel', required=False)
args_setup.add_argument('--find',    '-f', type=str, help='Text to find', required=True )
args_setup.add_argument('--replace', '-r', type=str, help='Replacement text', required=True )

pargs = args_setup.parse_args()

textfiles = []
count = 0

for root, dirnames, filenames in os.walk(pargs.path):
    for filename in filter(lambda s: s.endswith(".txt"), filenames):
        textfiles.append(os.path.join(root, filename))

for textfile in textfiles:
    with open(textfile, 'r') as f:
        content, t_count = re.subn(pargs.find, pargs.replace, f.read())
        count += t_count

    with open(textfile, 'w') as f:
        f.write(content)

print "Replaced {} occurences of {} in {}".format(
    str(count), pargs.find, pargs.path)
