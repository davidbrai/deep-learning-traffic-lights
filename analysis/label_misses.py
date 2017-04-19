from subprocess import call
import pandas as pd
import argparse


def main(misses_file):
    labels = {}
    misses = pd.read_csv(misses_file, header=None, names=['file'])
    print "found %d misses" % len(misses)
    i = 0
    while i < len(misses):
        f = misses.loc[i]['file']
        print "At:", i, f
        call(['open', 'images/' + f])
        label = raw_input("[n]one, [r]ed or [g]reen: ")
        if label not in ['n', 'r', 'g']:
            print "error, try again"
        else:
            labels[f] = label
            i += 1
    return labels


if __name__ == "__main__":
    main()