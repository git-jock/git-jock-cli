#!/usr/bin/env python
import os
import sys

import jock.cli

if os.environ.get('LC_CTYPE', '') == 'UTF-8':
    os.environ['LC_CTYPE'] = 'en_US.UTF-8'


def main():
    return jock.cli.main()


if __name__ == '__main__':
    sys.exit(main())
