# abbrev_example.py
import argparse
import util
import os

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--inp', action='store', type=str, required=True)
my_parser.add_argument('--out', action='store', type=str, default='out.pdf')
my_parser.add_argument('--c', action='store', type=int, required=True)

args = my_parser.parse_args()
book = util.Book(os.path.basename(os.path.normpath(args.inp)))
for i in range(1,args.c+1):
    with open(f'{args.inp}/{str(i)}.txt','r') as f:
        book.AddChapter(util.CutTextInPages(f.read()),str(i))

