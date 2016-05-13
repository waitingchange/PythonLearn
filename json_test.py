

import argparse
import json
import sys
import os


def main():
    plistFiles = open("test.json","r")
    ps = plistFiles.read()
    plistFiles.close()

    pf = json.loads(ps)
    names = pf["names"]



    print type(names)

    for i in names:
        print i , "lall"


if __name__ == '__main__':
    main()